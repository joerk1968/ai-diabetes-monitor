# data/synthetic_glucose_provider.py
import random
from datetime import datetime
from glucose_provider import GlucoseProvider


class SyntheticGlucoseProvider(GlucoseProvider):
    """
    Generates realistic synthetic glucose readings
    for demonstration and testing.
    """

    def __init__(self, start_value: int = 120):
        self.current_value = start_value

    def get_latest_reading(self):
        # Random glucose change
        change = random.randint(-25, 25)
        previous = self.current_value
        self.current_value = max(60, min(300, self.current_value + change))

        # Determine trend
        if self.current_value > previous:
            trend = "rising"
        elif self.current_value < previous:
            trend = "falling"
        else:
            trend = "stable"

        return {
            "value": self.current_value,
            "unit": "mg/dL",
            "trend": trend,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
