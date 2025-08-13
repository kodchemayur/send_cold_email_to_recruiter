# 📧 Recruiter Email Automation Tool

This Python tool automates sending **personalized job application emails to recruiters** using the **Gmail API**. It supports dynamic email content based on Excel input and allows file attachments (like your resume).

---

## 🚀 Features

- 🔐 Secure Gmail authentication (OAuth 2.0)
- 🧑‍💼 Dynamic personalization using Excel data:
  - Recruiter's first name
  - Company name
  - Job ID (optional)
- 📄 Attach resume or other documents
- 🖋️ Professionally formatted HTML email template
- 📊 Reads recruiter list from Excel (.xlsx)
- ✅ Reusability for Data Engineer, GenAI, or other roles

---

## 📁 Project Structure

recruiter-email-automation/
├── credentials.json # OAuth credentials from Google Cloud Console
├── token.json # Generated after successful authentication
├── emails.xlsx # Recruiter contact list
├── Mayur_Kodche.pdf # Resume or attachment
├── send_emails.py # Main automation script
└── README.md # Project documentation

---

## 🛠️ Setup Instructions

### 1. Clone the Repo
git clone https://github.com/your-username/recruiter-email-automation.git
cd recruiter-email-automation

### 2. Install Dependencies
pip install pandas google-auth google-auth-oauthlib google-api-python-client openpyxl

### 3. Enable Gmail API
Go to Google Cloud Console

Create a new project → Enable Gmail API

Create OAuth 2.0 credentials

Download credentials.json into the project folder

🧾 Prepare Your Files

🧑‍💼 emails.xlsx Format

| First Name | Email                                         | Company Name | Job Id                          |
| ---------- | --------------------------------------------- | ------------ | ------------------------------- |
| Priya      | [priya@company.com](mailto:priya@company.com) | ABC Corp     | 123456                          |
| John       | [john@xyz.com](mailto:john@xyz.com)           | XYZ Ltd      | (leave blank if not applicable) |

📎 Attachment
Save your resume as Mayur_Kodche.pdf (or update the filename in the script).

▶️ Run the Script
python send_emails.py

A browser window will open to authenticate your Gmail account.

Emails will be sent to each recruiter in your emails.xlsx file.


