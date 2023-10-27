import os
import random
import time
import sys

def child(sleep_time):
    pid = os.getpid()
    ppid = os.getppid()
    print(f"Child[{pid}]: I am started. My PID {pid}. Parent PID {ppid}.")

    time.sleep(sleep_time)

    print(f"Child[{pid}]: I am ended. PID {pid}. Parent PID {ppid}.")
    os._exit(random.randint(0, 1))


def parent(n, s):
    pid = os.getpid()

    for _ in range(n):
        child_pid = os.fork()
        if child_pid == 0:
            child(s)
        else:
            print(f"Parent[{pid}]: I ran children process with PID {child_pid}.")

    while True:
        child_pid, status = os.wait()
        print(f"Parent[{pid}]: Child with PID {child_pid} terminated. Exit Status {status}.")

        if status != 0:
            child_pid = os.fork()
            if child_pid == 0:
                child(s)
            else:
                print(f"Parent[{pid}]: I ran additional children process with PID {child_pid}.")
        else:
            break


if __name__ == "__main__":
    num_children = int(sys.argv[1])
    sleep_time = int(sys.argv[2])
    print(num_children, sleep_time)
    parent(num_children, sleep_time)