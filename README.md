Local WebSocket Chat is a simple chat application built for learning purposes. It demonstrates how to implement real-time communication using WebSockets in a local environment. The application allows multiple users on the same device to register, log in, and send messages to each other in real-time.

Purpose
The primary goal of this project is educational. It helps you understand:

How WebSockets enable real-time communication between a client and a server.
Basic implementation of user registration and login systems.
Handling of multiple client connections on the server side.
Broadcasting messages to all connected clients.
Features
User Registration: Users can create an account with a unique username and password.
User Login: Registered users can log in to the chat application.
Real-time Messaging: Logged-in users can send and receive messages instantly.
Local Environment: The application runs entirely on a single device, making it easy to set up and experiment with.
How It Works
WebSocket Server: The server is built using Python and the websockets library. It listens for connections on ws://localhost:6789 and handles user registration, login, and message broadcasting.

Client Interface: The frontend is an HTML file with embedded JavaScript. It provides a simple user interface for registration, login, and chatting.

Communication Flow:

Registration: The client sends a registration request to the server with a username and password.
Login: The client sends a login request. Upon successful authentication, the user can access the chat room.
Messaging: Users can send messages, which are sent to the server and then broadcast to all connected clients.
Disconnect: Users can disconnect from the chat, and the server will handle the disconnection.

Run python server.py and navigate to navigate to index.html in the folder and open in a browser.
