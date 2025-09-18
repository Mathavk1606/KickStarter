document.addEventListener('DOMContentLoaded', () => {
    // --- Chat History Active State ---
    const chatItems = document.querySelectorAll('.chat-item');

    chatItems.forEach(item => {
        item.addEventListener('click', () => {
            // Remove 'active' class from all other items
            chatItems.forEach(i => i.classList.remove('active'));
            
            // Add 'active' class to the clicked item
            item.classList.add('active');
            
            // Here you would typically fetch and display the content for the clicked chat.
            // For example:
            // const chatId = item.dataset.chatId;
            // loadChatContent(chatId);
            console.log('Switched to chat:', item.querySelector('p').textContent.trim());
        });
    });

    // --- Custom File Upload Handling ---
    const fileInput = document.getElementById('file-upload');
    const fileNameDisplay = document.getElementById('file-name');

    if (fileInput) {
        fileInput.addEventListener('change', () => {
            if (fileInput.files.length > 0) {
                fileNameDisplay.textContent = `File selected: ${fileInput.files[0].name}`;
            } else {
                fileNameDisplay.textContent = '';
            }
        });
    }
});

// Example function to load chat content (to be implemented)
function loadChatContent(chatId) {
    console.log(`Fetching content for chat ID: ${chatId}`);
    // Use fetch() to get data from your Django backend
    // and update the main content area.
}
