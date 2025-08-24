import multiprocessing
import time

def job1():
    for i in range(5):
        print("Hello1")
        time.sleep(0.01)

def job2():
    for i in range(5):
        print("Hello2")
        time.sleep(0.01)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=job1)
    p2 = multiprocessing.Process(target=job2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("ended")
