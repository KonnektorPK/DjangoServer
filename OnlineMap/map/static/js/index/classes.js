import { message } from './msgAlert.js';

export class LocationManager {
    constructor() {
        this.locations = {
            location: { start: null, end: null },
            cabinet: { start: null, end: null }
        };
    }

    clearLocationStart() {
        this.locations.location.start = null;
        this.locations.cabinet.start = null;
    }

    clearLocationEnd() {
        this.locations.location.end = null;
        this.locations.cabinet.end = null;
    }

    setLocationStart(location, cabinet) {
        this.locations.location.start = location;
        this.locations.cabinet.start = cabinet;
    }

    setLocationEnd(location, cabinet) {
        this.locations.location.end = location;
        this.locations.cabinet.end = cabinet;
    }

    getEndLocation() {
        return this.locations.location.end;
    }

    getLocations() {
        return this.locations.location;
    }

    getStartLocationName() {
        return this.locations.cabinet.start
    }

    getEndLocationName() {
        return this.locations.cabinet.end
    }

    checkForNotNull() {
        return (
            this.locations.location.start !== null &&
            this.locations.location.end !== null &&
            this.locations.cabinet.start !== null &&
            this.locations.cabinet.end !== null
        );
    }

    checkForNotNullStart() {
        return this.locations.location.start !== null
    }

    checkForNotNullEnd() {
        return this.locations.location.end !== null
    }

    checkEquals() {
        return this.locations.location.start === this.locations.location.end;
    }
}

export class LocalStorageService {

    constructor() {
        this.key = 'location'; // Ключ для хранения данных в localStorage
        this.MAX_LENGTH = 5; // Максимальное количество элементов
        this.data = JSON.parse(localStorage.getItem(this.key)) || []; // Получаем данные или создаем пустой массив
    }

    setLocalMemoryCabinets(location, name) {
        // Проверяем, существует ли уже запись с такой location
        const exists = this.data.some(item => item.location === location);
        if (exists) {
            return;
        }

        if (this.data.length === this.MAX_LENGTH) {
            this.data.pop(); // Удаляем первый элемент массива
        }

        // Добавляем новый элемент
        this.data.unshift({ location, name });

        localStorage.setItem(this.key, JSON.stringify(this.data));
    };

    getLengthLocalMemory() {
        return ((JSON.parse(localStorage.getItem(this.key)) || []).length);
    }

    getLocalMemoryCabinets() {
        return JSON.parse(localStorage.getItem(this.key)) || [];
    }

    clearLocalMemory() {
        localStorage.removeItem(this.key);
    }
    // JSON.parse(localStorage.getItem('location') || '[]').forEach(item => {
    //     listenerRecentRequest(item.name).addEventListener('click', () => {
    //         //логика для нажатия на блок
    //     });
    // });
}

export const locationManager = new LocationManager(); //создаем объект для хранения в нем локаций
export const localStorageService = new LocalStorageService(); //создаем объект для хранения в нем последних запросов

export class CabinetsMemoryView {
    constructor(csrfToken, activeInput) {
        this.csrfToken = csrfToken;
        this.activeInput = activeInput;
    }

    setActiveInput(activeInput) {
        this.activeInput = activeInput;
    }

    createFrameItem(name) {
        // Создаём основной контейнер
        const frameItem = document.createElement("div");
        frameItem.className = "frame_item";

        // Создаём SVG для иконки
        const createSVG = (d, fill, stroke, strokeWidth) => {
            const svgNS = "http://www.w3.org/2000/svg";
            const svg = document.createElementNS(svgNS, "svg");
            svg.setAttribute("width", "24");
            svg.setAttribute("height", "24");
            svg.setAttribute("viewBox", "0 0 24 24");
            svg.setAttribute("fill", fill || "none");

            const path = document.createElementNS(svgNS, "path");
            path.setAttribute("d", d);
            if (stroke) path.setAttribute("stroke", stroke);
            if (strokeWidth) path.setAttribute("stroke-width", strokeWidth);
            if (stroke) path.setAttribute("stroke-linecap", "round");
            if (stroke) path.setAttribute("stroke-linejoin", "round");

            svg.appendChild(path);
            return svg;
        };

        // Иконка локации
        frameItem.appendChild(createSVG(
            "M13.024 12H14.6646C15.1175 12 15.4847 12.3698 15.4847 12.8331C15.4847 13.2933 15.1208 13.6663 14.6646 13.6663H12.2036C11.9785 13.6663 11.7744 13.5749 11.6263 13.4259C11.4754 13.272 11.3836 13.0657 11.3836 12.8409V9.49295C11.3836 9.03703 11.7477 8.66747 12.2038 8.66747C12.6568 8.66747 13.024 9.04322 13.024 9.49295L13.024 12ZM5.7223 9.31763C6.54052 7.15336 8.33233 5.40326 10.7056 4.75736C14.6437 3.68555 18.6914 6.0593 19.7466 10.0594C20.8018 14.0594 18.4649 18.1708 14.5268 19.2426C10.5887 20.3145 6.54102 17.9406 5.48575 13.9407L7.07035 13.5094C7.89097 16.6204 11.0393 18.4668 14.1021 17.6332C17.165 16.7997 18.9828 13.6018 18.1621 10.4908C17.3414 7.37972 14.1931 5.53334 11.1303 6.36693C9.19358 6.89404 7.75466 8.36634 7.16608 10.1643L9.02268 11.2531L5.06153 12.3313L4 8.30758L5.7223 9.31763Z",
            "#828180"
        ));

        // Текст локации
        const spanLocation = document.createElement("span");
        spanLocation.className = "span_location";
        spanLocation.textContent = name;
        frameItem.appendChild(spanLocation);

        // Кнопка удаления
        const button = document.createElement("button");
        button.setAttribute("onclick", "removeItem(this)");
        button.appendChild(createSVG(
            "M7 7L17 17M7 17L17 7",
            "none",
            "#828180",
            "2"
        ));
        frameItem.appendChild(button);

        // Добавляем в родительский элемент
        document.getElementById('recent_queries').appendChild(frameItem);
        return frameItem
    };

    drawFrequentFrame() {
        document.getElementById('recent_queries').innerHTML = '';

        localStorageService.getLocalMemoryCabinets().forEach(cabinet => {
            this.createFrameItem(cabinet.name).addEventListener('click', () => {
                let obj = new BlockClickHandler(this.csrfToken, this.activeInput, cabinet.name, cabinet.location);
                obj.click();
            });
        });
    }

    drawFrequentFrameInput(activeInput) {
        document.getElementById('recent_queries').innerHTML = '';

        localStorageService.getLocalMemoryCabinets().forEach(cabinet => {
            this.createFrameItem(cabinet.name).addEventListener('click', () => {
                let obj = new BlockClickHandler(this.csrfToken, activeInput, cabinet.name, cabinet.location);
                obj.click();
            });
        });
    }
}

export class BlockView {

    static showСlearEnd() {
        document.getElementById('clearEnd').style.display = 'block';
    }
    static hidСlearEnd() {
        document.getElementById('clearEnd').style.display = 'none';
    }

    static showСlearStart() {
        document.getElementById('clearStart').style.display = 'block';
    }
    static hidСlearStart() {
        document.getElementById('clearStart').style.display = 'none';
    }

    static showFrequent() {
        document.getElementById('frequent_frame').style.display = 'block';
    }
    static hideFrequent() {
        document.getElementById('frequent_frame').style.display = 'none';
    }

    static showRecent() {
        if (localStorageService.getLengthLocalMemory() > 0) { document.getElementById('recent_frame').style.display = 'block'; }
    }
    static hideRecent() {
        document.getElementById('recent_frame').style.display = 'none';
    }

    static showResult() {
        document.getElementById('result_frame').style.display = 'flex';
    }
    static hideResult() {
        document.getElementById('result_frame').style.display = 'none';
    }

    static showNoResult() {
        document.getElementById('noresult_frame').style.display = 'flex';
    }
    static hideNoResult() {
        document.getElementById('noresult_frame').style.display = 'none';
    }

}

export class RouteDataSender {

    constructor(csrfToken) {
        this.csrfToken = csrfToken;
    }

    sendRouteData() {
        const startTime = performance.now();
        const locations = locationManager.getLocations();

        document.getElementById('locationEnd').value = locationManager.getEndLocationName();
        document.getElementById('locationStart').value = locationManager.getStartLocationName();

        localStorageService.setLocalMemoryCabinets(locationManager.getEndLocation(), locationManager.getEndLocationName())
        console.log(locations)

        fetch('/getMapFromPoints/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': this.csrfToken,
            },
            body: JSON.stringify({ location_start: locations.start, location_end: locations.end }),
        })
            .then(response => {
                const endTime = performance.now(); // Засекаем время завершения запроса
                console.log(`Server response time: ${(endTime - startTime).toFixed(2)} ms`);
                return response.json();
            })
            .then(data => {
                document.getElementById('search_text').setAttribute('style', 'display: none');
                document.getElementById('search_route').setAttribute('style', 'display: flex');
                document.getElementById('recent_frame').setAttribute('style', 'display: block');
                document.getElementById('search_result_start').textContent = locationManager.getStartLocationName();
                document.getElementById('search_result_end').textContent = locationManager.getEndLocationName();

                const dataMaps = data.results;

                if (dataMaps) {
                    document.getElementById('search_overlay').classList.remove('visible')
                    document.getElementById('frequent_frame').setAttribute('style', 'display: block')
                }

                if (Array.isArray(dataMaps)) {
                    document.getElementById('all_maps_placeholder').innerHTML = '';
                    document.getElementById('all_maps_placeholder').innerHTML = dataMaps[0];
                    document.getElementById('floor_up').style.display = 'block';
                    document.getElementById('floor_down').style.display = 'block';
                    document.getElementById('search_overlay').classList.remove('visible')
                }
                else if (!Array.isArray(dataMaps)) {
                    document.getElementById('all_maps_placeholder').innerHTML = '';
                    document.getElementById('all_maps_placeholder').innerHTML = dataMaps;
                    document.getElementById('floor_up').style.display = 'none';
                    document.getElementById('floor_down').style.display = 'none';
                    document.getElementById('search_overlay').classList.remove('visible')
                }
                else {
                    message('Error: ' + (data.error || 'Unknown error'));
                }
            })
            .catch(error => {
                message(error.message, 'Error');
            });
    }
}

export class BlockClickHandler {

    constructor(csrfToken, activeInput, name, location) {
        this.csrfToken = csrfToken;
        this.activeInput = activeInput;
        this.name = name;
        this.location = location;
    }

    click() {

        if (this.activeInput.id === 'locationStart') {
            locationManager.setLocationStart(this.location, this.name)
            BlockView.hidСlearStart();
        } else {
            locationManager.setLocationEnd(this.location, this.name)
            BlockView.hidСlearEnd();
        }

        if (locationManager.checkEquals()) {
            message('Точка начала и конца не может быть в одном месте! Попробуйте еще раз :)', 'Упс')
            return;
        }
        this.activeInput.value = this.name;

        BlockView.showFrequent();
        BlockView.showRecent();
        BlockView.hideResult();
        BlockView.hideNoResult();

        if (locationManager.checkForNotNull() && !locationManager.checkEquals()) {
            let obj = new RouteDataSender(this.csrfToken)
            obj.sendRouteData();
        }
    }
}

export class CabinetSearchView {

    constructor(csrfToken, cabinetsInput) {
        this.csrfToken = csrfToken;
        this.cabinetsInput = cabinetsInput;
    }

    createFrameItem(cabinet) {
        const frameItem = document.createElement('div');
        frameItem.classList.add('frame_item');

        const svgIcon = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svgIcon.setAttribute('width', '24');
        svgIcon.setAttribute('height', '24');
        svgIcon.setAttribute('viewBox', '0 0 24 24');
        svgIcon.setAttribute('fill', 'none');
        svgIcon.innerHTML = `
          <g clip-path="url(#clip0_195_1304)">
            <path d="M14.3996 9.6002C14.3996 8.2402 13.3596 7.2002 11.9996 7.2002C10.6396 7.2002 9.59961 8.2402 9.59961 9.6002C9.59961 10.9602 10.6396 12.0002 11.9996 12.0002C13.3596 12.0002 14.3996 10.9602 14.3996 9.6002ZM11.1996 9.6002C11.1996 9.1202 11.5196 8.8002 11.9996 8.8002C12.4796 8.8002 12.7996 9.1202 12.7996 9.6002C12.7996 10.0802 12.4796 10.4002 11.9996 10.4002C11.5196 10.4002 11.1996 10.0002 11.1996 9.6002Z" fill="#828180" />
            <path d="M15.5198 14C16.6398 12.56 17.5998 10.96 17.5998 9.6C17.5998 6.48 15.1198 4 11.9998 4C8.87981 4 6.3998 6.48 6.3998 9.6C6.3998 10.96 7.35981 12.56 8.4798 14C6.1598 14.48 4.7998 15.52 4.7998 16.8C4.7998 18.88 8.39981 20 11.9998 20C15.5998 20 19.1998 18.88 19.1998 16.8C19.1998 15.52 17.8398 14.48 15.5198 14ZM11.9998 5.6C14.2398 5.6 15.9998 7.36 15.9998 9.6C15.9998 11.12 13.7598 13.76 11.9998 15.44C10.2398 13.76 7.9998 11.12 7.9998 9.6C7.9998 7.36 9.75981 5.6 11.9998 5.6ZM11.9998 18.4C8.39981 18.4 6.3998 17.28 6.3998 16.8C6.3998 16.48 7.3598 15.76 9.6798 15.36C10.5598 16.24 11.2798 16.96 11.4398 17.12L11.9998 17.6L12.5598 17.12C12.7198 16.96 13.5198 16.32 14.3198 15.36C16.6398 15.68 17.5998 16.48 17.5998 16.8C17.5998 17.28 15.5998 18.4 11.9998 18.4Z" fill="#828180" />
          </g>
          <defs>
            <clipPath id="clip0_195_1304">
              <rect width="16" height="16" fill="white" transform="translate(4 4)" />
            </clipPath>
          </defs>
        `;
        frameItem.appendChild(svgIcon);

        const spanLocation = document.createElement('span');
        spanLocation.classList.add('span_location');
        spanLocation.textContent = cabinet.nameCabinet;
        frameItem.appendChild(spanLocation);

        const spanBuilding = document.createElement('span');
        spanBuilding.classList.add('span_building');
        spanBuilding.textContent = cabinet.frame;
        frameItem.appendChild(spanBuilding);

        frameItem.addEventListener('click', () => {
            let obj = new BlockClickHandler(this.csrfToken, this.cabinetsInput, cabinet.nameCabinet, cabinet.location);
            obj.click();
        });

        return frameItem;
    };

    drawCabinets(cabinets) {
        if (this.cabinetsInput.value == '') {
            BlockView.showFrequent();
            BlockView.showRecent();
            BlockView.hideResult();
            BlockView.hideNoResult();
        }
        else if (cabinets.length === 0) {
            BlockView.hideFrequent();
            BlockView.hideRecent();
            BlockView.hideResult();
            BlockView.showNoResult();
        } else {
            BlockView.hideFrequent();
            BlockView.hideRecent();
            BlockView.showResult();
            BlockView.hideNoResult();
        }

        document.getElementById('all_result_queries').innerHTML = '';

        cabinets.forEach(cabinet => {
            document.getElementById('all_result_queries').appendChild(this.createFrameItem(cabinet));
        });
    }
}

export class SearchCabinetInDB {

    constructor(csrfToken, cabinetsInput) {
        this.csrfToken = csrfToken;
        this.cabinetsInput = cabinetsInput;
    }

    showSimilarCabinets() {

        fetch('/search_location/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': this.csrfToken,
            },
            body: JSON.stringify({ cabinet: this.cabinetsInput.value, language: localStorage.getItem('language') }),
        })
            .then(response => response.json())
            .then(data => {
                if (data.results) {
                    let obj = new CabinetSearchView(this.csrfToken, this.cabinetsInput)
                    obj.drawCabinets(data.results)
                } else {
                    message('Error: ' + (data.error || 'Unknown error'));
                }
            })
            .catch(error => {
                console.error('Error:', error);
                message('Error: ' + error.message);
            });
    }
}