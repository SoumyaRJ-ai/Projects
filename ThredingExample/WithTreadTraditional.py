# How Traditional threading works
import threading
import time


start = time.perf_counter()


def do_something_thread():
    print('Sleeping for 1 second...')
    time.sleep(1)
    print('Done sleeping...')

# For the number of threads to run first you need to start them and store them inside a list and then start
# looping over the list to join them So that they will finish working with the threads first before moving to
# other functions
threads = []
for _ in range(10):
    t = threading.Thread(target=do_something_thread)
    t.start()
    threads.append(t)
    # t.join() # If we will keep join() here then there will be no use of threading

for thread in threads:
    thread.join()

# t1 = threading.Thread(target=do_something_thread)
# t2 = threading.Thread(target=do_something_thread)
# t1.start()
# t2.start() # If we run this without the join() it will start the function, sleep for 1 second, by that time
# # the control will move out of the function and run the next print statement. TO make it run the function
# # completely and then move out of the function we need to use join function as below
# t1.join()
#
# t2.join()
finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} seconds")