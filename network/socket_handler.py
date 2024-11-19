import socket
class SocketHandler():
  #initilize server_port attribute
  def __init__(self, server_port =  60000):
    self.server_port  = server_port

  # Estblish TCP connection with given peer
  def establish_tcp_connection(self,peer_ip):
    try:
      with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as tcp_socket:
        tcp_socket.connect((peer_ip,self.server_port))
        print(f"Connected to peer at {peer_ip}")
        tcp_socket.sendall("Hello from peer!".encode())
    except Exception as e:
      print(f"Failed to connect to peer {e}")
    # start TCP server to accept incoming connection
  def start_tcp_server(self):
      with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
        server_socket.bind(("",self.server_port))
        server_socket.listen()
        print("TCP server is listening.....")

        while True:
          client_socket,  client_addr = server_socket.accept()
          print(f"Connected to by {client_addr}")

          self.handle_peer_connection(client_socket)
    #handle communication between peers
  def handle_peer_connection(self,client_socket):
      with client_socket:
        message = client_socket.recv(1024).decode()

        print(f"Recived message : {message}")


