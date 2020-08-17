import time


start = time.perf_counter()


def do_something():
    print('Sleeping for 1 second...')
    time.sleep(1)
    print('Done sleeping...')


for _ in range(10):
    do_something()

finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} seconds")
