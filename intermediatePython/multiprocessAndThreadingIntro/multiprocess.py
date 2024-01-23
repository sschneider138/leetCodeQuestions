import time
from multiprocessing import Process
import os


def squareNums():
    for i in range(100):
        i * i
        time.sleep(0.1)


if __name__ == '__main__':
    processes = []
    numProcesses = os.cpu_count()

    for i in range(numProcesses):
        p = Process(target=squareNums)
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("End main")
