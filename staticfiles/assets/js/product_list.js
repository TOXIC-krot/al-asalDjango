document.querySelectorAll('.product-card').forEach(card => {
    const quantitySelector = card.querySelector('#quantity-selector');
    const addProductBtn = card.querySelector('#add-product');

    addProductBtn.addEventListener('click', function() {
        addProductBtn.classList.add('hidden');
        quantitySelector.classList.remove('hidden');
    });
});