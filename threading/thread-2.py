import threading, time, datetime

# Thread class
def worker(number):
    while True:
        time = datetime.datetime.now()
        print("{} worker number-{} \n".format(time, number))
    
    return

threads = []
for i in range(4):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)

for thr in threads:
    thr.start()