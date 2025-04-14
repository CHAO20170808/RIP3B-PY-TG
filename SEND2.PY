import os
from datetime import datetime

def capture_image():
    # 使用當前系統時間生成唯一的檔案名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # 格式: 年月日_時分秒
    image_path = f"/home/pi/captured_image_{timestamp}.jpg"
    
    # 使用 fswebcam 捕捉影像
    os.system(f"fswebcam -r 1280x720 {image_path}")
    return image_path

def send_to_telegram(image_path, chat_ids):
    from telegram import Bot
    
    bot_token = "YOUR_BOT_API_TOKEN"  # 替換為您的 Bot Token
    bot = Bot(token=bot_token)
    
    for chat_id in chat_ids:
        try:
            bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))
            print(f"Image successfully sent to chat_id {chat_id}")
        except Exception as e:
            print(f"Failed to send image to chat_id {chat_id}: {e}")

if __name__ == "__main__":
    # 擷取影像並發送
    image_path = capture_image()
    chat_ids = ["563666314", "123456789"]  # 替換為目標 chat_id 列表
    send_to_telegram(image_path, chat_ids)