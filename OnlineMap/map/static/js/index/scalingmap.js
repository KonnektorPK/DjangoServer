document.addEventListener('DOMContentLoaded', () => {
    const mapElement = document.getElementById('all_maps_placeholder');
    const zoomInButton = document.getElementById('zoom_in');
    const zoomOutButton = document.getElementById('zoom_out');

    let scale = 1; // Начальный масштаб
    let translateX = 0; // Начальное смещение по X
    let translateY = 0; // Начальное смещение по Y
    let targetTranslateX = 0; // Целевое смещение по X
    let targetTranslateY = 0; // Целевое смещение по Y
    let isDragging = false; // Флаг для отслеживания перетаскивания
    let startX, startY; // Начальные координаты при перетаскивании

    // Ограничения для масштаба
    const minScale = 1;
    const maxScale = 15;

    let maxTranslateX, maxTranslateY; // Максимальное смещение
    let minTranslateX, minTranslateY; // Минимальное смещение

    // Функция для обновления ограничений перемещения
    const updateTranslateLimits = () => {
        const mapWidth = mapElement.offsetWidth * scale;
        const mapHeight = mapElement.offsetHeight * scale;
        const viewportWidth = window.innerWidth;
        const viewportHeight = window.innerHeight;

        // Максимальное и минимальное смещение по X и Y
        maxTranslateX = Math.max((mapWidth - viewportWidth) / 2, 0);
        maxTranslateY = Math.max((mapHeight - viewportHeight) / 2, 0);
        minTranslateX = -maxTranslateX;
        minTranslateY = -maxTranslateY;

        // Если масштаб минимальный, фиксируем карту в центре
        if (scale === minScale) {
            translateX = 0;
            translateY = 0;
            targetTranslateX = 0;
            targetTranslateY = 0;
        }
    };

    // Инициализация ограничений перемещения
    updateTranslateLimits();

    // Функция для обновления трансформации
    const updateTransform = () => {
        mapElement.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale})`;
    };

    // Функция для ограничения смещения
    const clampTranslate = () => {
        targetTranslateX = Math.min(maxTranslateX, Math.max(minTranslateX, targetTranslateX));
        targetTranslateY = Math.min(maxTranslateY, Math.max(minTranslateY, targetTranslateY));
    };

    // Функция для изменения масштаба
    const zoom = (delta) => {
        const newScale = scale + delta;

        // Ограничение масштаба
        if (newScale >= minScale && newScale <= maxScale) {
            // Обновление масштаба
            scale = newScale;

            // Обновление ограничений перемещения
            updateTranslateLimits();

            // Корректировка смещения при изменении масштаба
            if (scale !== minScale) {
                translateX = translateX * (scale / (scale - delta));
                translateY = translateY * (scale / (scale - delta));
                targetTranslateX = targetTranslateX * (scale / (scale - delta));
                targetTranslateY = targetTranslateY * (scale / (scale - delta));
            }

            // Ограничение смещения
            clampTranslate();

            // Применение трансформации
            updateTransform();
        }
    };

    // Обработчик колесика мыши для изменения масштаба
    mapElement.addEventListener('wheel', (event) => {
        event.preventDefault();
        const delta = event.deltaY < 0 ? 1 : -1; // Увеличение или уменьшение масштаба
        zoom(delta);
    });

    // Обработчик кнопки увеличения
    zoomInButton.addEventListener('click', () => {
        zoom(1);
    });

    // Обработчик кнопки уменьшения
    zoomOutButton.addEventListener('click', () => {
        zoom(-1);
    });

    // Обработчик начала перетаскивания
    mapElement.addEventListener('mousedown', (event) => {
        if (event.button === 0 && scale !== minScale) { // Левая кнопка мыши и не минимальный масштаб
            isDragging = true;
            startX = event.clientX - translateX;
            startY = event.clientY - translateY;
        }
    });

    // Обработчик перемещения мыши
    document.addEventListener('mousemove', (event) => {
        if (isDragging && scale !== minScale) { // Перетаскивание только если не минимальный масштаб
            targetTranslateX = event.clientX - startX;
            targetTranslateY = event.clientY - startY;

            // Ограничение смещения
            clampTranslate();
        }
    });

    // Обработчик окончания перетаскивания
    document.addEventListener('mouseup', () => {
        isDragging = false;
    });

    // Обработчик свайпа (для мобильных устройств)
    let touchStartX, touchStartY;
    let initialDistance = null;

    mapElement.addEventListener('touchstart', (event) => {
        if (event.touches.length === 2) {
            // Начало жеста pinch-to-zoom
            const touch1 = event.touches[0];
            const touch2 = event.touches[1];
            initialDistance = Math.hypot(
                touch2.clientX - touch1.clientX,
                touch2.clientY - touch1.clientY
            );
        } else if (event.touches.length === 1 && scale !== minScale) {
            // Начало перетаскивания (только если не минимальный масштаб)
            const touch = event.touches[0];
            touchStartX = touch.clientX - translateX;
            touchStartY = touch.clientY - translateY;
        }
    });

    mapElement.addEventListener('touchmove', (event) => {
        event.preventDefault();
        if (event.touches.length === 2) {
            // Обработка жеста pinch-to-zoom
            const touch1 = event.touches[0];
            const touch2 = event.touches[1];
            const currentDistance = Math.hypot(
                touch2.clientX - touch1.clientX,
                touch2.clientY - touch1.clientY
            );

            if (initialDistance !== null) {
                const newScale = scale * (currentDistance / initialDistance);

                // Ограничение масштаба
                if (newScale >= minScale && newScale <= maxScale) {
                    scale = newScale;

                    // Обновление ограничений перемещения
                    updateTranslateLimits();

                    // Корректировка смещения при изменении масштаба
                    if (scale !== minScale) {
                        translateX = translateX * (scale / (scale / (currentDistance / initialDistance)));
                        translateY = translateY * (scale / (scale / (currentDistance / initialDistance)));
                        targetTranslateX = targetTranslateX * (scale / (scale / (currentDistance / initialDistance)));
                        targetTranslateY = targetTranslateY * (scale / (scale / (currentDistance / initialDistance)));
                    }

                    // Ограничение смещения
                    clampTranslate();

                    // Применение трансформации
                    updateTransform();
                }
            }
        } else if (event.touches.length === 1 && scale !== minScale) {
            // Обработка перетаскивания (только если не минимальный масштаб)
            const touch = event.touches[0];
            targetTranslateX = touch.clientX - touchStartX;
            targetTranslateY = touch.clientY - touchStartY;

            // Ограничение смещения
            clampTranslate();
        }
    });

    mapElement.addEventListener('touchend', () => {
        initialDistance = null;
    });

    // Обновление ограничений при изменении размера окна
    window.addEventListener('resize', () => {
        updateTranslateLimits();
        clampTranslate();
        updateTransform();
    });

    // Функция для плавного обновления позиции карты
    const smoothUpdate = () => {
        // Интерполяция между текущей позицией и целевой позицией
        translateX += (targetTranslateX - translateX) * 0.15;
        translateY += (targetTranslateY - translateY) * 0.15;

        // Применение трансформации
        updateTransform();

        // Продолжаем анимацию
        requestAnimationFrame(smoothUpdate);
    };

    // Запуск анимации
    smoothUpdate();
});