import os
import base64
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]


def get_gmail_service():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists("credentials.json"):
                raise FileNotFoundError(
                    "Download your Google OAuth credentials.json file first."
                )

            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def get_recent_emails(service, max_results=10):
    response = service.users().messages().list(
        userId="me",
        maxResults=max_results,
        labelIds=["INBOX"]
    ).execute()

    emails = []

    for message in response.get("messages", []):
        details = service.users().messages().get(
            userId="me",
            id=message["id"],
            format="full"
        ).execute()

        headers = details.get("payload", {}).get("headers", [])
        header_map = {h["name"].lower(): h["value"] for h in headers}

        body = extract_body(details.get("payload", {}))

        emails.append({
            "id": message["id"],
            "sender": header_map.get("from", "Unknown"),
            "subject": header_map.get("subject", "(No subject)"),
            "body": body
        })

    return emails


def extract_body(payload):
    body_data = payload.get("body", {}).get("data")

    if body_data:
        return base64.urlsafe_b64decode(body_data).decode(
            "utf-8", errors="replace"
        )

    for part in payload.get("parts", []):
        result = extract_body(part)
        if result:
            return result

    return ""


def create_draft(service, recipient, subject, body):
    message = MIMEText(body)
    message["to"] = recipient
    message["subject"] = "Re: " + subject

    encoded_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    draft = {
        "message": {
            "raw": encoded_message
        }
    }

    return service.users().drafts().create(
        userId="me",
        body=draft
    ).execute()
