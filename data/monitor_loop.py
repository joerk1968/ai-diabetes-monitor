import time
from data.synthetic_glucose_provider import SyntheticGlucoseProvider
from data.alert_engine import AlertEngine
from data.alert_notifier import AlertNotifier
from data.ai_medical_advisor import AIMedicalAdvisor

def run_monitoring_loop(interval_seconds=5):
    provider = SyntheticGlucoseProvider()
    alert_engine = AlertEngine()
    advisor = AIMedicalAdvisor()
    notifier = AlertNotifier(advisor)

    while True:
        reading = provider.get_reading()
        print("Reading:", reading)

        alert = alert_engine.evaluate(reading)
        if alert:
            notifier.notify(alert, reading)

        time.sleep(interval_seconds)
