import socket

client = socket.socket()
client.connect(("localhost", 9999))

print("Connected to server")

while True:
    a = input("Enter first number: ")
    op = input("Enter operation (+, -, *, /): ")
    b = input("Enter second number: ")

    message = a + " " + op + " " + b

    client.send(message.encode())

    result = client.recv(1024).decode()

    print("Result:", result)

    choice = input("Continue? (yes/no): ")

    if choice.lower() == "no":
        client.send("exit".encode())
        break

client.close()