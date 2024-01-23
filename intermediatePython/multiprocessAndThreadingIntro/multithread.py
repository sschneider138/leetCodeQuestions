import time
from threading import Thread


def squareNums():
    for i in range(100):
        i * i
        time.sleep(0.1)


if __name__ == '__main__':
    threads = []
    numThreads = 10

    for i in range(numThreads):
        t = Thread(target=squareNums)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("End main")
