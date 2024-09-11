document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll('.save-presidium-button');
    


    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const memberId = button.getAttribute('data-id');
    
            const name = document.getElementById(`name-${memberId}`).innerHTML.trim();
            const description = document.getElementById(`description-${memberId}`).innerHTML.trim();

            fetch(updateTextPresidumUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrfToken
                },
                body: new URLSearchParams({
                    'id': memberId,
                    'name': name,
                    'description': description,
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