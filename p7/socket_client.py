import json
import time
from threading import Thread
from django.conf import settings
import socketio
from django.db import connection


class SocketClient:
    socket = socketio.Client(ssl_verify=False, reconnection=False)
    MAX_THREAD = settings.SOCKET_MAX_THREAD
    msg_threads = []

    @staticmethod
    @socket.on("receive")
    def _receive(data):
        data = json.loads(data)
        if data.get("type") == "status":
            if data.get("text") == "valid":
                print("authenticated")
        else:
            print("invalid credential")
            SocketClient.socket.disconnect()

    @classmethod
    def send(cls, data):
        wait = True
        while wait:
            msg_thread = cls.get_threads(data)
            if msg_thread:
                msg_thread.start()
                wait = False
            else:
                time.sleep(0.1)

    @classmethod
    def get_threads(cls, data):
        if len(cls.msg_threads) < cls.MAX_THREAD:
            msg_thrd= Thread(target=cls._send, args=(data,))
            cls.msg_threads.append(msg_thrd)
            return msg_thrd
        else:
            for msg_thrd in cls.msg_threads:
                if not msg_thrd.is_alive():
                    msg_thrd = Thread(target=cls._send, args=(data,))
                    return msg_thrd


    @classmethod
    def _send(cls, data):
        if not cls.socket.connected:
            cls.socket.connect(settings.SOCKET_BASE_URL + "?server_token=" + settings.SOCKET_SERVER_TOKEN)
        if cls.socket.connected:
            msg = json.dumps(data)
            cls.socket.emit('send', msg)

        try:
            connection.close()
        except:
            print('connection not found')