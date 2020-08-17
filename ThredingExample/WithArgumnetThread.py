import threading
import time

start = time.perf_counter()


def do_something_thread(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    print('Done sleeping...')

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something_thread, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} seconds")