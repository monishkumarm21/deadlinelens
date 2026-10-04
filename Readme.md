```markdown
# 📅 DeadlineLens

DeadlineLens is an AI-powered deadline tracking assistant that uses Google Gemini Vision to understand images containing deadlines, assignments, timetables, notices, syllabi, and calendars.

Users can upload an image, let the AI identify important dates and tasks, ask follow-up questions, generate a structured deadline summary, and send the summary directly to their email using Gmail SMTP.

---

## ✨ Features

- 📷 Upload images of:
  - Assignment sheets
  - Timetables
  - College notices
  - Syllabi
  - Calendars
  - Schedule screenshots

- 🤖 AI-powered image understanding using Google Gemini

- 📅 Extracts:
  - Task or event name
  - Subject or category
  - Deadline date
  - Time
  - Important instructions

- 💬 Conversational AI support

- 🔎 Ask follow-up questions such as:
  - Which deadline is closest?
  - What should I complete first?
  - What deadlines do I have this week?

- 📧 Generate and send a deadline summary through Gmail

- 🧠 Maintains conversation context during the current session

- 🔐 Secure handling of API keys and Gmail credentials using Streamlit Secrets

---

## 🎯 Problem Statement

Students often receive important academic deadlines through different sources such as notices, screenshots, assignment sheets, timetables, and syllabus documents.

Manually identifying and organizing these deadlines can be time-consuming and may lead to missed submissions.

DeadlineLens simplifies this process by allowing users to upload an image and automatically extract the important deadline-related information using AI.

The extracted information can then be discussed with the chatbot and sent as a clean summary directly to the user's email.

---

## 🚀 How DeadlineLens Works

```text
User
 │
 │ Uploads image / enters text
 ▼
Streamlit Interface
 │
 ▼
Google Gemini Vision
 │
 ├── Identifies tasks
 ├── Extracts dates
 ├── Extracts times
 ├── Extracts instructions
 └── Understands follow-up questions
 │
 ▼
Conversational Deadline Assistant
 │
 ▼
Generate Deadline Summary
 │
 ▼
Gmail SMTP
 │
 ▼
📧 User Inbox
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Web application interface |
| Google Gemini API | AI chat and image understanding |
| Google GenAI SDK | Communication with Gemini |
| Gmail SMTP | Sending deadline summaries through email |
| Python `smtplib` | SMTP email communication |
| Streamlit Community Cloud | Cloud deployment |

---

## 🧠 AI Capabilities

DeadlineLens uses a multimodal Gemini model, meaning the application can understand both:

```text
Text
+
Images
```

For example, a user may upload an assignment screenshot containing:

```text
DBMS Assignment
Submission Date: 10 October
Submit through LMS before 5 PM
```

DeadlineLens can identify:

```text
📌 Task/Event: DBMS Assignment
📚 Subject/Category: DBMS
📅 Date: 10 October
⏰ Time: 5 PM
📝 Important Note: Submit through LMS
```

The user can then ask:

```text
Which deadline should I prioritize first?
```

Gemini continues the same conversation and answers using the context from the uploaded image.

---

## 📧 Email Summary

After discussing deadlines, users can click:

```text
📧 Send Summary
```

DeadlineLens asks Gemini to generate a clean plain-text summary.

Example:

```text
📅 DeadlineLens Summary
━━━━━━━━━━━━━━━━━━━━

📌 Task/Event: DBMS Assignment
📚 Subject/Category: DBMS
📅 Date: 10 October 2026
⏰ Time: 5:00 PM
📝 Important Note: Submit through LMS.

━━━━━━━━━━━━━━━━━━━━

📌 Task/Event: Cryptography Record
📚 Subject/Category: Cryptography
📅 Date: 12 October 2026
⏰ Time: Not specified
📝 Important Note: Bring completed record.

━━━━━━━━━━━━━━━━━━━━

⚡ Priority
The DBMS Assignment has the earliest available deadline.
```

The summary is sent directly to the email address entered during onboarding.

---

## 📂 Project Structure

```text
deadlinelens/
│
├── app.py
├── prompts.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── .streamlit/
│   ├── secrets.toml
│   └── secrets.toml.example
│
└── venv/
```

### File Description

```text
app.py
```

Contains the main Streamlit application logic including:

- User onboarding
- Gemini connection
- Chat interface
- Image handling
- Session management
- Deadline summary generation
- Gmail SMTP integration

```text
prompts.py
```

Contains:

- DeadlineLens system prompt
- Welcome message
- Email summary prompt

Keeping prompts separate makes the application easier to maintain and modify.

```text
requirements.txt
```

Contains the external Python dependencies required by the project.

```text
.streamlit/secrets.toml
```

Contains private credentials used locally.

This file must never be uploaded to GitHub.

```text
.streamlit/secrets.toml.example
```

Provides an example of the secrets required to run the application.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Move into the project directory:

```bash
cd deadlinelens
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

The project currently requires:

```txt
streamlit
google-genai
```

Gmail functionality uses Python's built-in:

```python
smtplib
email.mime
```

so no additional email package is required.

---

## 🔑 Environment Setup

Create the following file:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "your-gemini-api-key"
GMAIL_ADDRESS = "your-gmail-address"
GMAIL_APP_PASSWORD = "your-google-app-password"
```

---

## 🔐 Gmail App Password

DeadlineLens uses Gmail SMTP instead of storing the user's normal Gmail password.

You should use a Google App Password.

General setup:

1. Enable 2-Step Verification on your Google account.
2. Open Google Account security settings.
3. Create an App Password.
4. Use the generated App Password in:

```toml
GMAIL_APP_PASSWORD = "your-app-password"
```

Do not use your normal Gmail password.

---

## ▶️ Run the Application Locally

After activating the virtual environment:

```bash
streamlit run app.py
```

Streamlit will start a local development server.

Usually the app will be available at:

```text
http://localhost:8501
```

---

## 🧪 Typical Usage Flow

```text
1. Open DeadlineLens

2. Enter:
   - Name
   - Email address

3. Upload an image containing deadlines

4. Gemini analyzes the image

5. Ask follow-up questions if needed

6. Click "📧 Send Summary"

7. Gemini generates a deadline digest

8. Gmail SMTP sends the summary

9. Check your inbox 📧
```

---

## 🔒 Security

Sensitive credentials are never hard-coded inside `app.py`.

DeadlineLens uses Streamlit Secrets:

```python
st.secrets["GEMINI_API_KEY"]
st.secrets["GMAIL_ADDRESS"]
st.secrets["GMAIL_APP_PASSWORD"]
```

The real secrets file is excluded through `.gitignore`:

```gitignore
.streamlit/secrets.toml
venv/
__pycache__/
```

Only the template file should be uploaded:

```text
.streamlit/secrets.toml.example
```

Example:

```toml
GEMINI_API_KEY = "your-gemini-api-key-here"
GMAIL_ADDRESS = "your-gmail-address-here"
GMAIL_APP_PASSWORD = "your-gmail-app-password-here"
```

---

## ☁️ Deployment

DeadlineLens can be deployed using Streamlit Community Cloud.

### Deployment Steps

1. Push the project to GitHub.

2. Open Streamlit Community Cloud.

3. Create a new application.

4. Select:
   - Repository
   - Branch
   - `app.py`

5. Add the following values in Streamlit Cloud Secrets:

```toml
GEMINI_API_KEY = "your-real-gemini-api-key"
GMAIL_ADDRESS = "your-real-gmail-address"
GMAIL_APP_PASSWORD = "your-real-app-password"
```

6. Deploy the application.

7. Test:
   - Image upload
   - Gemini response
   - Follow-up conversation
   - Email summary

---

## 🧩 Application Architecture

```text
┌──────────────────────────────┐
│            User              │
│                              │
│   Image / Text / Questions   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          Streamlit           │
│                              │
│  UI + Session State + Chat   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│        Google Gemini         │
│                              │
│   Vision + Conversation AI   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Deadline Extraction      │
│                              │
│ Dates | Tasks | Time | Notes │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Summary Generator      │
│                              │
│ Clean Plain-Text Digest      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          Gmail SMTP          │
│                              │
│       Email Delivery         │
└──────────────┬───────────────┘
               │
               ▼
         📧 User Inbox
```

---

## 🧭 Prompt Design

DeadlineLens uses a dedicated system prompt that instructs Gemini to focus specifically on deadlines.

The AI is instructed to:

- Identify deadline-related information
- Extract dates and times
- Extract task names
- Extract subjects and categories
- Identify relevant instructions
- Answer follow-up questions
- Avoid inventing missing information
- Clearly indicate when a deadline cannot be identified

This helps reduce hallucinations and keeps the AI focused on the intended use case.

---

## ⚠️ Limitations

DeadlineLens uses AI-based image understanding, so extracted information should still be reviewed by the user.

Accuracy may depend on:

- Image quality
- Handwriting clarity
- Visibility of dates
- Ambiguous wording
- Cropped images
- Missing context

DeadlineLens intentionally avoids inventing information when a clear deadline cannot be found.

---

## 🔮 Future Enhancements

Possible future improvements include:

- 📆 Google Calendar integration
- 🔔 Automatic deadline reminders
- 🗂️ Persistent deadline storage
- 📊 Deadline dashboard
- 🏷️ Deadline categorization
- 🚨 Urgency levels
- 👤 User authentication
- 📄 PDF upload support
- 📝 OCR fallback support
- 📱 Mobile-friendly improvements
- 🔄 Recurring deadline detection
- 🎓 Subject-wise deadline grouping

---

## 💡 Why DeadlineLens?

Traditional deadline tracking requires users to manually read and enter information into calendars or task management applications.

DeadlineLens combines:

```text
Computer Vision
+
Generative AI
+
Conversational AI
+
Email Automation
```

to turn an ordinary screenshot or photograph into useful deadline information within seconds.

---

## 📌 Example Use Cases

DeadlineLens can help with:

- College assignment notices
- Internal assessment schedules
- Laboratory submission deadlines
- Exam timetables
- Project submission notices
- Hackathon deadlines
- Placement schedules
- Workshop schedules
- Course calendars
- Event notices

---

## 👨‍💻 Author

**M. Monish Kumar**

B.E. Computer Science and Engineering

---

## ⭐ Acknowledgement

DeadlineLens was developed as part of an AI Vision application workshop project exploring:

- Multimodal AI
- Google Gemini Vision
- Conversational AI
- Streamlit
- API integration
- Email automation
- Cloud deployment

---

## 📄 License

This project is intended for educational and learning purposes.

---

## ⭐ Support

If you find DeadlineLens useful, feel free to star the repository.

```

### One tiny thing before GitHub

Your repository should eventually look like:

```text
deadlinelens
├── .streamlit
│   └── secrets.toml.example
├── .gitignore
├── README.md
├── app.py
├── prompts.py
└── requirements.txt
```

Notice what is **not** supposed to appear on GitHub:

```text
❌ secrets.toml
❌ venv/
❌ __pycache__/
```
