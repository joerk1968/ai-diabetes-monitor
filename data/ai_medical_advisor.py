# ai_medical_advisor.py
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables (.env)
load_dotenv()

class AIMedicalAdvisor:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.3
        )

        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """
You are a medical support AI for diabetes monitoring.
Your role is to provide SAFE, NON-DIAGNOSTIC advice.

Rules:
- DO NOT prescribe medication doses
- DO NOT replace doctors
- DO explain risks clearly
- DO suggest safe actions
- DO recommend contacting a healthcare professional when needed
"""
            ),
            (
                "user",
                """
Patient glucose reading:
- Value: {value} mg/dL
- Trend: {trend}

Give clear and calm advice suitable to be sent by SMS.
"""
            )
        ])

    def get_advice(self, glucose_reading: dict) -> str:
        response = self.llm.invoke(
            self.prompt.format_messages(
                value=glucose_reading["value"],
                trend=glucose_reading["trend"]
            )
        )
        return response.content.strip()
