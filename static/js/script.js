
const svg = document.querySelector('svg');
const textContainer = document.getElementById('region_inf');


svg.addEventListener('mouseover', (e) => {
    const tooltipElement = e.target.closest('g');
    const tooltip = document.createElement('div');
            
    tooltip.textContent = tooltipElement.getAttribute('title');

    tooltip.style.backgroundColor = '#f3f3f1';
    tooltip.style.padding = '5px';
    tooltip.style.position = 'absolute';
    tooltip.style.top = (e.clientY + 15) + 'px';
    tooltip.style.left = (e.clientX + 15) + 'px';
    tooltip.classList.add('tooltip')

            
    document.body.appendChild(tooltip);
});
          
svg.addEventListener('mousemove', (e) => {
    const tooltip = document.querySelector('.tooltip');
    tooltip.style.top = (e.clientY + 15) + 'px';
    tooltip.style.left = (e.clientX + 15) + 'px';
});
        
svg.addEventListener('mouseout', (e) => {
    const tooltip = document.querySelector('.tooltip');
    tooltip.remove();
});
        
svg.addEventListener('click', (e) => {
    const clickedElement = e.target.closest('g');
    if (!clickedElement.classList.contains('nosite')) {
        window.open(clickedElement.getAttribute('site'))
        }
});