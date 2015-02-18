from socket import *
import ssl
import base64

msg = '\r\n I love computer networks!'
endmsg = '\r\n.\r\n'
# Choose a mail server (e.g. Google mail server) 
# and call it mailserver
mailserver = 'smtp.gmail.com'
mailport = 25
# Create socket called clientSocket and establish 
# a TCP connection with mailserver
#Fill in start

def received(recv):
	print("her er recv")
	print(recv)
	print(recv[:3])
	if (recv[:3] != '250'):
		print '250 reply not received from server.'

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailport))
print("clientSocket made and sexed up")

#Fill in end
recv = clientSocket.recv(1024)
print(recv[:3])
if (recv[:3] != '220'):
	print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode('utf-8'))
recv1 = clientSocket.recv(1024)
received(recv1)

#STARTTLS
command = 'STARTTLS\r\n'
clientSocket.send(command)
recv = clientSocket.recv(1024)
print(recv[:3])
if (recv[:3] != '220'):
	print '220 reply not received from server.'

#SSC
scc = ssl.wrap_socket(clientSocket, 
	ssl_version=ssl.PROTOCOL_SSLv23)
scc.send('auth login\r\n')

scc.send(base64.b64encode('johanloudon@gmail.com\r\n'))
scc.send(base64.b64encode('hannah3RKUL\r\n'))

# Send MAIL FROM command and print server response.
# Fill in start

mailfrom = 'MAIL FROM: <johanloudon@gmail.com>\r\n'
clientSocket.sendall(mailfrom.encode('utf-8'))
recvMF = clientSocket.recv(1024)
received(recvMF)

# Fill in end

# Send RCPT TO command and print server response.
# Fill in start

rcptTO = 'RCPT TO: <johanloudon@gmail.com>\r\n'
clientSocket.sendall(rcptTO.encode('utf-8'))
recv = clientSocket.recv(1024)
received(recv)

# Fill in end

# Send DATA command and print server response.
# Fill in start

dc = 'Data'
print(dc)
clientSocket.send(dc.encode('utf-8'))
recv = clientSocket.recv(1024)
received(recv)

# Fill in end

# Send message data.
# Fill in start

message = raw_input('Enter message: ')

# Fill in end
# Message ends with a single period.
# Fill in start

mailMessageEnd = '\r\n.\r\n'
message = message + mailMessageEnd
clientSocket.send(message.encode('utf-8'))
recv = clientSocket.recv(1024)
received(recv)

# Fill in end

# Send QUIT command and get server response.
# Fill in start

quit = 'Quit\r\n'
print(quit)
clientSocket(quit.encode('utf-8'))
recv = clientSocket(1024)
received(recv)

# Fill in end