
# 📧 InboxAutopilot

**AI-Powered Email Assistant using Python, Gmail API and Ollama**

InboxAutopilot is a Python-based AI email assistant that helps users organize their Gmail inbox, categorize emails and generate professional reply suggestions using a locally running Ollama language model.

## 🚀 Features

- Connect to Gmail using Google OAuth 2.0.
- Fetch recent inbox emails.
- Categorize emails using AI.
- Generate professional email reply suggestions.
- Edit and review suggested replies.
- Save replies as Gmail drafts.
- Use Ollama locally without an OpenAI or Gemini API key.
- Keep email sending under the user's control.

## 🛠️ Tech Stack

- Python
- Streamlit
- Gmail API
- Google OAuth 2.0
- Ollama
- Llama 3.2
- Requests

## 📁 Project Structure

```text
InboxAutopilot/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── LICENSE
│
└── utils/
    ├── __init__.py
    ├── gmail_service.py
    └── ai_engine.py
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ganesh-hub7172/InboxAutopilot.git
cd InboxAutopilot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gmail API

1. Open Google Cloud Console.
2. Create a Google Cloud project.
3. Enable the Gmail API.
4. Configure the OAuth consent screen.
5. Create an OAuth Client ID using the Desktop App option.
6. Download the OAuth credentials file.
7. Rename it to `credentials.json`.
8. Place it in the project root folder.

**Never upload `credentials.json` or `token.json` to GitHub.**

### 5. Install and start Ollama

Download Ollama from:

https://ollama.com/

Pull the model:

```bash
ollama pull llama3.2
```

Make sure Ollama is running locally.

### 6. Run the application

```bash
python -m streamlit run app.py
```

## 🔐 Security

- Gmail access uses Google OAuth 2.0.
- Credentials and authentication tokens must remain local.
- Email analysis is performed using a local Ollama model.
- Reply suggestions are saved as drafts.
- The application does not automatically send emails.

## 🔮 Future Enhancements

- Smart priority detection.
- Email summarization.
- Custom email categories.
- Improved HTML email extraction.
- Search and filter functionality.
- Better AI-generated reply personalization.

## 👨‍💻 Author

**Ganesh Musham**

- GitHub: https://github.com/ganesh-hub7172
- LinkedIn: https://www.linkedin.com/in/ganesh-musham-14946b333/

---

⭐ If you find this project useful, consider giving it a star!
