import multiprocessing
import time

def job1(qx):
   a = 1
   b = 1
   for i in range(5):
     a += 1
     b += 1
     result = a+b
     qx.put(result)
     time.sleep(1)
   qx.put(None)


def job2(qx):
    while True:
        value = qx.get()
        if value is None:
            print("ended")
            break
        print(value)

if __name__ == "__main__":
    qx = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=job1, args=(qx, ))
    p2 = multiprocessing.Process(target=job2, args=(qx, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("main ended")
