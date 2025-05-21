import requests
from typing import Dict

class TelegramNotifier:
    URL = "https://api.telegram.org/bot{token}/{method}"

    def __init__(self, token: str):
        self.token = token

    def _make_request(self, method: str, params: Dict = None) -> Dict:
        url = self.URL.format(token=self.token, method=method)
        response = requests.post(url, json=params or {})
        
        if not response.ok:
            raise Exception(f"Ошибка API: {response.text}")
            
        return response.json()["result"] 

    def send_message(self, chat_id: str, message: str) -> None:
        self._make_request("sendMessage", {"chat_id": chat_id, "text": message})

    def get_chat_id(self) -> str:
        updates = self._make_request("getUpdates", {"timeout": 10})
        if not updates:
            raise Exception("Отправьте сообщение боту для получения ChatID")
            
        last_update = updates[-1]
        
        # Проверяем различные типы сообщений
        message = last_update.get("message")
        if message:
            return str(message.get("chat", {}).get("id"))
            
        channel_post = last_update.get("channel_post")
        if channel_post:
            return str(channel_post.get("chat", {}).get("id"))
            
        raise Exception("Не удалось получить ChatID")