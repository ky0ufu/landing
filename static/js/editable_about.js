document.addEventListener("DOMContentLoaded", function() {
    const saveButtons = document.querySelectorAll('.save-council-button');


    saveButtons.forEach(button => {
        button.addEventListener('click', function() {
            const councilId = button.getAttribute('data-id');
            
            const councilName = document.getElementById(`council-name-${councilId}`).innerHTML.trim();

            const chairpersonName = document.getElementById(`chairperson-name-${councilId}`).innerHTML.trim();
            const chairpersonDescription = document.getElementById(`chairperson-description-${councilId}`).innerHTML.trim();
            
            fetch(updateTextAboutUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrfToken
                },
                body: new URLSearchParams({
                    'council_id': councilId,
                    'council_name': councilName,
                    'chairperson_name': chairpersonName,
                    'chairperson_description': chairpersonDescription
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Изменения успешно сохранены');
                } else {
                    alert('Ошибка сохранения изменений: ' + data.error);
                }
            })
            .catch(error => {
                alert('Ошибка отправки данных: ' + error);
            });
        });
    });
});