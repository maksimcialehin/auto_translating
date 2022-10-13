import socket
from googletrans import Translator
from main import translate_text


translator = Translator()
server_lang = 'be'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1529))
server.listen(4)

client, address = server.accept()

while True:
    message = client.recv(1024).decode()
    lang = message[1:message.index(']')]
    translation = translate_text(
        text=message[message.index(']') + 1:],
        src=lang,
        dest=server_lang
    )
    print(translation)

