import asyncio
import logging
import time

from websockets import connect

class WebsocketConnector:
    def __init__(self, ip_address, port):
        """
        This class is used to create an instance of WebSockerConnector, which can be used to connect to a remote machine
        and then execute commands on remote machine.

        :param str ip_address: the remote machine's ip_address.
        :param str port: the port number on which websocket is running on server machine.
        """
        self.ip_address = ip_address
        self.URL = f"ws://{self.ip_address}:{port}"
        self.conn = None
        self.loop = asyncio.get_event_loop()

    def get_connection(self):
        conn = None
        retry_count = 10
        while conn is None and retry_count > 0:
            try:
                logging.debug(f"Establishing connection with {self.URL}")
                conn = connect(self.URL)
            except Exception as ex:
                logging.warning(f"Failed to establish connection.. retrying again after 1 min. {ex}")
                time.sleep(60)
                conn = None
                retry_count -= 1

        if conn is None:
            logging.error(f"Failed to establish connection with {self.URL}")

        return conn

    async def close_connection(self):
        if self.conn:
            await self.conn.close()

    async def send_command(self, command):
        try:
            if self.conn is None:
                #logging.debug(f"Connection object is None. creating connection with {self.URL}")
                self.conn = await self.get_connection()
            await self.conn.send(command)
        except Exception as ex:
            logging.warning(f"Failed to send command {command}")
    
    async def receive_output(self):
        try:
            if self.conn is None:
                self.conn = await self.get_connection()
            #while True:
            output = await self.conn.recv()
            print(output)
            return output
            
        except Exception as ex:
            logging.warning(f"Failed to receive output: {ex}")
