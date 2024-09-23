import multiprocessing
from main import start
from engine.features import hotword

# To run Jarvis
def startJarvis():
    # Code for process 1
    print("Process 1 is running.")
    start()
    
# To run hotword
def listenHotword():
    # Code for process 2
    print("Process 2 is running.")
    hotword()

# Start both processes
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=startJarvis)
    p2 = multiprocessing.Process(target=listenHotword)
    p1.start()
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("System stop")
