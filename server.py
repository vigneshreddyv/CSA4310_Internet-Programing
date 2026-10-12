import socket

server = socket.socket()
server.bind(("localhost", 9999))
server.listen(1)

print("Server is waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

while True:
    operation = conn.recv(1024).decode()

    if operation == "exit":
        break

    a, op, b = operation.split()
    a = float(a)
    b = float(b)

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b
    else:
        result = "Invalid operation"

    conn.send(str(result).encode())

conn.close()
server.close()