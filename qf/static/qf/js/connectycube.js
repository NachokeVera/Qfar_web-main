document.addEventListener("DOMContentLoaded", function() {
    const CREDENTIALS = {
        appId: 7678,
        authKey: "7Jz5LusMpV2Ugb2",
        authSecret: "uZVVgk3kAVmMraV",
    };

    const DEFAULT_CONFIG = {
        debug: { mode: 1 },
        chat: {
            streamManagement: {
                enable: true,
            }
        }
    };

    ConnectyCube.init(CREDENTIALS, DEFAULT_CONFIG);

    var token = document.getElementById("token").value;
    var opponentId  = document.getElementById("idQui").value;
    var dialogId = document.getElementById("dialogId").value;

    console.log(token);
    console.log(opponentId);
    console.log(dialogId);

    ConnectyCube.chat.connect({
        userId: opponentId,
        password: token
    }).then(() => {
        console.log("Conectado!");
    }).catch((error) => {
        console.log("Error: ", error);
    });

    /* ConnectyCube.chat.onSentMessageCallback = function (messageLost, messageSent) {
        console.log("[ConnectyCube.chat.onSentMessageCallback] callback:", messageLost, messageSent);
    }; */
    
    ConnectyCube.chat.onDeliveredStatusListener = function (messageId, dialogId, userId) {
        console.log("[ConnectyCube.chat.onDeliveredStatusListener] callback:", messageId, dialogId, userId);
    };

    ConnectyCube.chat.onSentMessageCallback = function (messageLost, messageSent) 
    {
        console.log("[ConnectyCube.chat.onSentMessageCallback] callback:", messageLost,"messagesentttt:", messageSent);
    };

    const formChat = document.getElementById("form_chat");

    formChat.addEventListener("submit", function(event) {
        event.preventDefault();
        const messageInput = document.getElementById("messageId");
        const messageText = messageInput.value;

        console.log("Form submit event triggered");
        console.log("Message: ", messageText);
        console.log("Dialog ID: ", dialogId);

        if (messageText && dialogId) {
            sendMessage(dialogId, messageText);
        } else {
            console.error("Message or Dialog ID is missing");
        }
    });

    function sendMessage(dialogId, messageText) {
        const messageParams = {
            type: 'groupchat',
            body: messageText,
            extension: {
              save_to_history: 1,
              dialog_id: dialogId
            },
            markable: 1
        };
        console.log("MessageParams: ", messageParams);

        const messageId = ConnectyCube.chat.send(opponentId, messageParams);
        
        console.log("Message ID: ", messageId);
        addMessageToTable(messageParams);
    }

    function addMessageToTable(message) {
        const chatTableBody = document.getElementById('chatBodyId');
        const row = document.createElement('tr');
        const timeCell = document.createElement('td');

        const currentDate = new Date();
        const hours = currentDate.getHours();
        const minutes = currentDate.getMinutes();
        const formattedHours = hours.toString().padStart(2, '0');
        const formattedMinutes = minutes.toString().padStart(2, '0');

        timeCell.style.width = '10px';
        timeCell.textContent = `${formattedHours}:${formattedMinutes}`;

        const senderCell = document.createElement('td');
        senderCell.style.width = '50px';
        senderCell.textContent = opponentId;

        const messageCell = document.createElement('td');
        messageCell.textContent = message.body;

        row.appendChild(timeCell);
        row.appendChild(senderCell);
        row.appendChild(messageCell);
        chatTableBody.appendChild(row);
    }

   /* function loadMessages(dialogId) {
        const params = { chat_dialog_id: dialogId, sort_desc: 'date_sent', limit: 50 };

        ConnectyCube.chat.message
            .list(params)
            .then((result) => {
                console.log("Messages: ", result);
                updateChatTable(result.items);
            })
            .catch((error) => {
                console.error("Message retrieval error: ", error);
            });
    }

    function updateChatTable(messages) {
        const chatTableBody = document.getElementById("chatBodyId");
        chatTableBody.innerHTML = ''; // limpia los chats de la tabla
        messages.forEach((message) => {
            const row = document.createElement('tr');
            const timeCell = document.createElement('td');
            timeCell.style.width = '10px';
            timeCell.textContent = new Date(message.date_sent * 1000).toLocaleTimeString();

            const senderCell = document.createElement('td');
            senderCell.style.width = '50px';
            senderCell.textContent = message.sender_id;

            const messageCell = document.createElement('td');
            messageCell.textContent = message.message;

            row.appendChild(timeCell);
            row.appendChild(senderCell);
            row.appendChild(messageCell);
            chatTableBody.appendChild(row);
        });
    }  */
});
