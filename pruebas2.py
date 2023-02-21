import multiprocessing

counter = 0

def myProcess():
    global counter
    counter = 2

if __name__ == "__main__":
    subp = multiprocessing.Process(target=myProcess)
    counter +=5
    print(counter , "counter antes de proceso")
    subp.start()
    myProcess()
    subp.join()
    print(counter , "counter después de proceso")