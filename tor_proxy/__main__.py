from .tor_proxy import tor_proxy, get_onion_instance
import time
import argparse
import sys
import os

def kill_tor_processes():
    try:
        import psutil
    except ImportError:
        print("psutil not installed. Installing now...")
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'psutil'])
        import psutil
    killed = 0
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['name'] == 'tor' and proc.info['cmdline']:
                cmd = ' '.join(proc.info['cmdline'])
                if '/usr/bin/tor' in cmd and '-f' in cmd and '/tmp/' in cmd:
                    print(f"Killing Tor process PID {proc.info['pid']}: {cmd}")
                    proc.kill()
                    killed += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    if killed == 0:
        print("No matching Tor processes found.")
    else:
        print(f"Killed {killed} Tor process(es).")

def main():
    parser = argparse.ArgumentParser(description="Run Tor proxy service.")
    parser.add_argument('-d','--detach', action='store_true', help='Run as a background (detached) process')
    parser.add_argument('-k','--kill', action='store_true', help='Kill running Tor processes started with /usr/bin/tor -f /tmp/...')
    args = parser.parse_args()

    if args.kill:
        kill_tor_processes()
        sys.exit(0)

    if args.detach:
        port = tor_proxy()
        print(f"Tor SOCKS proxy running on port: {port}")

    else:
        try:
            port = tor_proxy()
            print(f"Tor SOCKS proxy running on port: {port}")
            print("Press Ctrl+C to stop the service")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nShutting down Tor service...")
            onion = get_onion_instance()
            if onion:
                onion.cleanup()
        except Exception as e:
            print(f"Error: {str(e)}")
            onion = get_onion_instance()
            if onion:
                onion.cleanup()

if __name__ == "__main__":
    main()
