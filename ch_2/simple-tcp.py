import socket

target_host = "0.0.0.0"
target_port = 9999

# create a socket object
# AF_INET - we are going to use a standard IPv4 address or hostname
# SOCK_STREAM - this will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send(b"Ping")

# receive some data
response = client.recv(4096)

print(response)

# In the above code snippet, we are making some serious assumptions about
# sockets. The first assumption is that our connection will always succeed,
# and the second is that the server is always expecting us to send data
# first (as opposed to servers that expect to send data to you first and
# await your response). Our third assumption is that the server will always
# send us data back in a timely fashion. We make these assumptions largely
# for simplicity’s sake.
