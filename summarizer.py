import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_article(text):
    prompt = f"Summarize this news article in 3-4 sentences:\n{text}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful news summarizer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error summarizing article: {e}"