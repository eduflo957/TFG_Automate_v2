import multiprocessing

counter = 0

def myProcess():
        global counter
        counter +=1

if __name__ == "__main__":
    subp = multiprocessing.Process(target=myProcess())
    subp.start()
    counter +=1
    subp.join()
    print(counter)

