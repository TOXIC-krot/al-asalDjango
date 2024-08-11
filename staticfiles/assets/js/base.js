function formatNumber(number) {
    return number.replace(/\B(?=(\d{3})+(?!\d))/g, '\u202F'); // \u2009 is the Unicode thin space
}

document.addEventListener('DOMContentLoaded', function() {
    var priceElements = document.querySelectorAll('[data-value-type="price"]');
    priceElements.forEach(element => {
        element.textContent = formatNumber(element.textContent);
    });
});

$(document).ready(function() {
    $(".owl-carousel").owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        dots: false,
        responsive: {
            0: {
                items: 3
            },
            600: {
                items: 3
            },
            1000: {
                items: 3
            }
        }
    });
});