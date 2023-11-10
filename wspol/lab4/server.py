import subprocess
import time
import os

FIFO = 'buffer'
DB = {
    "01": {"name": "Maciej", "len": "06"},
    "02": {"name": "Filip", "len": "05"},
    "03": {"name": "Marek!!", "len": "07"}
}

try:
    if not os.path.exists(FIFO):
        subprocess.run(['mkfifo', FIFO])
except FileExistsError:
    pass

fifo_in = os.open(FIFO, os.O_RDONLY | os.O_BINARY)

fifo_out = os.open(FIFO, os.O_WRONLY | os.O_NDELAY | os.O_BINARY)

while True:
    message_len = os.read(fifo_in, 2)
    if len(message_len) > 0:
        message_len = int(message_len)
        db_id = os.read(fifo_in, 2).decode()
        path = os.read(fifo_in, message_len).decode()
        print(message_len, db_id, path)

        response = os.open(path, os.O_WRONLY | os.O_BINARY)
        os.write(response, f'{DB[db_id]["len"]}{DB[db_id]["name"]}'.encode())
        os.close(response)
    time.sleep(5)
