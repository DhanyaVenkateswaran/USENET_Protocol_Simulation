import socket
import json

newsgroups = ['SPO', 'POL']
articles = {'SPO': ['1', '2'], 'POL': ['3', '4']}
file = open("sample.txt","r")

artlist=json.loads(file.read())
print("Stats in current server :")
print("No. of newsgroups : ",len(newsgroups))
print("No. of articles : ",len(artlist))
print("Connecting to nearby server for new articles....")

s = socket.socket()
#print("Socket created")
s.connect(('localhost',9997))
print("Connected")
x=s.recv(5000).decode()
#print(x)
y=json.loads(x)
for i in y.keys():
    z=i
    if z not in artlist:
        artlist[z]=y[z]
        if(y[z][:3] not in newsgroups):
            newsgroups.append(y[z][:3])
            articles[y[z][:3]]=[z]
        else:
            if z not in articles[y[z][:3]]:
                articles[y[z][:3]].append(z)


#print(artlist)
#print(newsgroups)
#print(articles)

print("Synchronisation complete\n")
print("Newsgroups and articles updated ")
print("No. of newsgroups : ",len(newsgroups))
print("No. of articles : ",len(artlist))
s.close()

s = socket.socket()
s.bind(('localhost',9998))


s.listen(3)
print('waiting for connections')

c, addr =s.accept()
print("Connected with ", addr)
c.send(bytes('Welcome to UseNet Server \n1) List the groups \n2)Select a group\n3) Select an Article \n4) Post an article ','utf-8'))

while True:

    temp=int(c.recv(1024).decode())

    if(temp==1):
        a=""
        for i in newsgroups:
            a=a+i
            a=a+'\n'
        c.send(bytes(a,'utf-8'))
    elif temp==2:
        c.send(bytes('Enter group name : ','utf-8'))
        reply= c.recv(1024).decode()

        a=""
        for i in articles[reply]:
            a = a + str(i)
            a = a + '\n'
        c.send(bytes(a,'utf-8'))

    elif temp==3:
        c.send(bytes('Enter article no. : ', 'utf-8'))
        reply = c.recv(1024).decode()

        a = artlist[reply]
        c.send(bytes(a, 'utf-8'))

    elif temp==4:
        c.send(bytes('Enter the article in the format "ArticleID_NEWSGROUP_CONTENTS" : ', 'utf-8'))
        reply = c.recv(2000).decode()
        aid=int(reply[0])
        agrp=reply[2:5]
        con=reply[2:]

        artlist[aid]=con
        if agrp in newsgroups:
            articles[agrp].append(aid)
        else:
            newsgroups.append(agrp)
            articles[agrp]=[con]

        c.send(bytes('Article published', 'utf-8'))

        print(artlist)
    elif temp==5:
        break

print("Server closing")

with open("serverjson.txt", "w") as outfile:
    json.dump(artlist, outfile)

c.close()