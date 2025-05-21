import os
from dotenv import load_dotenv
from ltm.notifier import TelegramNotifier

def reply_chatid() -> None:
    load_dotenv()
    
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Создайте файл .env и добавьте TELEGRAM_BOT_TOKEN")
        return

    notifier = TelegramNotifier(token)
    
    try:
        chat_id = notifier.get_chat_id()
        print(f"ChatID: {chat_id}")
        notifier.send_message(chat_id, f"Ваш ChatID: {chat_id}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    reply_chatid()