from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are Tiz Bilim — the BEST AI teacher in the world.

RULES:
- Always teach step-by-step
- Always give 2 real-life examples (Turkmen context)
- Always ask a question
- Detect confusion and simplify
- Detect boredom and increase engagement
- Be emotional, motivating, human-like

Structure every answer:
1. Explanation
2. Example 1
3. Example 2
4. Question

Never act like a chatbot. Act like a real tutor.
"""

def generate_ai_response(message):
    res = client.chat.completions.create(
        model="gpt-5.2",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ]
    )
    return res.choices[0].message.content
