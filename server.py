import asyncio
import websockets
import json

# Store connected clients and their usernames
USERS = {}
CONNECTED_CLIENTS = {}


async def handle_connection(websocket):
    current_username = None
    try:
        async for message in websocket:
            data = json.loads(message)
            action = data.get("action")

            if action == "register":
                username = data.get("username")
                password = data.get("password")

                if username in USERS:
                    response = {
                        "type": "register",
                        "status": "error",
                        "message": "Username already exists"
                    }
                elif username and password:
                    USERS[username] = password  # In production, use secure password hashing
                    response = {
                        "type": "register",
                        "status": "success",
                        "message": f"User {username} registered successfully"
                    }
                else:
                    response = {
                        "type": "register",
                        "status": "error",
                        "message": "Username or password missing"
                    }
                await websocket.send(json.dumps(response))

            elif action == "login":
                username = data.get("username")
                password = data.get("password")

                if username in USERS and USERS[username] == password:
                    # Store the websocket connection for this user
                    current_username = username
                    CONNECTED_CLIENTS[username] = websocket
                    response = {
                        "type": "login",
                        "status": "success",
                        "message": f"User {username} logged in successfully"
                    }
                else:
                    response = {
                        "type": "login",
                        "status": "error",
                        "message": "Incorrect username or password"
                    }
                await websocket.send(json.dumps(response))

            elif action == "send":
                username = data.get("username")
                message = data.get("message")

                # Broadcast message to all connected clients
                for client_name, client_socket in list(CONNECTED_CLIENTS.items()):
                    try:
                        await client_socket.send(json.dumps({
                            "type": "message",
                            "user": username,
                            "message": message
                        }))
                    except websockets.exceptions.ConnectionClosed:
                        # Remove disconnected client
                        del CONNECTED_CLIENTS[client_name]

            else:
                response = {
                    "type": "error",
                    "message": "Unknown action"
                }
                await websocket.send(json.dumps(response))

    except websockets.exceptions.ConnectionClosed:
        # Remove disconnected client
        if current_username and current_username in CONNECTED_CLIENTS:
            del CONNECTED_CLIENTS[current_username]
        print(f"Connection closed for user {current_username}")


async def main():
    async with websockets.serve(handle_connection, "localhost", 6789):
        print("Chat server started on ws://localhost:6789")
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())