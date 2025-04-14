import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from telegram import Bot
import asyncio

# 捕捉圖片
async def capture_image():
    image_path = "/home/agk32/captured_image.jpg"
    os.system(f"fswebcam -r 1280x720 {image_path}")
    return image_path

# 添加時間戳
def add_timestamp(image_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    text_position = (10, image.size[1] - 30)
    draw.text(text_position, timestamp, fill=(255, 255, 255), font=font)
    image.save(image_path)
    return image_path

# 發送圖片至 Telegram
async def send_to_telegram(image_path, chat_ids):
    bot_token = "YOU BOT TOKEN"  # 替換為您的 Bot Token
    bot = Bot(token=bot_token)
    for chat_id in chat_ids:
        try:
            await bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))
            print(f"Image sent to chat_id {chat_id}")
        except Exception as e:
            print(f"Failed to send to chat_id {chat_id}: {e}")

# 主執行邏輯
async def main():
    image_path = await capture_image()
    add_timestamp(image_path)
    chat_ids = ["要發送的Chat_id", "要發送的Chat_id2"]  # 替換為您的 chat_id
    await send_to_telegram(image_path, chat_ids)

# 開始執行
asyncio.run(main())