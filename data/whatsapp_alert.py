from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import os

# Load from environment
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

WA_FROM = os.getenv("TWILIO_WA_FROM")   # whatsapp:+14155238886
WA_TO   = os.getenv("TWILIO_WA_TO")     # whatsapp:+9613929206

def send_whatsapp(message: str):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        msg = client.messages.create(
            from_=WA_FROM,
            to=WA_TO,
            body=message
        )

        print(f"📲 WhatsApp SENT — SID: {msg.sid}")
        return msg.sid

    except TwilioRestException as e:
        print("❌ TWILIO ERROR:", e)
        return None

    except Exception as e:
        print("❌ GENERAL ERROR:", e)
        return None
