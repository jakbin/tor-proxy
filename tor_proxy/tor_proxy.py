from .onion import *
from .onionstart import OnionStart
import sys

# Global onion instance for cleanup
_onion_instance = None

def get_onion_instance():
    return _onion_instance

def tor_proxy():
    global _onion_instance
    # Start the Onion object
    onion = Onion()
    _onion_instance = onion
    try:
        onion.connect()
    except (TorTooOld, TorErrorInvalidSetting, TorErrorAutomatic, TorErrorSocketPort, TorErrorSocketFile, TorErrorMissingPassword, TorErrorUnreadableCookieFile, TorErrorAuthError, TorErrorProtocolError, BundledTorNotSupported, BundledTorTimeout) as e:
        _onion_instance = None
        sys.exit(e.args[0])
    except KeyboardInterrupt:
        print("\nShutting down...")
        if onion:
            onion.cleanup()
        _onion_instance = None
        sys.exit()

    # Start the onionshare app
    try:
        app_tor = OnionStart(onion)
        app_tor.start_onion_service()
        proxy_port = app_tor.get_tor_socks_port()
    except KeyboardInterrupt:
        print("\nShutting down...")
        if onion:
            onion.cleanup()
        _onion_instance = None
        sys.exit()

    return proxy_port[1]
