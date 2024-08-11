window.addEventListener('scroll', function() {
    var iconContainer = document.getElementById('icon-container');
    if (window.scrollY > 0) {
        iconContainer.classList.add('icon-scrolled');
    } else {
        iconContainer.classList.remove('icon-scrolled');
    }
});