import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

WA_FROM = os.getenv("TWILIO_WA_FROM")   # whatsapp:+14155238886
WA_TO = os.getenv("TWILIO_WA_TO")       # whatsapp:+961...

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp(message: str):
    if not WA_TO:
        raise ValueError("TWILIO_WA_TO is missing")

    msg = client.messages.create(
        body=message,
        from_=WA_FROM,
        to=WA_TO
    )

    print("📩 WhatsApp SENT — SID:", msg.sid)
