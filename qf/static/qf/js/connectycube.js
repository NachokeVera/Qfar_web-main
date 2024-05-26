document.addEventListener("DOMContentLoaded", function() {
    //esto quizas este mal, tengo que correr esto cuando se crea el chat
    const CREDENTIALS = {
        appId: 7678,
        authKey: "7Jz5LusMpV2Ugb2",
        authSecret: "uZVVgk3kAVmMraV",
    };
    
    const DEFAULT_CONFIG = {
        debug: { mode: 1 }
    };
    
    ConnectyCube.init(CREDENTIALS, DEFAULT_CONFIG);

    var token = document.getElementById("token").value;
    var userIdQui = document.getElementById("idQui").value;
    var dialogId = document.getElementById("dialogId").value;

    console.log(token);
    console.log(userIdQui);
    console.log(dialogId);
  
    ConnectyCube.chat.connect({
        userId: userIdQui,
        password: token
    }).then((result) => {
        console.log("Conectado!: ", result);
        //loadMessages(dialogId);
    }).catch((error) => {
        console.log("error: ", error);
    });

    ConnectyCube.chat.onMessageListener = onMessage;
    ConnectyCube.chat.onSentMessageCallback = (messageLost, messageSent) => {
        if (messageLost) {
            console.error('Mensaje perdido:', messageLost);
        }
        console.log('Mensaje enviado:', messageSent);
    };

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


    const formChat = document.getElementById("form_chat");

    formChat.addEventListener("submit", function(event) {
        event.preventDefault();
        const messageInput = document.getElementById("messageId");
        const messageText = messageInput.value;

        console.log("Form submit event triggered"); // Verifica que el evento se dispare
        console.log("Message: ", messageText); // Verifica el valor del mensaje
        console.log("Dialog ID: ", dialogId); // Verifica el valor de dialogId

        if (messageText && dialogId) {
            sendMessage(dialogId, messageText);
        } else {
            console.error("Message or Dialog ID is missing");
        }
    });

    function sendMessage(dialogId, messageText) {
        const messageParams = {
            type: 'chat', //3
            body: messageText,
            extension: {
              save_to_history: 1,
              dialog_id: dialogId
            },
            markable: 1
        };

        const opponentId = userIdQui;
        console.log("MessageParams: ", messageParams);
        messageParams.id = ConnectyCube.chat.send(opponentId, messageParams);

        console.log("Message ID: ", messageParams.id);
        addMessageToTable(messageParams);
    }

    function addMessageToTable(message) {
        const chatTableBody = document.getElementById('chatBodyId');
        const row = document.createElement('tr');
        const timeCell = document.createElement('td');

        const currentDate = new Date(); // Crea un objeto Date con la fecha y hora actual
        const hours = currentDate.getHours(); // Obtiene la hora actual
        const minutes = currentDate.getMinutes(); // Obtiene los minutos actuales

        // Formatea la hora y los minutos con un cero a la izquierda si es necesario
        const formattedHours = hours.toString().padStart(2, '0');
        const formattedMinutes = minutes.toString().padStart(2, '0');

        timeCell.style.width = '10px';
        timeCell.textContent = `${formattedHours}:${formattedMinutes}`;

        const senderCell = document.createElement('td');
        senderCell.style.width = '50px';
        senderCell.textContent = userIdQui;

        const messageCell = document.createElement('td');
        messageCell.textContent = message.body;

        row.appendChild(timeCell);
        row.appendChild(senderCell);
        row.appendChild(messageCell);
        chatTableBody.appendChild(row);
    }

    function onMessage(userId, message) {
        console.log('[ConnectyCube.chat.onMessageListener] callback:', userId, message);
        addMessageToTable(message);
    }
});
