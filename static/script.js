var map = L.map('map').setView([52.5, 137.0], 4); // Координаты и масштаб для Дальнего Востока России

        // Добавление базового слоя карты
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Пример добавления маркера
        L.marker([48.5, 135.1]).addTo(map) // Координаты Хабаровска
            .bindPopup('Хабаровск')
            .openPopup();