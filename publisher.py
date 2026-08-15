import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

finding = input("Beacon finding: ")

prompt = f"""
You are Beacon Publisher for Reedstar.

Turn this verified Beacon finding into a concise draft:

{finding}

Rules:
- Use only the supplied evidence.
- Do not invent statistics or claims.
- Identify the business problem.
- Explain why it matters.
- Connect it naturally to a relevant Reedstar service.
- End with a clear, non-pushy CTA.
- Return the draft only.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print(response.text)
