# monitor_loop.py
import time
from data.synthetic_glucose_provider import SyntheticGlucoseProvider
from data.alert_engine import GlucoseAlertEngine
from data.alert_notifier import AlertNotifier
from data.whatsapp_alert import send_whatsapp


def run_monitoring_loop(interval_seconds=2):
    
    provider = SyntheticGlucoseProvider()
    engine = GlucoseAlertEngine()
    notifier = AlertNotifier()
    
    print("🩺 Diabetes monitoring started. cloud mode..\n")
    while True:
        try:
            reading = provider.get_latest_reading()
            print(f"Reading: {reading}")
            alert = engine.evaluate(reading)
            notifier.notify(alert, reading)
            time.sleep(interval_seconds)

        except Exception as e:
            print("run time error:",e)
            time.sleep(15)

if __name__ == "__main__":
    run_monitoring_loop()
