from __future__ import annotations
import os
import errno
import time
import signal
import sys
import select

def sigusr1Handler(signum, frame):
    print("Server jest wyłączany")
    sys.exit(0)

# keep running the server even after closing the terminal
def sighupHandler(signum, frame):
    print("Serwer nadal działa, pomimo otrzymania SIGHUP")

def sigtermHandler(signum, frame):
    print("Serwer nadal działa, pomimo otrzymania SIGTERM")

signal.signal(signal.SIGUSR1, sigusr1Handler)
signal.signal(signal.SIGHUP, sighupHandler)
signal.signal(signal.SIGTERM, sigtermHandler)

def main() -> None:
    SERVER_INPUT_FIFO_PATH = "server-fifo"
 
    people = {
        "1": "Marek",
        "2": "Krzysztof",
        "3": "Karol",
        "4": "Maciej",
    }

    try:
        os.mkfifo(SERVER_INPUT_FIFO_PATH)
    except OSError as oe:
        if oe.errno != errno.EEXIST:
            raise

    print("Serwer jest aktywny i oczekuję zapytań")
    server_input_fifo = open(SERVER_INPUT_FIFO_PATH, "r")

    while True:
        rlist, _, _ = select.select([server_input_fifo], [], [])
        raw_request = server_input_fifo.readline()
        if not raw_request:
            continue
        raw_request_split = raw_request.strip().split(" ")
        if len(raw_request_split) != 2:
            print("Invalid request")
            continue
        [person_id, client_input_fifo_path] = raw_request_split
        print(f"Zapytanie od {client_input_fifo_path} o osobe z id {person_id}")

        try:
            client_input_fifo = open(client_input_fifo_path, "w")
            try:
                person = people.get(person_id, "nie znaleziono osoby")
                client_input_fifo.write(f"{person}\n")
            finally:
                client_input_fifo.close()
        except FileNotFoundError:
            print("fifo klienta nie znalezione")

if __name__ == "__main__":
    main()
