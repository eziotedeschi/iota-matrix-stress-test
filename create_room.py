import json

from dotenv import dotenv_values
from matrix_client.api import MatrixHttpApi

if __name__ == "__main__":
    config = dotenv_values()

    with open("users.json") as file:
        user = json.load(file)["users"][0]

    matrix = MatrixHttpApi(config["BASE_URL"], token=user["token"])
    output = matrix.create_room(config["ROOM_NAME"], is_public=True)

    with open("room.json", "w") as file:
        output = json.dumps(output, indent=3)
        file.write(output)

    print("> Room created")
