import socket
#Define the host as a tuple
HOST, PORT = "", 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen(True)

print("Serving HTTP on port %s...." %PORT)

while True:
    client_connection, client_address = s.accept()
    request = client_connection.recv(1024) #Buffer Size
    print(request.decode("utf-8")) #Display the HTTP request
    #Define the Web response message

    http_reponse = "HTTP/1.1 200 OK \n\n"\
                   "<html>"\
                   "<head>" \
                   "<title>Team Yarichin</title>"\
                   "</head>"\
                   "<body>"\
                   "<p>"\
                   "Welcome to our website"\
                   "</p>"\
                   "<img src='https://steamuserimages-a.akamaihd.net/ugc/1772697886352337698/C84B5AFF15DA669ECDF5DAEDA7006159975560CE/'>" \
                   "<table>"\
                   "<tr>"\
                   "<th>First Name</th>" \
                   "<th>Last Name</th>" \
                   "<th>CCA</th>" \
                   "</tr>"\
                   "<tr>"\
                   "<td>Eden</td>" \
                   "<td>Fok</td>" \
                   "<td>Volleyball</td>" \
                   "</tr>" \
                   "<tr>" \
                   "<td>Jun An</td>" \
                   "<td>Lim</td>" \
                   "<td>Swimming</td>" \
                   "</tr>" \
                   "<tr>" \
                   "<td>Joshua</td>" \
                   "<td>Kok</td>" \
                   "<td>Dating</td>" \
                   "</tr>" \
                   "</table>"\
                   "</html>"\

    client_connection.sendall(bytes(http_reponse, "utf-8"))
    client_connection.close()


