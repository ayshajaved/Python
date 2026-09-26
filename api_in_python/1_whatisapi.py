'''
Application programming interface
application is any software that has a specific purpose, interface is the protocol that decides that how two
applications can contract between eachother
What is an API?
An API (Application Programming Interface) is a set of rules and protocols that allows one software application to interact with another.
It defines the methods and data formats that applications can use to communicate with each other, simplifying the development of software 
and enabling different systems to work together.
api is the communicator between server and application, application requests the data through api and server responses through
the api
api types:
GETapi: Retrieve data from a server.
POST: Send data to a server to create a resource.
PUT: Update an existing resource on a server., update the complete table in the databse
PATCH: also update but a single column
DELETE: Remove a resource from a server.
api hit: when api is hit, the responce is generated through the status code that tells us whether the request is successful or not
Response is may be in two formats:-JSON/XML
JSON: {"name" : "ayesha"}
xml: extensible markup language: in the form of angular brackets <name> "ayesha"</name>
APi is hit by Considering some protocols , like http, https and urls that ensures that APIs can communicate effectively and efficiently. 
APIs (Application Programming Interfaces) can be categorized based on their architecture, usage, and communication style. Here’s a detailed breakdown of the main types of APIs along with examples in Python.

1. Web APIs
Web APIs are accessed over the web using the HTTP/HTTPS protocol. They allow applications to interact with web services. Web APIs can be further divided into REST and SOAP APIs.

REST (Representational State Transfer)
Key Features:

Stateless: Each request from a client to a server must contain all the information the server needs to fulfill that request.
Resource-Based: Resources (such as data objects) are identified by URLs.
HTTP Methods: Uses standard HTTP methods such as GET, POST, PUT, DELETE.
Format: Typically uses JSON for data interchange, but can also use XML, HTML, or plain text.
Example: Using a REST API in Python
'''
# import requests

# # URL of the API endpoint
# url = "https://jsonplaceholder.typicode.com/posts/1"

# # Send a GET request to the API
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()
#     print(data)
# else:
#     print(f"Failed to retrieve data: {response.status_code}")

'''Advantages:

Simple to use and understand.
Flexible with different data formats.
Scalable and stateless nature.
Disadvantages:

Less standardized compared to SOAP.
Might require custom handling for transactions and security.
SOAP (Simple Object Access Protocol)
Key Features:

Protocol: A protocol for exchanging structured information in web services.
Format: Uses XML exclusively to format messages.
Transport: Can use multiple transport protocols like HTTP, SMTP, TCP, etc.
Standardization: Highly standardized with strict rules.
Example: Using a SOAP API in Python
'''
# from zeep import Client

# # Example of a different WSDL URL
# wsdl = "https://www.w3schools.com/xml/tempconvert.asmx?WSDL"

# try:
#     client = Client(wsdl)
#     response = client.service.CelsiusToFahrenheit(100)
#     print(response)
# except ConnectionError as e:
#     print(f"Connection error: {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")


'''Advantages:

High security with WS-Security.
Built-in error handling.
Suitable for enterprise-level applications.
Disadvantages:

More complex and verbose.
Slower due to the XML format.
Requires more bandwidth.
2. Library APIs
Library APIs allow software libraries to interact with each other. These are typically used within a single application or across applications running on the same system.

Example: Using the os library in Python

python
Copy code
import os

# Get the current working directory
current_directory = os.getcwd()
print(current_directory)

# Join paths
path = os.path.join(current_directory, 'subdir', 'file.txt')
print(path)
Example: Using the json library in Python

python
Copy code
import json

# JSON data
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON data
data = json.loads(json_data)
print(data)

# Convert dictionary to JSON
json_string = json.dumps(data, indent=4)
print(json_string)
3. Operating System APIs
Operating System APIs allow applications to interact with the underlying operating system.

Example: Using the subprocess library in Python

python
Copy code
import subprocess

# Run a command and capture its output
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

# Print the output
print(result.stdout)
Example: Using the shutil library in Python

python
Copy code
import shutil

# Copy a file
shutil.copy('source.txt', 'destination.txt')

# Remove a directory
shutil.rmtree('directory_to_remove')
4. Remote APIs
Remote APIs enable interaction between applications on different devices or systems over a network. This includes protocols like RPC and gRPC.

RPC (Remote Procedure Call)
RPC allows a program to execute a procedure on a remote server.

Example: Using XML-RPC in Python

python
Copy code
import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

# Call a remote procedure
result = proxy.add(2, 3)
print(result)
gRPC (gRPC Remote Procedure Call)
gRPC is a high-performance RPC framework that uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features such as authentication, load balancing, and more.

Example: Using gRPC in Python

To use gRPC, you'll need to define your service in a .proto file and then generate the Python code from it. Below is a simplified example.

Define the service in a .proto file:
proto
Copy code
syntax = "proto3";

service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}
Generate Python code from the .proto file:
sh
Copy code
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. greeter.proto
Implement the server and client in Python:
Server:

python
Copy code
import grpc
from concurrent import futures
import greeter_pb2
import greeter_pb2_grpc

class Greeter(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greeter_pb2.HelloReply(message='Hello, {}'.format(request.name))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
Client:

python
Copy code
import grpc
import greeter_pb2
import greeter_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(greeter_pb2.HelloRequest(name='World'))
    print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()

'''

