const urlInput = document.getElementById('url');
const submitButton = document.getElementById('submit');

urlInput.addEventListener('keyup', function(event) {
    if (urlInput.validity.valid) {
        submitButton.disabled = false;
        urlInput.classList.remove('is-danger');
    } else {
        submitButton.disabled = true;
        urlInput.classList.add('is-danger');
    }
});

