from twilio.rest import Client
from dotenv import load_dotenv
import os

# ✅ Load .env FIRST
load_dotenv()

# ✅ Now read environment variables
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

SMS_FROM = os.getenv("TWILIO_SMS_FROM")
SMS_TO = os.getenv("PATIENT_PHONE_SMS")

WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")
WHATSAPP_TO = os.getenv("PATIENT_PHONE_WHATSAPP")

# ✅ Debug (safe now)
print("DEBUG TWILIO ENV")
print("SID:", TWILIO_ACCOUNT_SID)
print("SMS FROM:", SMS_FROM)
print("SMS TO:", SMS_TO)
print("WA FROM:", WHATSAPP_FROM)
print("WA TO:", WHATSAPP_TO)

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
def send_whatsapp(message: str):
    try:
        msg = client.messages.create(
            body=message,
            from_=WHATSAPP_FROM,
            to=WHATSAPP_TO
        )
        print(f"📲 WhatsApp SENT — SID: {msg.sid}")
        return msg.sid
    except Exception as e:
        print("❌ WhatsApp failed:", e)
        return None


def send_sms(message: str):
    try:
        msg = client.messages.create(
            body=message,
            from_=SMS_FROM,
            to=SMS_TO
        )
        print(f"📩 SMS SENT — SID: {msg.sid}")
        return msg.sid
    except Exception as e:
        print("❌ SMS failed:", e)
        return None
