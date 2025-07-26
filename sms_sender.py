import os
import time
from tkinter import *
from tkinter import messagebox
from dotenv import load_dotenv
from twilio.rest import Client

# Load credentials
load_dotenv()
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
twilio_number = os.getenv("TWILIO_NUMBER")

client = Client(account_sid, auth_token)

# GUI setup
root = Tk()
root.title("SMS Loop Sender")
root.geometry("420x400")
root.resizable(False, False)

# Title
Label(root, text="📱 Twilio SMS Sender -by jemit", font=("Arial", 14, "bold")).pack(pady=10)

# Phone Number
Label(root, text="To Number (+91...)").pack()
to_entry = Entry(root, width=45)
to_entry.pack(pady=5)

# Message Body
Label(root, text="Message").pack()
msg_entry = Text(root, height=5, width=45)
msg_entry.pack(pady=5)

# Number of Times
Label(root, text="How many times? (Max 10)").pack()
count_entry = Entry(root, width=10)
count_entry.insert(0, "1")
count_entry.pack(pady=5)

# Delay
Label(root, text="Delay between messages (sec)").pack()
delay_entry = Entry(root, width=10)
delay_entry.insert(0, "5")
delay_entry.pack(pady=5)

def send_sms():
    to_number = to_entry.get().strip()
    msg_body = msg_entry.get("1.0", END).strip()
    count = count_entry.get().strip()
    delay = delay_entry.get().strip()

    if not to_number or not msg_body or not count or not delay:
        messagebox.showerror("Error", "All fields are required.")
        return

    try:
        count = int(count)
        delay = float(delay)

        if count > 10:
            confirm = messagebox.askyesno("Warning", "Sending more than 10 messages is not recommended. Continue?")
            if not confirm:
                return

        for i in range(count):
            msg = f"{msg_body} ({i+1}/{count})"
            message = client.messages.create(
                body=msg,
                from_=twilio_number,
                to=to_number
            )
            print(f"✅ Message {i+1} sent! SID: {message.sid}")
            time.sleep(delay)

        messagebox.showinfo("Done", f"✅ Sent {count} messages successfully!")

    except Exception as e:
        messagebox.showerror("Failed", f"❌ Error:\n{str(e)}")

Button(root, text="Send Message(s)", command=send_sms, bg="green", fg="white", padx=15, pady=6).pack(pady=15)
root.bind('<Return>', lambda event: send_sms())
root.mainloop()
