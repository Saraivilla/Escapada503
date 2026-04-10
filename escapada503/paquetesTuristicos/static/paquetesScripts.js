document.addEventListener("DOMContentLoaded", function () {
    // Funcionalidad del menú hamburguesa
    function toggleMenu() {
        const menu = document.getElementById('menu_opcionesHeader');
        if (menu) {
            menu.classList.toggle('show');
        }
    }

    // Añadir el evento de clic al menú hamburguesa
    const hamburger = document.querySelector('.hamburger');
    if (hamburger) {
        hamburger.addEventListener('click', toggleMenu);
    }

    // Funcionalidad del overlay de reserva
    const openOverlayBtns = document.querySelectorAll('.reservaAhoraBtn');
    const overlay = document.getElementById('overlay');
    const closeOverlayBtn = document.getElementById('closeOverlayBtn');
    const nombreLugarInput = document.getElementById('nombreLugar');
    const paqueteIdInput = document.getElementById('paqueteId');
    const paquetePrecioInput = document.getElementById('precioLugar');
    const cantidadPersonasInput = document.getElementById('cantidadPersonas');
    const totalInput = document.getElementById('total');

    openOverlayBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Obtener el nombre y el ID del paquete desde los atributos data del botón clicado
            const nombreLugar = btn.getAttribute('data-nombre');
            const paqueteId = btn.getAttribute('data-id');
            const precioLugar = btn.getAttribute('data-precio');

            // Mostrar el overlay
            overlay.style.display = 'block';

            // Actualizar los campos del formulario
            if (nombreLugarInput) {
                nombreLugarInput.value = nombreLugar;
            }
            if (paqueteIdInput) {
                paqueteIdInput.value = paqueteId;
            }
            if (paquetePrecioInput) {
                paquetePrecioInput.value = precioLugar;
            }
        });
    });

    closeOverlayBtn.addEventListener('click', () => {
        overlay.style.display = 'none';
    });

    window.addEventListener('click', (event) => {
        if (event.target === overlay) {
            overlay.style.display = 'none';
        }
    });

    // Actualizar el total cuando cambia la cantidad de personas
    if (cantidadPersonasInput) {
        cantidadPersonasInput.addEventListener('input', () => {
            const cantidad = cantidadPersonasInput.value;
            const precio = parseFloat(paquetePrecioInput.value);
            const total = cantidad * precio;
            totalInput.value = total.toFixed(2); // Formatear el total a dos decimales
        });
    }

    // Buscar por coincidencia en el buscador
    const searchInputs = document.querySelectorAll('.searchInput');
    searchInputs.forEach(input => {
        input.addEventListener('input', function () {
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

    // Funcionalidad de tarjetas informativas
    function showCardInfo(cardIndex) {
        const cardItem = document.getElementsByClassName("card-item")[cardIndex];
        cardItem.classList.toggle("flipped");
    }

    const cardItems = document.getElementsByClassName("card-item");
    Array.from(cardItems).forEach((item, index) => {
        item.addEventListener('click', () => showCardInfo(index));
    });

    // Funcionalidad del menú de usuario
    document.getElementById('userInfo').addEventListener('click', function () {
        var userOptions = document.getElementById('userOptions');
        if (userOptions.style.display === 'none' || userOptions.style.display === '') {
            userOptions.style.display = 'block';
        } else {
            userOptions.style.display = 'none';
        }
    });

    // Exponer las funciones de slideshow globalmente
    window.plusSlides = plusSlides;
    window.currentSlide = currentSlide;
});
