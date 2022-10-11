# Automate Ping
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020
from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Justin Ellis")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    my_server_ip = "34.209.241.29"
    server=Server(my_server_ip)
    # TODO - Call Ping method and print the results
    print(server.ping())