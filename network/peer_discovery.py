import socket
import time
import threading
from network.socket_handler import SocketHandler

class  PeerDiscovery():
  def __init__(self,broadcast_port = 50000, discovery_handler = 5  ):
    self.broadcast_port =  broadcast_port
    self.discovery_handler =  discovery_handler
    self.socket_handler =  SocketHandler()
  def broadcast_presence(self):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP) as udp_socket:
        udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
        message = "Peer Discovery : I'm here".encode()

        while True:
          udp_socket.sendto(message,('<broadcast>',self.broadcast_port))
          print("Broadcasting Presence...")
          time.sleep(self.discovery_handler)

  def listen_for_broadcast(self):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket :
      udp_socket.bind(("", self.broadcast_port))
      print("Listening for broadcast...")

      while True:
        data,addr = udp_socket.recvfrom(1024)
        print(f"Recieved broadcast from {addr}: {data.decode()}")

        self.socket_handler.establish_tcp_connection(addr[0])

  def start(self):

    broadcast_thread = threading.Thread(target= self.broadcast_presence, daemon= True)
    listen_thread =  threading.Thread(target= self.listen_for_broadcast, daemon= True)
    broadcast_thread.start()
    listen_thread.start()


