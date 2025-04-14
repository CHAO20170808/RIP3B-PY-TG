import os
from telegram import Bot
import asyncio

async def capture_image():
    # 定義圖片保存路徑
    image_path = "/home/agk32/captured_image.jpg"
    # 使用 fswebcam 捕捉影像
    os.system(f"fswebcam -r 1280x720 {image_path}")
    return image_path

async def send_to_telegram(image_path, chat_ids):
    # Telegram Bot Token
    bot_token = "YOU BOT TOKEN"  # 替換為您的 Bot Token
    bot = Bot(token=bot_token)

    for chat_id in chat_ids:
        try:
            # 發送圖片給每個 chat_id
            await bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))
            print(f"Image successfully sent to chat_id {chat_id}")
        except Exception as e:
            print(f"Failed to send image to chat_id {chat_id}: {e}")

async def main():
    # 擷取影像
    image_path = await capture_image()
    # 定義多個 chat_id
    chat_ids = ["要發送的Chat_id", "要發送的Chat_id2"]  # 替換為您的 chat_id 清單
    # 發送影像到 Telegram
    await send_to_telegram(image_path, chat_ids)

# 啟動異步函數
asyncio.run(main())