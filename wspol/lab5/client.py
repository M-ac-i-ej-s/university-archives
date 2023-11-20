import os
import random
import multiprocessing

def client_process(serverq, clientq, wocabulary):
    pid = os.getpid()
    for i in range(3):
        to_send = random.choice(wocabulary)
        serverq.put((to_send.encode(), pid))
        m, t = clientq.get()
        m = m.decode()
        print(f"{to_send}: {m}")

if __name__ == "__main__":
    server_key = 123
    client_key = 321
    pid = os.getpid()

    wocabulary = ["dog", "cat", "fish", "lion", "python", "js", "html", "css"]

    serverq = multiprocessing.Queue()
    clientq = multiprocessing.Queue()

    input("Press enter to start...")

    client_process_instance = multiprocessing.Process(target=client_process, args=(serverq, clientq, wocabulary))
    client_process_instance.start()

    for i in range(3):
        to_send = random.choice(wocabulary)
        serverq.put((to_send.encode(), pid))
        m, t = clientq.get()
        m = m.decode()
        print(f"{to_send}: {m}")

    client_process_instance.join()
