import os, shutil

from . import common

class OnionStart(object):
    """
    OnionShare is the main application class. Pass in options and run
    start_onion_service and it will do the magic.
    """
    def __init__(self, onion, local_only=False, stay_open=False):

        # The Onion object
        self.onion = onion

        self.hidserv_dir = None
        self.onion_host = None
        self.stealth = None
        self.local_only = local_only

    def start_onion_service(self):
        """
        Start the onionshare onion service.
        """

        # Choose a random port
        self.port = common.get_available_port(17600, 17650)

        if self.local_only:
            self.onion_host = '127.0.0.1:{0:d}'.format(self.port)
            return

        self.onion_host = self.onion.start_onion_service(self.port)

        if self.stealth:
            self.auth_string = self.onion.auth_string

    def get_tor_socks_port(self):
        self.socks_port = self.onion.get_tor_socks_port()
        return self.socks_port

    def tor_data_dir(self):
        """
        Get the Tor data directory.
        """
        # print(type(self.onion.tor_data_directory))
        return self.onion.tor_data_directory.name
    
    def tor_torrc_path(self):
        """
        Get the path to the torrc file.
        """
        return self.onion.tor_torrc

    def tor_control_socket(self):
        """
        Get the path to the Tor control socket.
        """
        return self.onion.tor_control_socket