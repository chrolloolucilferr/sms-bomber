import requests
import time
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("FAST2SMS_KEY")

# Inputs
to_number = input("📞 Enter mobile number (without +91): ").strip()
msg = input("💬 Enter your message: ").strip()
count = int(input("🔁 How many times to send: "))
delay = float(input("⏱ Delay between messages (in seconds): "))

url = "https://www.fast2sms.com/dev/bulkV2"

for i in range(count):
    payload = {
        'sender_id': '',
        'message': msg + f" ({i+1}/{count})",
        'language': 'english',
        'route': 'q',
        'numbers': '91' + to_number,
    }

    headers = {
        'authorization': api_key,
        'Content-Type': "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    print(f"✅ Message {i+1} sent | Response:", response.text)
    time.sleep(delay)
