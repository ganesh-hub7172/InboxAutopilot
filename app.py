import streamlit as st
from utils.gmail_service import get_gmail_service, get_recent_emails, create_draft
from utils.ai_engine import categorize_email, generate_reply

st.set_page_config(page_title="InboxAutopilot", page_icon="📧", layout="wide")

st.title("📧 InboxAutopilot")
st.caption("AI-powered email assistant using Gmail API and Ollama")

if "emails" not in st.session_state:
    st.session_state.emails = []

with st.sidebar:
    st.header("Settings")
    model = st.text_input("Ollama model", "llama3.2")

    if st.button("Connect Gmail"):
        try:
            st.session_state.service = get_gmail_service()
            st.success("Gmail connected!")
        except Exception as e:
            st.error(str(e))

if "service" not in st.session_state:
    st.info("Connect your Gmail account from the sidebar to begin.")
    st.stop()

if st.button("Fetch Recent Emails"):
    try:
        st.session_state.emails = get_recent_emails(
            st.session_state.service, max_results=10
        )
    except Exception as e:
        st.error(f"Unable to fetch emails: {e}")

for index, email in enumerate(st.session_state.emails):
    with st.expander(f"{email['subject']} — {email['sender']}"):
        st.write(email["body"])

        if st.button("Categorize Email", key=f"cat_{index}"):
            with st.spinner("Analyzing email..."):
                st.session_state[f"category_{index}"] = categorize_email(
                    email["body"], model
                )

        category = st.session_state.get(f"category_{index}")
        if category:
            st.success(f"Category: {category}")

        if st.button("Generate Reply", key=f"reply_{index}"):
            with st.spinner("Generating reply..."):
                st.session_state[f"reply_{index}"] = generate_reply(
                    email["body"], model
                )

        reply = st.session_state.get(f"reply_{index}")
        if reply:
            edited_reply = st.text_area(
                "Review and edit your reply",
                value=reply,
                key=f"edit_{index}"
            )

            if st.button("Save as Gmail Draft", key=f"draft_{index}"):
                try:
                    create_draft(
                        st.session_state.service,
                        email["sender"],
                        email["subject"],
                        edited_reply
                    )
                    st.success("Draft saved in Gmail. Review and send it manually.")
                except Exception as e:
                    st.error(f"Could not save draft: {e}")
