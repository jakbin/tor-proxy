from .onion import *
from .onionstart import OnionStart
import sys

def tor_proxy():
    # Start the Onion object
    onion = Onion()
    try:
        onion.connect()
    except (TorTooOld, TorErrorInvalidSetting, TorErrorAutomatic, TorErrorSocketPort, TorErrorSocketFile, TorErrorMissingPassword, TorErrorUnreadableCookieFile, TorErrorAuthError, TorErrorProtocolError, BundledTorNotSupported, BundledTorTimeout) as e:
        sys.exit(e.args[0])
    except KeyboardInterrupt:
        print("")
        sys.exit()

    # Start the onionshare app
    try:
        app_tor = OnionStart(onion)
        # app_tor.set_stealth(stealth)
        app_tor.start_onion_service()
        proxy_port = app_tor.get_tor_socks_port()
    except KeyboardInterrupt:
        print("")
        sys.exit()

    return proxy_port[1]
