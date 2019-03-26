from threading import Thread
import socket
import os

TARGET_IP = "127.0.0.1"
TARGET_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((TARGET_IP, TARGET_PORT))
namafile=["bart.png", "maggie.jpg", "lisa.jpg", "homer.jpg"]

def sendImage(CLIENT_IP, CLIENT_PORT):
   addr = CLIENT_IP, CLIENT_PORT
   sock.sendto("SENDING" , (addr))
   for nama in namafile:
      sock.sendto("START {}" . format(nama) , (addr))
      ukuran = os.stat(nama).st_size
      fp = open(nama,'rb')
      k = fp.read()
      terkirim=0
      for x in k:
         sock.sendto(x, (addr))
         terkirim = terkirim + 1
         print "\r terkirim {} of {} " . format(terkirim,ukuran)
      sock.sendto("FINISH", (addr))
      fp.close()
   sock.sendto("ENDING", (addr))


while True:
   print "Waiting..."
   data, addr = sock.recvfrom(1024)
   if(data=="READY"):
      thread = Thread(target=sendImage, args=(addr))
      thread.start()
      

