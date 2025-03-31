import { SearchCabinetInDB } from './classes.js'
import { BlockClickHandler } from './classes.js'
import { BlockView } from './classes.js'
import { CabinetsMemoryView } from './classes.js';

import { locationManager } from './classes.js'
import { localStorageService } from './classes.js'


document.addEventListener('DOMContentLoaded', () => {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    const cabinetsInputEnd = document.getElementById('locationEnd');
    const cabinetsInputStart = document.getElementById('locationStart');

    const searchOverlay = document.getElementById('search_overlay');
    let activeInput = null;

    document.getElementById('search_route').setAttribute('style', 'display: none');

    cabinetsInputStart.addEventListener('input', () => {
        if (cabinetsInputStart.value.length > 0) {
            BlockView.showСlearStart();
        } else {
            BlockView.hidСlearStart();
        }

        let objInputStart = new SearchCabinetInDB(csrfToken, cabinetsInputStart)
        objInputStart.showSimilarCabinets(cabinetsInputStart.value)
    });

    cabinetsInputStart.addEventListener('focus', () => {
        let obj = new CabinetsMemoryView(csrfToken, cabinetsInputStart);
        obj.drawFrequentFrameInput(cabinetsInputStart);
        BlockView.hidСlearEnd();

        if (cabinetsInputStart.value.length > 0) {
            BlockView.showСlearStart();
        } else {
            BlockView.hidСlearStart();
        }

        activeInput = cabinetsInputStart;

        // if (!locationManager.checkForNotNullEnd()) {
        //     cabinetsInputEnd.value = '';
        //     document.getElementById('clearEnd').style.display = 'none';
        //     BlockView.showFrequent();
        //     BlockView.showRecent();
        //     BlockView.hideResult();
        //     BlockView.hideNoResult();
        // }

        let objInputStart = new SearchCabinetInDB(csrfToken, cabinetsInputStart)
        objInputStart.showSimilarCabinets(cabinetsInputStart.value)
    });

    cabinetsInputEnd.addEventListener('input', () => {
        if (cabinetsInputEnd.value.length > 0) {
            BlockView.showСlearEnd();
        } else {
            BlockView.hidСlearEnd();
        }

        let objInputEnd = new SearchCabinetInDB(csrfToken, cabinetsInputEnd)
        objInputEnd.showSimilarCabinets(cabinetsInputEnd.value)
    });

    cabinetsInputEnd.addEventListener('focus', () => {
        let obj = new CabinetsMemoryView(csrfToken, cabinetsInputStart);
        obj.drawFrequentFrameInput(cabinetsInputEnd);
        BlockView.hidСlearStart();

        if (cabinetsInputEnd.value.length > 0) {
            BlockView.showСlearEnd();
        } else {
            BlockView.hidСlearEnd();
        }

        activeInput = cabinetsInputEnd;

        // if (!locationManager.checkForNotNullStart()) {
        //     cabinetsInputStart.value = '';
        //     document.getElementById('clearStart').style.display = 'none';
        //     BlockView.showFrequent();
        //     BlockView.showRecent();
        //     BlockView.hideResult();
        //     BlockView.hideNoResult();
        // }

        let objInputEnd = new SearchCabinetInDB(csrfToken, cabinetsInputEnd);
        objInputEnd.showSimilarCabinets(cabinetsInputEnd.value);
    });

    const clearInput = (inputElement, clearButtonId, clearLocationMethod) => {
        inputElement.value = '';
        document.getElementById(clearButtonId).style.display = 'none';
        BlockView.showFrequent();
        BlockView.showRecent();
        BlockView.hideResult();
        BlockView.hideNoResult();
        clearLocationMethod();
    }

    document.getElementById('clearRecent').addEventListener('click', () => {
        BlockView.hideRecent();
        localStorageService.clearLocalMemory();
        let obj = new CabinetsMemoryView(csrfToken, cabinetsInputStart);
        obj.drawFrequentFrame();
    });

    document.getElementById('clearStart').addEventListener('click', () => {
        clearInput(cabinetsInputStart, 'clearStart', () => locationManager.clearLocationStart());
    });

    document.getElementById('clearEnd').addEventListener('click', () => {
        clearInput(cabinetsInputEnd, 'clearEnd', () => locationManager.clearLocationEnd());
    });

    document.getElementById('canteenBtn').addEventListener('click', () => {
        let obj = new BlockClickHandler(csrfToken, activeInput, document.getElementById('diningRoom').textContent, '07000000');
        obj.click();
    });

    document.getElementById('maleToiletBtn').addEventListener('click', () => {
        let obj = new BlockClickHandler(csrfToken, activeInput, document.getElementById('menToilet').textContent, '08000000');
        obj.click();
    });

    document.getElementById('femaleToiletBtn').addEventListener('click', () => {
        let obj = new BlockClickHandler(csrfToken, activeInput, document.getElementById('womenToilet').textContent, '09000000');
        obj.click();
    });

    document.querySelector('.search_box').addEventListener('click', () => {

        if (localStorageService.getLengthLocalMemory() > 0) {
            BlockView.showRecent();
        }

        let obj = new CabinetsMemoryView(csrfToken, cabinetsInputStart);
        obj.drawFrequentFrame()
        searchOverlay.classList.add('visible');
    });

    document.querySelector('#search_overlay #close_search').addEventListener('click', () => {
        // console.log(localStorage.getItem("language"));
        searchOverlay.classList.remove('visible');
    });

    document.getElementById('search_overlay').addEventListener('click', (event) => {

        if (event.target === searchOverlay) {
            searchOverlay.classList.remove('visible');
        }
    });
});