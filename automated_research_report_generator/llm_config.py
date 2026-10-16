from crewai import LLM
import os

llm = LLM(
    model="openai/gpt-4o",
    temperature=0.7,
    max_tokens=4000
)
