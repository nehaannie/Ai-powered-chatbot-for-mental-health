$(document).ready(function() {
    // Event listener for the form submission
    $(".msger-inputarea").on("submit", function(e) {
        e.preventDefault(); // Prevent the form from refreshing the page

        var userText = $("#textInput").val(); // Get the text input by the user
        if (userText === "") {
            return; // If the input is empty, do nothing
        }

        // Display user's message in the chat
        appendMessage("User", "right", userText);

        // Clear the input field
        $("#textInput").val("");

        // Send the user's message to the Flask backend
        $.get("/get", { msg: userText }).done(function(response) {
            // Display the bot's response in the chat
            appendMessage("Bot", "left", response);
        }).fail(function() {
            // Handle error if the request fails
            appendMessage("Bot", "left", "Error: Unable to get response. Please try again later.");
        });
    });

    // Function to append a message to the chat
    function appendMessage(name, side, text) {
        const msgHTML = `
            <div class="msg ${side}-msg">
                <div class="msg-img" style="background-image: url('https://image.flaticon.com/icons/svg/327/327779.svg')"></div>
                <div class="msg-bubble">
                    <div class="msg-info">
                        <div class="msg-info-name">${name}</div>
                    </div>
                    <div class="msg-text">${text}</div>
                </div>
            </div>
            
        `;

        $(".msger-chat").append(msgHTML);
        $(".msger-chat").scrollTop($(".msger-chat")[0].scrollHeight); // Scroll to the bottom
    }
    
    
});
