# Light Telegram Notifier

Микролиба для отправки уведомлений в Telegram


## Установка

```bash
pip install git+https://github.com/DiorditsPV/light-telegram-notifyer
```

## Отправка

```python
from ltm import TelegramNotifier

notifier = TelegramNotifier("TELEGRAM_BOT_TOKEN")
notifier.send_message("CHAT_ID", "Hello, Notify!")
```

## Получение ChatID

Для получения Chat ID используйте `reply_chatid.py`:

1. Отправьте любое сообщение боту в чат или канал
2. Определите переменную окружения `TELEGRAM_BOT_TOKEN`
3. Запустите еxample-код

```python
import os
from ltm.utils.reply_chatid import reply_chatid

if not os.environ.get("TELEGRAM_BOT_TOKEN"):
    raise ValueError("Добавте переменную TELEGRAM_BOT_TOKEN в окружение")

reply_chatid()
```
3. Бот ответит вам сообщением с вашим Chat ID

## Реплаи к посту канала
> #todo