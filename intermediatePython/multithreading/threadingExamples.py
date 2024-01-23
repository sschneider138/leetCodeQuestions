import time
from threading import Thread, Lock

dbVal = 0


def increase(lock):
    global dbVal

    with lock:
        localCopy = dbVal
        localCopy += 1
        time.sleep(0.1)
        dbVal = localCopy


if __name__ == '__main__':
    lock = Lock()
    print(f'start value {dbVal}')

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'end value {dbVal}')

    print("End main")
