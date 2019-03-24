import threading, time, datetime

class Worker(threading.Thread):
    def __init__(self,nomor):
        self.nomor = nomor
        threading.Thread.__init__(self)
        self.daemon=True

    def run(self):
        while True:
           waktu = datetime.datetime.now()  
           print "{} saya worker nomor {}" . format(waktu,self.nomor)
           time.sleep(1)

def main():
    worker1 = Worker(1)
    worker2 = Worker(2)
    worker3 = Worker(3)
    worker4 = Worker(4)
    
    worker1.start()
    worker2.start()
    worker3.start()
    worker4.start()

if __name__ == "__main__":
    try: 
      main()
      while True:
        pass
    except KeyboardInterrupt:
      print "Program Stop .." 