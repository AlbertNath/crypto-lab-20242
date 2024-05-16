import asyncio
from websocket_connector import WebsocketConnector

async def main():
    ip_address = '192.168.1.242'
    port='1463'
    wb = WebsocketConnector(ip_address=ip_address, port=port)

    command = 'start'
    await wb.send_command(command)
    
    while True:
        response = await wb.receive_output()
        if "?" in response:
            user_input = input()
            await wb.send_command(user_input)
        if "exit" in response:
            break
            
    while True:
        user_input = input()
        await wb.send_command(user_input)
        if user_input == "exit":
            break
        #while input() != "exit":
        #    pass
            
    response = await wb.receive_output()
    await wb.close_connection() 

if __name__ == "__main__":
    asyncio.run(main())
