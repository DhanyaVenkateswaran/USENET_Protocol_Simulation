import socket

newsgroups = ['BUS', 'POL']
tnewsgroups = newsgroups[:]
articles = {'BUS': ['art5', 'art6'], 'POL': ['art3', 'art4']}
file = open("server2json.txt","r")
artlist=file.read()


s2 = socket.socket()
print("Socket created")
s2.bind(('localhost',9997))

s2.listen(3)
print('waiting for connections')

c, addr =s2.accept()
print("Connected with ", addr)

c.send(bytes(artlist,'utf-8'))

