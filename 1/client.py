from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))
msg = 'Привет сервер!'
s.send(msg.encode('UTF-8'))
answer = s.recv(1000000)
print("Сообщение от сервера", answer.decode('utf-8'), 'длиной', len(answer), 'байт')
a = input("введите число a")
s.send(a.encode('UTF-8'))
b = input("введите число b")
s.send(b.encode('UTF-8'))
c = input("введите операцию * / + -")
s.send(c.encode('UTF-8'))
s.close()