document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');

    form.addEventListener('submit', function(event) {
        let isValid = true;

        document.querySelectorAll('.form_input').forEach(function(input){
            if (!input.checkValidity()) {
                input.classList.add('form_input-error');
                isValid = false;
            } else {
                input.classList.remove('form_input-error');
            }
        });

        document.querySelectorAll('.form_select input').forEach(function(input){
            const group = input.name;
            const inputs = document.querySelectorAll(`input[name="${group}"]`);
            const anyChecked = Array.from(inputs).some(i => i.checked);

            if (!anyChecked) {
                inputs.forEach(i => i.classList.add('form_input-error'));
                isValid = false;
            } else {
                inputs.forEach(i => i.classList.remove('form_input-error'));
            }
        });

        if (!isValid) {
            event.preventDefault();
        }
    });

    document.querySelectorAll('.form_input').forEach(function(input){
        input.addEventListener('input', function() {
            if (input.checkValidity()) {
                input.classList.remove('form_input-error');
            }
        });
    });

    document.querySelectorAll('.form_select input').forEach(function(input){
        input.addEventListener('change', function() {
            const group = input.name;
            const inputs = document.querySelectorAll(`input[name="${group}"]`);
            const anyChecked = Array.from(inputs).some(i => i.checked);

            if (anyChecked) {
                inputs.forEach(i => i.classList.remove('form_input-error'));
            }
        });
    });
});
