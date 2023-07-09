
const room_id=JSON.parse(document.getElementById('room_id').textContent)
const message_sender=JSON.parse(document.getElementById('sender').textContent)

let url = `ws://${window.location.host}/ws/socket-server/${room_id}`
console.log(url)
const chatsocket = new WebSocket(url)

chatsocket.onmessage = function (e) {
    console.log("on messaging")
    let data = JSON.parse(e.data)
    console.log(data)
    if (data.type == 'chat_message') {
        let message = document.getElementById('chat-messages')
        message.insertAdjacentHTML('beforeend',
            `<p>${data.message_content}</p>`
        )
    }
}

let form = document.getElementById('chat-input')
form.addEventListener('submit', (e) => {
    e.preventDefault()
    let message = e.target.message.value
    chatsocket.send(JSON.stringify(
        { 'message': message,
           'message_sender':message_sender,
        }
    ))
    console.log(message)
    form.reset()
}
)


