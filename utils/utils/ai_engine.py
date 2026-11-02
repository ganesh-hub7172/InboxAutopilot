import requests

OLLAMA_URL = "http://localhost:11434/api/chat"


def ask_ollama(prompt, model="llama3.2"):
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=180
    )

    response.raise_for_status()

    return response.json()["message"]["content"].strip()


def categorize_email(email_body, model="llama3.2"):
    prompt = f"""
    Categorize this email into exactly one category:
    Work, Personal, Important, Promotion, Spam, or Other.

    Return only the category name.

    Email:
    {email_body}
    """

    return ask_ollama(prompt, model)


def generate_reply(email_body, model="llama3.2"):
    prompt = f"""
    Write a professional, polite and concise reply to this email.

    Do not invent personal information or make commitments.
    Return only the suggested reply.

    Email:
    {email_body}
    """

    return ask_ollama(prompt, model)
