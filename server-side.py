import socket
import tkinter as tk
import threading

def start_server():
    # Set up UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Define server address and port
    server_address = ('', 9999)

    # Bind the socket to the server address
    udp_socket.bind(server_address)

    status_label.config(text="UDP network discovery server is ready to receive messages...")

    while True:
        # Receive data from client
        data, address = udp_socket.recvfrom(1024)
        message = f"Received message from {address}: {data.decode()}"
        messages_listbox.insert(tk.END, message)

        # Send back a response to the client
        response = f"Server: Hello, client"
        udp_socket.sendto(response.encode(), address)

def start_server_thread():
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

# Create GUI
root = tk.Tk()
root.title("UDP Network Discovery Server")

frame = tk.Frame(root)
frame.pack(padx=150, pady=30)

start_button = tk.Button(frame, text="Start Server", command=start_server_thread)
start_button.pack(side=tk.LEFT)

status_label = tk.Label(frame, text="")
status_label.pack(side=tk.LEFT, padx=50)

messages_label = tk.Label(root, text="Received Messages:")
messages_label.pack()

messages_listbox = tk.Listbox(root, width=100, height=30)
messages_listbox.pack()

root.mainloop()
