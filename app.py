import smtplib
from email.mime.text import MIMEText

import streamlit as st
from google import genai
from google.genai import types

from prompts import (
    SYSTEM_PROMPT,
    WELCOME_MESSAGE_TEMPLATE,
    SUMMARY_REQUEST_PROMPT
)

MODEL_NAME = "gemini-3.5-flash"

st.set_page_config(
    page_title="DeadlineLens",
    page_icon="📅"
)

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
GMAIL_ADDRESS = st.secrets["GMAIL_ADDRESS"]
GMAIL_APP_PASSWORD = st.secrets["GMAIL_APP_PASSWORD"]


@st.cache_resource
def get_gemini_client():
    return genai.Client(api_key=GEMINI_API_KEY)


gemini_client = get_gemini_client()


def render_message(message):
    with st.chat_message(message["role"]):
        if message["kind"] == "text":
            st.write(message["content"])

        elif message["kind"] == "image":
            st.image(message["content"])


def add_message(role, kind, content):
    st.session_state.messages.append(
        {
            "role": role,
            "kind": kind,
            "content": content
        }
    )

    render_message(st.session_state.messages[-1])


def ask_gemini(parts):
    try:
        response = st.session_state.chat.send_message(parts)
        return response.text

    except Exception as error:
        return f"Sorry, something went wrong: {error}"


def send_email(to_address, subject, body):
    try:
        gmail_address = GMAIL_ADDRESS.strip()
        app_password = GMAIL_APP_PASSWORD.replace(" ", "").strip()

        message = MIMEText(body, "plain", "utf-8")

        message["Subject"] = subject
        message["From"] = gmail_address
        message["To"] = to_address

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=20) as server:
            server.ehlo()

            server.starttls()

            server.ehlo()

            server.login(
                gmail_address,
                app_password
            )

            server.send_message(message)

        return True, "Email sent successfully."

    except smtplib.SMTPAuthenticationError as error:
        return False, f"Gmail authentication failed: {error}"

    except smtplib.SMTPConnectError as error:
        return False, f"Could not connect to Gmail SMTP: {error}"

    except smtplib.SMTPServerDisconnected as error:
        return False, f"Gmail SMTP disconnected unexpectedly: {error}"

    except TimeoutError:
        return False, "Connection to Gmail SMTP timed out."

    except Exception as error:
        return False, f"{type(error).__name__}: {error}"


# ---------------- ONBOARDING ----------------

if "onboarded" not in st.session_state:
    st.title("📅 DeadlineLens")
    st.caption(
        "Upload deadlines. Understand them. Email yourself a clean summary."
    )

    with st.form("onboarding_form"):
        name = st.text_input("Your name")

        email = st.text_input(
            "Your email address",
            placeholder="you@example.com"
        )

        submitted = st.form_submit_button("Let's go 🚀")

        if submitted:
            if not name.strip() or not email.strip():
                st.warning(
                    "Please fill in both your name and email."
                )

            else:
                st.session_state.name = name.strip()
                st.session_state.email = email.strip()

                st.session_state.chat = gemini_client.chats.create(
                    model=MODEL_NAME,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT
                    )
                )

                st.session_state.messages = []
                st.session_state.onboarded = True

                st.rerun()

    st.stop()


# ---------------- MAIN APP ----------------

header_col, button_col = st.columns(
    [5, 2],
    vertical_alignment="center"
)

with header_col:
    st.title("📅 DeadlineLens")

with button_col:
    send_disabled = len(st.session_state.messages) <= 1

    if st.button(
        "📧 Send Summary",
        disabled=send_disabled,
        use_container_width=True
    ):
        with st.spinner(
            "Preparing your deadline summary..."
        ):

            summary = ask_gemini(
                [SUMMARY_REQUEST_PROMPT]
            )

            subject = f"📅 DeadlineLens Summary for {st.session_state.name}"

            success, info = send_email(
                st.session_state.email,
                subject,
                summary
            )

        if success:
            st.success(
                "Deadline summary sent to your email! 📧"
            )

        else:
            st.error(
                f"Couldn't send email: {info}"
            )


st.caption(
    f"Logged in as {st.session_state.name} • summaries will go to {st.session_state.email}"
)


if not st.session_state.messages:
    add_message(
        "assistant",
        "text",
        WELCOME_MESSAGE_TEMPLATE.format(
            name=st.session_state.name
        )
    )

else:
    for message in st.session_state.messages:
        render_message(message)


user_input = st.chat_input(
    "Ask about deadlines, or attach an image",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"]
)


if user_input:
    photo = (
        user_input.files[0]
        if user_input.files
        else None
    )

    text = user_input.text

    parts = []

    if photo is not None:
        photo_bytes = photo.getvalue()

        add_message(
            "user",
            "image",
            photo_bytes
        )

        parts.append(
            types.Part.from_bytes(
                data=photo_bytes,
                mime_type=photo.type
            )
        )

    if text:
        add_message(
            "user",
            "text",
            text
        )

        parts.append(text)

    elif photo is not None:
        parts.append(
            "Analyze this image and identify all deadlines, dates, times, tasks, subjects, and important instructions."
        )

    with st.spinner(
        "Scanning for deadlines..."
    ):
        answer = ask_gemini(parts)

    add_message(
        "assistant",
        "text",
        answer
    )
    st.rerun()