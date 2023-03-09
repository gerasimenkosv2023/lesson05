from socket import *
import time

# AF_INET - указываем, что сокет является сетевым
# SOCK_STREAM - определет сокет как потоковый
s = socket(AF_INET,SOCK_STREAM) #создали сокет TCP
s.bind(("",8888)) #настроили сокет, чтобы он принимал запросы от клиента по локальному IP и порту
s.listen(5)#Переходим в режим ожидания запросов и допускаем не более 5 запросов одновременно
while True:
    massiv = []
    client,addr = s.accept()#принимаем запрос на соединение
    data = client.recv(1000000)#получаем данные от клиента
    d = data.decode('utf-8')
    msg = "Привет клиент"
    print("Сообщение ",d,' было отправлено',addr)
    massiv.append(d)
    client.send(msg.encode('utf-8'))
    print(massiv)
    client.close()