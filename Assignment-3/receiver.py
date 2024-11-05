import zmq

context = zmq.Context()

socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:5555")

print("Receiver: Listening for messages...")
try:
    while True:
        message = socket.recv_string()
        print(f"Receiver: Received '{message}'")
except KeyboardInterrupt:
    print("Receiver: Stopped receiving messages.")
finally:
    socket.close()
    context.term()
