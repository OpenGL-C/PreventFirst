import socket
import data_handlerer


def server_program():

    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket() 
    server_socket.bind((host, port))  

    # configure how many client the server can listen simultaneously
    while True:
        server_socket.listen(1)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            print(data)
            if data == "":            
                # if data is not received break
                print("LE")
                break
            elif data[0] == "C": # Cancelling Apointment
                conn.send(data_handlerer.cancel_apointment(data[1:10], data[10:]).encode())  # send data to the client
                break
            elif data[0] == "T": # Taking the upcoming apointments for the user
                conn.send(data_handlerer.get_history(data[1:], 5, "upcomming_scans").encode())  # send data to the client
                


            

        conn.close()  # close the connection


if __name__ == '__main__':
    server_program()