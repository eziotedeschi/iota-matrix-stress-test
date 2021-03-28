# iota-matrix-stress-test

Basic script for stress testing a Matrix Homeserver implementation for Iota

```shell
pip install -r requirements.txt
```

Create a `.env` file by copying the `.env.example` available.  
Write your Homeserver url in `BASE_URL`.  
Decide how many users you want to create (`USERS_THREADS * USERS_PER_THREAD`).  
Choose a room name to send the messages `ROOM_NAME`.  
Decide how many messages will be send by each user `MESSAGES_PER_USER`.

```shell
python3 create_users.py
python3 create_room.py
python3 send_messages.py
```
