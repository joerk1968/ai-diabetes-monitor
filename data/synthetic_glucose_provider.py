import random
import datetime

class SyntheticGlucoseProvider:
    def __init__(self):
        self.value = 110

    def get_reading(self):
        change = random.randint(-15, 15)
        self.value = max(50, min(250, self.value + change))

        trend = "stable"
        if change > 5:
            trend = "rising"
        elif change < -5:
            trend = "falling"

        return {
            "value": self.value,
            "unit": "mg/dL",
            "trend": trend,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
