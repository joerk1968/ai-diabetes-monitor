# data/glucose_provider.py
from abc import ABC, abstractmethod
from typing import Dict


class GlucoseProvider(ABC):
    """
    Abstract interface for glucose data providers.
    Any real or simulated sensor must implement this.
    """

    @abstractmethod
    def get_latest_reading(self) -> Dict:
        """
        Returns the latest glucose reading.

        Expected format:
        {
            "value": int,
            "unit": "mg/dL",
            "trend": str,
            "timestamp": str
        }
        """
        pass
