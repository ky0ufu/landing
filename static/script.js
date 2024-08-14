const svg = document.querySelector('svg');
const textContainer = document.getElementById('region_inf');

svg.addEventListener('click', (e) => {
    const clickedElement = e.target.closest('g');
    const link = document.createElement('a');
    if (clickedElement && clickedElement.classList.contains('nosite') && clickedElement.classList.contains('other')) {
        textContainer.textContent = 'Для округа ' + clickedElement.getAttribute('title') + ' нет окружного сайта. Вместо этого предлагаем посетить сайт ';
        link.setAttribute('href', 'https://rsr-online.ru/');
        link.innerText = 'Российского союза ректоров.';
        textContainer.appendChild(link);
    }
    else if (clickedElement && clickedElement.classList.contains('other')) {
        textContainer.textContent = 'Сайт округа ';
        link.setAttribute('href',  clickedElement.getAttribute('site'));
        link.innerText = clickedElement.getAttribute('title') + '.';
        textContainer.appendChild(link);
    }

    if (clickedElement && clickedElement.classList.contains('nosite') && clickedElement.classList.contains('exist')) {
        textContainer.textContent = 'Для региона ' + clickedElement.getAttribute('title') + ' нет регионального сайта. Вместо этого предлагаем посетить сайт ';
        link.setAttribute('href', 'https://rsr-online.ru/');
        link.innerText = 'Российского союза ректоров.';
        textContainer.appendChild(link);
    }
    else if (clickedElement && clickedElement.classList.contains('exist')) {
        textContainer.textContent = 'Сайт региона ';
        link.setAttribute('href',  clickedElement.getAttribute('site'));
        link.innerText = clickedElement.getAttribute('title') + '.';
        textContainer.appendChild(link);
    }

    if (clickedElement && clickedElement.classList.contains('nexist')) {
        textContainer.textContent = 'Для региона ' + clickedElement.getAttribute('title') + ' нет ни региональных сайтов, ни вузов.';
    }
});