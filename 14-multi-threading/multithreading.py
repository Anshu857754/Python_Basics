import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"numbers{i}")

def print_letters():
    for letters in "abcde":
        time.sleep(2)
        print(f"letters:{letters}")


# creating a two thread 
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()
# starrt the thread
t1.start()
t2.start()

# wait for thread to complete 
t1.join()
t2.join()
print_numbers()
print_letters()
finished_time=time.time()-t
print(finished_time)