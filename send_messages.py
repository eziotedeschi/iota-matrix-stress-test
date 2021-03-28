import uuid
import json
import threading

from dotenv import dotenv_values
from matrix_client.api import MatrixHttpApi


def send_messages(thread_id, user):
    config = dotenv_values()

    with open("room.json") as file:
        room = json.load(file)

    for i in range(int(config["MESSAGES_PER_USER"])):
        print(f"[{thread_id}] - Sending a message ({i})")
        message = str(uuid.uuid1())
        matrix = MatrixHttpApi(config["BASE_URL"], token=user["token"])
        matrix.join_room(room["room_alias"])
        matrix.send_message(room["room_id"], message)


def main():
    with open("users.json") as file:
        users = json.load(file)["users"]

    threads = []
    for thread_id, user in enumerate(users):
        args = (thread_id, user)
        thread = threading.Thread(target=send_messages, args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":

    main()
