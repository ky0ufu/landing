document.addEventListener('DOMContentLoaded', function() {
    // Обработчик для кнопки "Читать дальше"
    document.querySelector('.btn-more').addEventListener('click', function() {
        window.location.href = 'about.html';
    });

    // Функция для интерактивной карты
    const regions = document.querySelectorAll('#map area');
    regions.forEach(region => {
        region.addEventListener('click', function(event) {
            event.preventDefault();
            const regionName = this.getAttribute('data-name');
            // Вызов модального окна или переход на страницу региона
            alert(`Вы выбрали регион: ${regionName}`);
        });
    });
});


document.addEventListener('DOMContentLoaded', (event) => {
    const video = document.getElementById('video-player');
    
    video.addEventListener('timeupdate', (e) => {
        console.log(`Current time: ${video.currentTime}`);
    });

    video.addEventListener('seeked', (e) => {
        console.log(`Seeked to: ${video.currentTime}`);
    });

    video.addEventListener('playing', (e) => {
        console.log('Video is playing');
    });

    video.addEventListener('pause', (e) => {
        console.log('Video is paused');
    });
});