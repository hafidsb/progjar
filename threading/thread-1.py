import threading, time, datetime

# Thread handler function 
def fungsi1():
    while True:
        waktu = datetime.datetime.now()
        print("{} Fungsi1 boi".format(waktu))
        time.sleep(4)
    return

def fungsi2():
    while True:
        waktu = datetime.datetime.now()
        print("{} Fungsi2 oof".format(waktu))
        time.sleep(2)
    return

def fungsi3():
    while True:
        waktu = datetime.datetime.now()
        print("{} Fungsi3 nih".format(waktu))
        time.sleep(1)
    return

f1 = threading.Thread(target = fungsi1)
f1.start()

f2 = threading.Thread(target = fungsi2)
f2.start()

f3 = threading.Thread(target = fungsi3)
f3.start()
