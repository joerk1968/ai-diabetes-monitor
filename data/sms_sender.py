import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

SMS_FROM = os.getenv("TWILIO_SMS_FROM")
SMS_TO = os.getenv("TWILIO_SMS_TO")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(message: str):
    if not SMS_TO:
        raise ValueError("TWILIO_SMS_TO is missing")

    msg = client.messages.create(
        body=message,
        from_=SMS_FROM,
        to=SMS_TO
    )

    print("📩 SMS SENT — SID:", msg.sid)
