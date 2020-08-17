import concurrent.futures
import time

start = time.perf_counter()


def do_something_thread(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping..{seconds} '


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]  # list of seconds which will be passed as argument to our function

    # results = [executor.submit(do_something_thread, sec) for sec in secs]
    # # We will be using here another method known as as_completed() whose sole responsibility is to give us an iterator
    # # which yields the results of the threads as they completed
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    # f1 = executor.submit(do_something_thread, 1)
    # Submit method set a function to be executed and returns a future object
    # future object helps us check the state of the function by encapsulating the function in background with the help
    # of 'result'

    # print(f1.result())

    # when we use submit method it returns a future object, but when we use map function it returns the
    # results directly.
    results = executor.map(do_something_thread, secs)
    for result in results:
        print(result)
    # The map function also runs the threads efficiently when other thread is sleeping but it shows up the
    # results in the manner they started execution. 

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds")
