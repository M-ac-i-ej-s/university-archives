import signal
import sys
import time
from multiprocessing import Process, Queue

def handler(signum, serverq, clientq):
    print(' Inna obsługa  sygnału ', signum)
    print("Server stop")
    serverq.put(None)  # Signal to stop the server process
    serverq.join()  # Wait for the server process to finish
    sys.exit(0)

def server_process(serverq, clientq):
    dictionary = {
        "dog": "pies",
        "cat": "kot",
        "fish": "ryba",
        "lion": "lew",
        "python": "pyton"
    }

    print("Server start")

    for i in range(3):
        m, pid = serverq.get()
        if m is None:
            break  # Stop the server if signaled
        m = m.decode()
        response = dictionary.get(m, "Nie znam takiego słowa")
        clientq.put((response.encode(), pid))
        time.sleep(2)

    print("Server stop")

if __name__ == "__main__":
    serverq = Queue()
    clientq = Queue()

    custom_signal = getattr(signal, 'SIGUSR1', 15)  # 15 is the number for SIGTERM if SIGUSR1 is not available
    signal.signal(custom_signal, lambda signum, frame: handler(signum, serverq, clientq))

    server_process_instance = Process(target=server_process, args=(serverq, clientq))
    server_process_instance.start()

    for i in range(3):
        serverq.put(("cat".encode(), 123))  # Simulating incoming messages

    serverq.put(None)  # Signal to stop the server process
    server_process_instance.join()  # Wait for the server process to finish
