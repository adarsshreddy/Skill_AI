

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Fast model for everyday conversations
MODEL_NAME = "gemini-3.5-flash-lite"

if not API_KEY:
    raise ValueError("Gemini API key is missing in .env")

client = genai.Client(api_key=API_KEY)

SYSTEM_INSTRUCTION = """
You are SkillPilot AI, a friendly technology mentor.

Teach beginners using simple English.
Answer the question directly.
Use short paragraphs and practical examples.
Avoid unnecessary introductions.
Keep normal answers concise.
Use code examples when helpful.
Ask one follow-up question only when necessary.
"""


def stream_gemini(prompt):
    """Generate an answer progressively."""

    response_stream = client.models.generate_content_stream(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.3,
            max_output_tokens=600
        )
    )

    for chunk in response_stream:
        if chunk.text:
            yield chunk.text


def ask_gemini(prompt):
    """Generate a complete answer."""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.3,
            max_output_tokens=600
        )
    )

    return response.text or "No response received."
