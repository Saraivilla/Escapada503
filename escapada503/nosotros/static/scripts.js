document.addEventListener("DOMContentLoaded", function () {
    // Buscar por coincidencia en el buscador
    const searchInputs = document.querySelectorAll('.searchInput');
    searchInputs.forEach(input => {
        input.addEventListener('input', function() {
            searchFunction(this);
        });
    });

    function searchFunction(inputElement) {
        const input = inputElement.value.toLowerCase();

        if (input.length < 2) {
            removeHighlightsFromAll();
            return;
        }

        const contentElements = document.querySelectorAll('.contenido');
        contentElements.forEach(el => {
            removeHighlights(el);
            highlightText(el, input);
        });

        const highlighted = document.querySelector('.highlight');
        if (highlighted) {
            highlighted.scrollIntoView({ behavior: 'smooth' });
        }
    }

    function removeHighlights(element) {
        const innerHTML = element.innerHTML;
        element.innerHTML = innerHTML.replace(/<mark class="highlight">|<\/mark>/g, '');
    }

    function removeHighlightsFromAll() {
        const contentElements = document.querySelectorAll('.contenido');
        contentElements.forEach(el => removeHighlights(el));
    }

    function highlightText(element, text) {
        const nodes = element.childNodes;

        nodes.forEach(node => {
            if (node.nodeType === Node.TEXT_NODE) {
                const regex = new RegExp(text, 'gi');
                const replacedText = node.textContent.replace(regex, match => `<mark class="highlight">${match}</mark>`);
                const span = document.createElement('span');
                span.innerHTML = replacedText;
                node.replaceWith(span);
            } else if (node.nodeType === Node.ELEMENT_NODE) {
                highlightText(node, text);
            }
        });
    }

    // Toggle menu functionality
    function toggleMenu() {
        const menu = document.getElementById('menu_opcionesHeader');
        if (menu) {
            menu.classList.toggle('show');
        }
    }

    // Add event listener to the hamburger menu
    const hamburger = document.querySelector('.hamburger');
    if (hamburger) {
        hamburger.addEventListener('click', toggleMenu);
    }

    // Ensure that plusSlides and currentSlide functions are accessible globally
    window.plusSlides = plusSlides;
    window.currentSlide = currentSlide;

    // Card info functionality
    function showCardInfo(cardIndex) {
        const cardItem = document.getElementsByClassName("card-item")[cardIndex];
        cardItem.classList.toggle("flipped");
    }

    const cardItems = document.getElementsByClassName("card-item");
    Array.from(cardItems).forEach((item, index) => {
        item.addEventListener('click', () => showCardInfo(index));
    });
});

document.getElementById('userInfo').addEventListener('click', function() {
    var userOptions = document.getElementById('userOptions');
    if (userOptions.style.display === 'none' || userOptions.style.display === '') {
        userOptions.style.display = 'block';
    } else {
        userOptions.style.display = 'none';
    }
});
