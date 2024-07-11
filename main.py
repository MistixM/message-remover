# Import all necessary libraries to work with Telegram API 
from telethon import TelegramClient
from colorama import Fore
from config import API_ID, API_HASH, PHONE_NUM

# Initialize client (create session and insert API_ID and HASH provided here: https://my.telegram.org/apps)
client = TelegramClient("msgrem", API_ID, API_HASH)

async def main():

    # Open the client    
    await client.start(phone=PHONE_NUM)

    # Store all chats in the variable
    chats = client.iter_dialogs()

    # Iterate through the all chats 
    async for chat in chats:
        print(f"{Fore.GREEN}>{Fore.WHITE} Deleting chat: {chat.name}, with ID: {chat.id}")

        # Delete each dialog for everyone
        try:
            await client.delete_dialog(chat.id, revoke=True)
        
        # If something went wrong notice to user and continue iteration
        except Exception as e:
            print(f"{Fore.RED}>{Fore.WHITE} Failed to delete chat: {chat.name}. Detailed error: {e}")
            pass
    
    # Notice if everything is okay
    print(f"{Fore.GREEN}>{Fore.WHITE} You're all set!")

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())