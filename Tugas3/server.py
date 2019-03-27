import sys
import socket
import os
from threading import Thread

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9001)
print >> sys.stderr, 'starting up on %s port %s' %server_address
sock.bind(server_address)

sock.listen(1)
namafile=["Image/bart.png",
          "Image/lisa.jpg",
          "Image/homer.jpg"]

def fungsi(connection):
    #connection = connectiondata[0]
    while True:
        req = connection.recv(32)
        if(req == '1'):
            for nama in namafile:
                connection.send(nama + "\n")
        elif(req == '2'):
            namanya = connection.recv(1024)
            for nama in namafile:
                if (nama == namanya):
                    counter = '1'
                    break
                else :
                    counter = '0'
            connection.send(counter)
            if (counter == '1'):
                connection.send("START {}" . format(namanya))
                ukuran = os.stat(namanya).st_size
                fp = open(namanya,'rb')
                k = fp.read()
                terkirim=0
                for x in k:
                    connection.send(x)
                    terkirim = terkirim + 1
                    print "\r terkirim {} of {} " . format(terkirim,ukuran)
                fp.close()
                connection.send("FINISH")
        elif(req == '3'):
            connection.send("READY")
            while True:
                data = connection.recv(1024)
                if(data[0:5]=="START"):
                    print data[6:]
                    namanya = "Image/" + data[6:]
                    fp = open(namanya,'wb+')
                    ditulis=0
                elif(data=="FINISH"):
                    fp.close()
                elif(data=="ENDING"):
                    break
                else:
                    print "blok ", len(data), data[0:10]
                    fp.write(data)
            namafile.append(namanya)

while True:
    print "waiting for a connection"
    connection, client_address = sock.accept()
    print >> sys.stderr, 'connection from', client_address
    thread = Thread(target=fungsi, args=(connection, ))
    thread.start()

