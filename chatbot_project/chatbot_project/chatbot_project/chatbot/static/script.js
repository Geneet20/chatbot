async function sendMessage() {
    const inputField = document.getElementById("input");
    const message = inputField.value;
    const messageSection = document.getElementById("message-section");

    if (message.trim() === "") return;

    // Display user's message
    const userMessageDiv = document.createElement("div");
    userMessageDiv.className = "message";
    userMessageDiv.id = "user";
    userMessageDiv.innerHTML = `<span id="user-response">${message}</span>`;
    messageSection.appendChild(userMessageDiv);

    // Clear the input field
    inputField.value = "";

    // Send message to the server
    const response = await fetch('/chatbot/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message }),
    });

    const data = await response.json();
    const botMessageDiv = document.createElement("div");
    botMessageDiv.className = "message";
    botMessageDiv.id = "bot";
    botMessageDiv.innerHTML = `<span id="bot-response">${data.bot_response || data.error}</span>`;
    messageSection.appendChild(botMessageDiv);

    // Scroll to the bottom of the message section
    messageSection.scrollTop = messageSection.scrollHeight;
}
