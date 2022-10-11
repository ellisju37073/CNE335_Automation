import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        result = os.system("ping -n 3 %s" % self.server_ip) #https://stackoverflow.com/questions/48468135/baccess-denied-option-c-requires-administrative-privileges
        return result