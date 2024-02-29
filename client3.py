import socket
import tkinter as tk

def send_broadcast():
    # Set up UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Define server address and port
    server_address = ('<broadcast>', 9999)

    # Broadcast presence on the network
    message = "Hello server, I am Client 3!"
    udp_socket.sendto(message.encode(), server_address)

    # Receive response from server
    response, _ = udp_socket.recvfrom(1024)
    received_response_label.config(text="Received response from server: " + response.decode() + " 3")

    # Close the socket
    udp_socket.close()

# Create GUI
root = tk.Tk()
root.title("UDP Client 3")

frame = tk.Frame(root)
frame.pack(padx=120, pady=30)

broadcast_button = tk.Button(frame, text="Send Broadcast", command=send_broadcast)
broadcast_button.pack()

received_response_label = tk.Label(root, text="")
received_response_label.pack()

root.mainloop()
