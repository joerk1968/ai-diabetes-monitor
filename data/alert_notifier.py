from data.whatsapp_alert import send_whatsapp
from data.sms_sender import send_sms

class AlertNotifier:
    def __init__(self, ai_advisor):
        self.ai = ai_advisor

    def notify(self, alert_type, reading):
        advice = self.ai.get_advice(reading)

        message = (
            f"🚨 Glucose Alert\n"
            f"Type: {alert_type}\n"
            f"Value: {reading['value']} mg/dL\n"
            f"Trend: {reading['trend']}\n\n"
            f"Advice:\n{advice}"
        )

        try:
            print("🔥 Attempting WhatsApp alert...")
            send_whatsapp(message)
        except Exception as e:
            print("❌ WhatsApp failed:", e)
            print("↩️ Falling back to SMS...")
            send_sms(message)
