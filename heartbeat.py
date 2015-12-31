import sys
import socket
import datetime
try:
    import requests
except ImportError:
    sys.exit("python requests not installed. run 'sudo easy_install install requests'")
try:
    from firebase import firebase
except ImportError:
    sys.exit("python-firebase not installed. run 'sudo easy_install install python-firebase'")
try:
    config = __import__('config')
except ImportError:
    sys.exit("Config file not found")


def main():
    print config.firebase
    auth = firebase.FirebaseAuthentication(
        config.firebase['token'], config.firebase['email']
        )
    hb = firebase.FirebaseApplication(config.firebase['url'], auth)
    output = {"last_update": {".sv": "timestamp"}}
    # get local ip
    output['local_ip'] = get_local_ip()
    # get local date and time
    output['local_datetime'] = datetime.datetime.now()
    try:
        r = requests.get('http://myexternalip.com/raw')
        output['global_ip'] = r.text
    except requests.exceptions.RequestException as e:
        message = e
    print output
    hb.put('/', config.firebase['machine_name'], output)


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


if __name__ == "__main__":
    main()
