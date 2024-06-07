/*!
* Start Bootstrap - Landing Page v6.0.6 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
function toggleDescription(id) {
    let desc = document.getElementById('desc-' + id);
    let btn = document.getElementById('toggle-btn-' + id);
    if (desc.classList.contains('truncate')) {
        desc.classList.remove('truncate');
        btn.textContent = 'Leer menos';
    } else {
        desc.classList.add('truncate');
        btn.textContent = 'Leer más';
    }
}