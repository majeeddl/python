
# Description: This is a simple example of using multiprocessing in Python.
import time
from time import sleep
from multiprocessing import Process, Queue, cpu_count


print('Number of CPU cores: ', cpu_count())


# colors = ['red', 'blue', 'green', 'yellow', 'black', 'white']

# cnt = 1

# queue = Queue()
# print('Queue size: ', queue.qsize())


def task(sleep_time, message):
    sleep(sleep_time)
    print(message)
    # print('Finished sleeping')


if __name__ == '__main__':

    print('Starting main process')

    process = Process(target=task, args=(1.5, "Parameter message from main process"))

    process.start()
    print('Waiting for the process...')
    process.join()

    # while True:

    #     print("end file")
    #     time.sleep(10)
