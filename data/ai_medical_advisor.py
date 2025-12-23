import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class AIMedicalAdvisor:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.3,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a medical assistant helping diabetes patients."),
            ("human", 
             "Glucose value: {value} mg/dL\n"
             "Trend: {trend}\n"
             "Give short, safe advice.")
        ])

    def get_advice(self, reading):
        response = self.llm.invoke(
            self.prompt.format_messages(
                value=reading["value"],
                trend=reading["trend"]
            )
        )
        return response.content
