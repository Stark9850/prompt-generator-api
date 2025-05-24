from fastapi import APIRouter, Request
from app.utils.prompt_builder import build_user_prompt
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# ✅ Groq-compatible OpenAI client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

router = APIRouter()

@router.post("/generate")
async def generate_prompt(request: Request):
    data = await request.json()
    pack = data.get("pack")
    inputs = data.get("inputs")

    if not pack or not inputs:
        return {"error": "Missing 'pack' or 'inputs' in request body."}

    # Create the dynamic user prompt using your logic
    user_prompt = build_user_prompt(pack, inputs)

    try:
        # Call Groq API
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are an expert prompt engineer. Generate high-quality prompts for ChatGPT based on the user's inputs."},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
        )
        return {"prompt": response.choices[0].message.content}

    except Exception as e:
        return {"error": f"Error: {str(e)}"}
