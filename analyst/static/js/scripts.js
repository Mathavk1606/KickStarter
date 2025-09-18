document.addEventListener('DOMContentLoaded', () => {
    const chatItems = document.querySelectorAll('.cursor-pointer');
    chatItems.forEach(item => {
        item.addEventListener('click', () => {
            alert('Chat clicked: ' + item.querySelector('p').textContent);
            // Add logic to load chat details
        });
    });
});
