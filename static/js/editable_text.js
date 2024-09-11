document.addEventListener("DOMContentLoaded", function() {
    const saveButton = document.getElementById('save-button');
    const editableText = document.getElementById('editable-text');



    if (saveButton && editableText) {
        saveButton.addEventListener('click', function() {
            const content = editableText.innerHTML;

            const key = saveButton.getAttribute('data-key');



            fetch(updateTextUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrfToken
                },
                body: new URLSearchParams({
                    'key': key,
                    'content': content
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Текст успешно обновлен');
                } else {
                    alert('Ошибка обновления текста: ' + data.error);
                }
            })
            .catch(error => {
                alert('Ошибка отправки данных: ' + error);
            });
        });
    }
});