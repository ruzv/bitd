import multiprocessing
import os

def info(title):
    print(title)
    print(__name__)
    print(os.getppid())
    print(os.getpid())


def f(name):
    info("func f")
    print(name)

if __name__ == "__main__":
    info("main")
    p = multiprocessing.Process(target=f, args=['bob'])
    p.start()
    p.join()