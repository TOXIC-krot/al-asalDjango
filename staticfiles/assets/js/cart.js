/*
document.addEventListener('DOMContentLoaded', function() {
    var now = new Date();
    var dateTimeString = now.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    }) + ', ' + now.toLocaleTimeString('en-US', {
        hour: '2-digit',
        minute: '2-digit'
    });
    document.getElementById('datetime').innerText = dateTimeString;
});
*/

document.addEventListener('DOMContentLoaded', function() {
    var openPopupButton = document.getElementById('open-popup');
    var popup = document.getElementById('popup');

    openPopupButton.addEventListener('click', function() {
        popup.classList.toggle('hidden');
    });

    window.addEventListener('click', function(event) {
        if (event.target === popup) {
            popup.classList.add('hidden');
        }
    });
});

document.getElementById("closeButton").addEventListener("click", function() {
    document.getElementById("popup").classList.add("hidden");
});

document.getElementById("clearButton").addEventListener('click', function() {
    const url = '/cart/clear/';  // URL to your Django view

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Ensure CSRF token is included
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // remove items from ui
            document.getElementById("items-list").innerHTML = '';
            document.getElementById("total-price").innerText = '0 UZS';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });

    document.getElementById("popup").classList.add("hidden");
});

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