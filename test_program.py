import time
import zmq
import io
import base64
from PIL import Image

context = zmq.Context()

# Connect to microservice.
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# JSON file for testing.
json_data = '{ "name":"John", "age":30, "city":"New York"}'

sample_json_string = '''{
    "labels": {
        "title": "Math Progress",
        "x-axis": "Date",
        "y-axis": "DCPM"
    },
    "x-axis-data": [
        "10/1",
        "10/8",
        "10/15"
    ],
    "y-axis-data": [
        "13",
        "16",
        "15"
    ]
}'''

# Keep client running for demo purposes.
while True:

    input("Press any key to send a JSON string containing graph data to the microservice.")

    # Send microservice JSON file.
    socket.send_json(sample_json_string)

    # Wait for reply.
    message = socket.recv()

    print("Received reply from microservice.")
    time.sleep(1.5)
    print("...")

    # Title: ZeroMQ pyzmq send jpeg image over tcp
    # Source: https://stackoverflow.com/questions/24791633/zeromq-pyzmq-send-jpeg-image-over-tcp
    # convert data form Base64 to byte,
    graph_image_bytes = bytearray(base64.b64decode(message))

    # Store bytes in the IO buffer, assign to image variable, and show image
    io_image_buffer = io.BytesIO(graph_image_bytes)

    # Title: Python Pillow Tutorial
    # Source: https://www.geeksforgeeks.org/python-pillow-tutorial/
    # Open image from buffer, save to variable, and show image.
    image = Image.open(io_image_buffer)
    image.show()


