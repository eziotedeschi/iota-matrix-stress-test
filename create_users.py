import uuid
import json
import threading

from dotenv import dotenv_values
from matrix_client.client import MatrixClient


users = []


def create_users(thread_id):
    global users
    config = dotenv_values()

    for i in range(int(config["USERS_PER_THREAD"])):
        client = MatrixClient(config["BASE_URL"])
        print(f"[{thread_id}] - Creating user {i}")
        args = {
            "username": f"username_{uuid.uuid1()}",
            "password": "somestrongpassword",
        }
        token = client.register_with_password(**args)
        users.append({**args, "token": token})


def main():
    config = dotenv_values()

    threads = []
    for thread_id in range(int(config["USERS_THREADS"])):
        args = (thread_id,)
        thread = threading.Thread(target=create_users, args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    with open("users.json", "w") as file:
        output = {"users": users}
        output = json.dumps(output, indent=3)
        file.write(output)


if __name__ == "__main__":
    main()