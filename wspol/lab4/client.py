import sys
import os
import errno

def main() -> None:
    if len(sys.argv) != 3:
        print("format zapytania: client.py <client_name> <requested_person_id>")
        sys.exit(1)
    client_name = sys.argv[1]
    requested_person_id = sys.argv[2]
    client_input_fifo_path = f"{client_name}"
    try:
        os.mkfifo(client_input_fifo_path)
    except OSError as oe:
        if oe.errno != errno.EEXIST:
            raise

    raw_request = f"{requested_person_id} {client_input_fifo_path}\n"
    print("Zapytania jest wysyłane..")
    SERVER_INPUT_FIFO_PATH = "server-fifo"
    server_input_fifo = open(SERVER_INPUT_FIFO_PATH, "w")
    server_input_fifo.write(raw_request)
    server_input_fifo.close()

    print("Oczekiwanie odpowiedzi od serwera...")
    
    client_input_fifo = open(client_input_fifo_path, "r")
    raw_response = client_input_fifo.read()
    client_input_fifo.close()
    os.remove(client_input_fifo_path)

    response = raw_response.strip()
    print(response)

if __name__ == "__main__":
    main()