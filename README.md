# VM Management Bot

## Overview
The **VM Management Bot** is a project designed to manage computers and virtual machines through commands sent via a Telegram bot. It aims to facilitate remote management by providing insights and executing tasks on connected machines.

## Project Structure
The project is divided into four key modules:

### 1. `server.py`
- **Purpose**: Acts as the central server for handling connections.
- **Functionality**:
  - Uses sockets for network communication.
  - Implements threads to allocate each new connection.
  - Will interpret Telegram commands (not implemented yet).
  - Forwards messages to the appropriate machine and sends the response back to the Telegram chat.

### 2. `bot.py`
- **Purpose**: Handles interaction with the Telegram bot.
- **Functionality**:
  - Sends messages and checks for updates.
  - Acts as the interface between the user and the server.

### 3. `settings.py` (Not Implemented Yet)
- **Purpose**: Reads a YAML configuration file.
- **Functionality**:
  - Imports settings such as IP address, port, and other server configurations.

### 4. `client.py` (Not Implemented Yet)
- **Purpose**: Functions as a persistent agent running on the target machine.
- **Functionality**:
  - Continuously attempts to connect to the server.
  - Receives commands from the server, executes them, and returns the results.

## Telegram Bot Commands
### Currently Implemented:
- `/?`, `/help`, `/start`: Displays the list of available commands.

### Not Implemented Yet:
- `/serverstatus`: Sends information about the server's current status.

### Planned Commands:
- `/getprocess:client`: Retrieves the list of running processes on the client.
- `/getcpu:client`: Checks the current CPU usage on the client.
- `/getram`: Checks the current RAM usage on the client.
- `/getstorage`: Checks the current storage usage on the client.

## Future Goals
- Fully implement all four modules.
- Enable secure communication between the server and clients.
- Add logging and error handling for better debugging.
- Develop an automated deployment system for clients.
