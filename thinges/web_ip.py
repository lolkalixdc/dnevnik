import socket
host = input("Enter the websites address: ")
print(list( map( lambda x: x[4][0], socket.getaddrinfo('www.example.com.',22,type=socket.SOCK_STREAM))))
input("Press enter to contine..")