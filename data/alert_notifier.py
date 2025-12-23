from data.sms_sender import send_sms,send_whatsapp
from data.ai_medical_advisor import AIMedicalAdvisor

class AlertNotifier:
    def __init__(self):
        self.ai = AIMedicalAdvisor()

    def notify(self, alert, reading):
        status = alert["status"]

        if status == "normal":
            return

        advice = self.ai.get_advice(reading)

        message = (
            f"🩺 Diabetes Alert ({status.upper()})\n"
            f"Glucose: {reading['value']} mg/dL\n"
            f"Trend: {reading['trend']}\n\n"
            f"AI Medical Advice:\n{advice}"
        )

        print("🔥 Attempting WhatsApp alert...")
        wa_sid = send_whatsapp(message)

        if wa_sid is None:
            print("↩️ Falling back to SMS...")
            send_sms(message)
