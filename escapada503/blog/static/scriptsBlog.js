document.addEventListener("DOMContentLoaded", function () {
    var slideIndex = 1;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");

    if (slides.length > 0) {
        showSlides(slideIndex);
    }

    function plusSlides(n) {
        showSlides(slideIndex += n);
    }

    function currentSlide(n) {
        showSlides(slideIndex = n);
    }

    function showSlides(n) {
        var i;
        if (n > slides.length) { slideIndex = 1 }
        if (n < 1) { slideIndex = slides.length }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[slideIndex - 1].style.display = "block";
        if (dots.length > 0) {
            dots[slideIndex - 1].className += " active";
        }
    }

    function showCardInfo(cardIndex) {
        var cardItem = document.getElementsByClassName("card-item")[cardIndex];
        cardItem.classList.toggle("flipped");
    }

    var cardItems = document.getElementsByClassName("card-item");
    for (var i = 0; i < cardItems.length; i++) {
        (function (index) {
            cardItems[index].addEventListener('click', function () {
                showCardInfo(index);
            });
        })(i);
    }

    // Función para alternar el menú
    function toggleMenu() {
        var menu = document.getElementById('menu_opcionesHeader');
        menu.classList.toggle('show');
    }

    // Añadir event listener a la barra de hamburguesa
    const hamburger = document.querySelector('.hamburger');
    if (hamburger) {
        hamburger.addEventListener('click', toggleMenu);
    }

    const wrapper = document.querySelector('.wrapper');
    const indicators = [...document.querySelectorAll('.indicators button')];

    let currentTestimonial = 0; // Default 0

    indicators.forEach((item, i) => {
        item.addEventListener('click', () => {
            indicators[currentTestimonial].classList.remove('active');
            wrapper.style.marginLeft = `-${100 * i}%`;
            item.classList.add('active');
            currentTestimonial = i;
        })
    })

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

    // Función para mostrar/ocultar opciones del usuario
    document.getElementById('userInfo').addEventListener('click', function() {
        var userOptions = document.getElementById('userOptions');
        if (userOptions.style.display === 'none' || userOptions.style.display === '') {
            userOptions.style.display = 'block';
        } else {
            userOptions.style.display = 'none';
        }
    });
});
