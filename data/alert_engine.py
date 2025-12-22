# alert_engine.py
from datetime import datetime

class GlucoseAlertEngine:
    def __init__(self):
        self.low_threshold = 70
        self.high_threshold = 140
        self.critical_high = 180

    def evaluate(self, reading: dict) -> dict:
        value = reading["value"]
        timestamp = reading["timestamp"]

        if value < self.low_threshold:
            return {
                "status": "critical",
                "level": value,
                "timestamp": timestamp,
                "message": "🚨 Blood sugar dangerously low!",
                "action_required": True
            }

        if value >= self.critical_high:
            return {
                "status": "critical",
                "level": value,
                "timestamp": timestamp,
                "message": "⚠️ High blood sugar detected! Consider insulin or medical advice.",
                "action_required": True
            }

        if value >= self.high_threshold:
            return {
                "status": "warning",
                "level": value,
                "timestamp": timestamp,
                "message": "⚠️ Blood sugar is high. Monitor closely.",
                "action_required": False
            }

        return {
            "status": "normal",
            "level": value,
            "timestamp": timestamp,
            "message": "Glucose level is within normal range.",
            "action_required": False
        }
