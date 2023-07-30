from ReadFile import ReadFile
from Buxmoney import Buxmoney
from Payup import Payup
import time
import undetected_chromedriver as uc
from threading import Thread, Barrier
import concurrent.futures

if __name__ == '__main__':
    timeWaitElement = 60
    data = ReadFile()
    username = data['username']
    password = data['password']
    apikey = data['apikey']
    buxusername = data['buxusername']
    buxpassword = data['buxpassword']
    numero_multitareas = 2
    barrier = Barrier(numero_multitareas)
    # creating thread
    t1 = Thread(target=Buxmoney(apikey=apikey,
                                buxusername=buxusername, buxpassword=buxpassword), args=(barrier,))
    t2 = Thread(target=Payup(
        username=username, password=password, apikey=apikey), args=(barrier,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")
