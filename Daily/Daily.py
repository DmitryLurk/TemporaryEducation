#import concurrent.futures
#import random
#import threading
#import time
#
#
#def work(semaphore):
#    time.sleep(random.randint(5, 10))
#    print('releasing')
#    semaphore.release()
#
#
#def connect(semaphore, reached_max_connection):
#    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
#        while True:
#            connection_counter = 0
#            while not reached_max_connection.is_set():
#                print(f'\nConnection n={connection_counter}')
#                semaphore.acquire()
#                connection_counter += 1
#
#                ex.submit(work, semaphore)
#                time.sleep(0.8)
#
#            time.sleep(5)
#
#
#def connections_guard(semaphore, reached_max_connection):
#    while True:
#        print(f'semaphore = {semaphore._value}')
#        time.sleep(1.5)
#
#        if semaphore._value == 0:
#            reached_max_connection.set()
#            print('max connection')
#            time.sleep(2)
#            reached_max_connection.clear()
#
#
#if __name__ == '__main__':
#    max_conection = 10
#    reached_max_connection = threading.Event()
#
#    semaphore = threading.Semaphore(value=max_conection)
#    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#        executor.submit(connections_guard, semaphore, reached_max_connection)
#        executor.submit(connect, semaphore, reached_max_connection)
#

