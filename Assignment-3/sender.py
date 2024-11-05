import zmq

context = zmq.Context()


socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:5555")

print("Sender: Sending a message...")
try:
    message = "This is a message from CS361"
    socket.send_string(message)
    print(f"Sender: Sent '{message}'")
except KeyboardInterrupt:
    print("Sender: Stopped sending messages.")
finally:
    socket.close()
    context.term()
