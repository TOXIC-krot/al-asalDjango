document.addEventListener('DOMContentLoaded', function () {
    const updateCartButtons = document.querySelectorAll('.update-cart');

    updateCartButtons.forEach(button => {
        button.addEventListener('click', function () {
            const productId = this.dataset.productId;
            const action = this.dataset.action;

            updateCart(productId, action, this);
        });
    });

    function updateCart(productId, action, buttonElement) {
        const url = '/cart/update/';  // URL to your Django view

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Ensure CSRF token is included
            },
            body: JSON.stringify({
                'product_id': productId,
                'action': action
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Update the UI based on the response data
                const quantitySpan = buttonElement.parentNode.querySelector('#selected-quantity');
                quantitySpan.textContent = data.quantity + ' dona';
                document.getElementById('cart-total-count').innerText = data.total_count;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

const openPopupButton = document.getElementById('open-popup');
const closePopupButton = document.getElementById('close-popup');
const popup = document.getElementById('popup');

openPopupButton.addEventListener('click', () => {
    popup.classList.remove('hidden');
});

closePopupButton.addEventListener('click', () => {
    popup.classList.add('hidden');
});