"use strict"

// When the window loads, add the 'event listener' that allows for sending messages with 'Enter'
window.onload = function() {
        document.getElementById("user-input").addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
};

// The function called when the user clicks the "Send" button or presses "Enter"
// Should 'send' the message and obtain a response from the bot.
async function sendMessage() {
    // Get the user input field
    const input = document.getElementById("user-input");
    
    // Get the message and trim whitespace
    const message = input.value.trim();

    if (message) {
        // Display the user's message in the chat window
        addMessage("You", message);
        // Clear the input field
        input.value = "";

        // Bot responds
        // TODO!!!
    }
}

// The function to add a message to the chat window. 'sender' is either "You" or "Bot", and 'text' is the message content.
function addMessage(sender, text) {
    const chatWindow = document.getElementById("chat-messages");
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", sender.toLowerCase());
    messageElement.textContent = `${sender}: ${text}`;
    chatWindow.appendChild(messageElement);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}