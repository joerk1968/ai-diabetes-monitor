class AlertEngine:
    def evaluate(self, reading):
        value = reading["value"]

        if value >= 180:
            return "HIGH_GLUCOSE"
        elif value <= 70:
            return "LOW_GLUCOSE"

        return None
