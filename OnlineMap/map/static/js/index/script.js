import { message } from './msgAlert.js';

import { locationManager } from './classes.js'


if (localStorage.getItem("language") === 'en' && !window.location.href.includes('/en/')) {
  window.location.href = window.location.href.replace('/location/', '/en/location/')
} //если в localStorage язык английский, а в ссылке русский, перенаправляем пользователя на английскуя версию

document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('language_toggle').addEventListener('click', (event) => {
    const currentUrl = window.location.href;

    if (currentUrl.includes('/en/')) {
      const newUrl = currentUrl.replace('/en/', '/');
      window.location.href = newUrl;
      localStorage.setItem("language", "ru");
    } else {
      const newUrl = currentUrl.replace('/location/', '/en/location/');
      window.location.href = newUrl;
      localStorage.setItem("language", "en");
    }
  });
});

document.addEventListener('DOMContentLoaded', () => { //получаем location ползователя
  const path = window.location.pathname;
  const digits = path.match(/\d+/);

  if (digits) {
    locationManager.setLocationStart(digits[0], document.getElementById('locationStart').value);
  }
})

document.addEventListener('DOMContentLoaded', () => {
  // Error overlay
  const overlay = document.getElementById('error_overlay');
  // const searchOver = document.getElementById('search_overlay');
  const openButton = document.querySelector('.error_button button'); // Кнопка, открывающая оверлей
  const closeSearchButton = document.getElementById('close_search');
  const closeErrorButton = document.getElementById('close_error');
  const form = document.getElementById('error_form');

  openButton.addEventListener('click', () => {
    overlay.classList.add('visible');
  });

  closeErrorButton.addEventListener('click', () => {
    overlay.classList.remove('visible');
  });

  overlay.addEventListener("touchstart", (e) => {
    window.startY = e.touches[0].clientY; // Запоминаем начальную точку
  }, { passive: false });

  overlay.addEventListener("touchmove", (e) => {
    const deltaY = e.touches[0].clientY - window.startY;

    if (deltaY > 100) { // Если свайп вниз
      overlay.classList.remove('visible');
      e.preventDefault(); // Блокируем обновление страницы
    }
  }, { passive: false });

  // Prevent page refresh on swipe down
  document.addEventListener('touchmove', (e) => {
    if (window.startY && e.touches[0].clientY > window.startY) {
      e.preventDefault(); // Блокируем обновление страницы при свайпе вниз
    }
  }, { passive: false });

  overlay.addEventListener('click', (event) => {
    if (event.target === overlay) {
      overlay.classList.remove('visible');
    }
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const overlay = document.getElementById('error_overlay');
  const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

  document.getElementById('submitBtn').addEventListener('click', (event) => {
    event.preventDefault();

    let user = document.getElementById('user_name').value;
    let description = document.getElementById('user_problem').value;
    let fileInput = document.getElementById('user_file'); // Инпут для файла
    const file = fileInput.files[0]; // Получаем первый выбранный файл

    if (!user.trim() || !description.trim()) {
      message('Пожалуйста, заполните все поля.');
      return; // Прекращаем выполнение, если одно из полей пустое
    }

    // Создаем объект FormData для передачи файла и других данных
    const formData = new FormData();
    formData.append('user', user);
    formData.append('description', description);
    if (file) {
      formData.append('file', file); // Добавляем файл, если он выбран
    }

    fetch('/create-error-report/', {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken, // Передача CSRF-токена
      },
      body: formData, // Используем FormData вместо JSON
    })
      .then(response => response.json())
      .then(data => {
        if (data.message) {
          document.getElementById('user_name').value = '';
          document.getElementById('user_problem').value = '';
          document.getElementById('user_file').value = '';
          message(data.message, 'Сообщение отправлено!');
        } else {
          message((data.error || 'Unknown error'));
        }
      })
      .catch(error => {
        message(error.message);
      });

    overlay.classList.remove('visible');
  });
});