import os
import base64
import json
import time
import pandas as pd
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# If modifying the email, the scope needs to be adjusted
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Path to your credentials.json file
CREDENTIALS_FILE = 'credentials.json'

def authenticate_gmail():
    """Authenticate the user via OAuth 2.0 and return the service."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # Refresh if expired
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=8080)  # OAuth flow

        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    try:
        service = build('gmail', 'v1', credentials=creds)
        return service
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

# Data Engineer roles with strong data engineering foundation
def send_email(service, sender, to, first_name, company_name, job_id=None, attachment=None):
    """Send an email with an optional attachment using Gmail API."""
    try:
        # Create the MIME email
        message = MIMEMultipart()
        message['to'] = to
        message['subject'] = f"🚀 Available from Aug 25 | Data Engineer (Cloud + GenAI) for {company_name}"

        # Handle job ID formatting (NaN, None, or numeric values)
        if job_id and str(job_id).lower() != 'nan':
            # Convert to string and remove .0 if it's a float-like string
            job_id_str = str(job_id).replace('.0', '') if '.0' in str(job_id) else str(job_id)
            job_reference = f" (Req ID: <strong>{job_id_str}</strong>)"
        else:
            job_reference = ""

        # Generate dynamic "Why Excited" section
        why_excited = f"""
        <p>I'm particularly interested in how {company_name} leverages data engineering to drive business value. 
        My expertise in building scalable cloud solutions and implementing AI-powered data tools could help:</p>
        <ul>
            <li>Enhance your data pipeline reliability and monitoring</li>
            <li>Implement intelligent automation to reduce manual efforts</li>
            <li>Improve data quality and governance frameworks</li>
            <li>Optimize costs through cloud resource management</li>
        </ul>
        """

        # Email body with dynamic first name
        body = f"""
        <html>
        <head>
            <style>
                body {{ font-family: 'Arial', sans-serif; line-height: 1.6; color: #333; max-width: 650px; margin: 0 auto; }}
                .header {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
                .highlight {{ background-color: #f8f9fa; padding: 15px; border-left: 4px solid #3498db; margin: 15px 0; }}
                .notice {{ background-color: #fff8e1; padding: 15px; border-left: 4px solid #ffc107; margin: 15px 0; }}
                ul {{ padding-left: 20px; }}
                li {{ margin-bottom: 8px; }}
                .signature {{ margin-top: 25px; border-top: 1px solid #eee; padding-top: 15px; }}
                a {{ color: #3498db; text-decoration: none; }}
                .cta {{ background-color: #3498db; color: white; padding: 10px 15px; text-decoration: none; border-radius: 4px; display: inline-block; margin: 15px 0; }}
                .achievement {{ font-weight: bold; color: #2c3e50; }}
                .impact {{ color: #27ae60; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h2>Hi {first_name},</h2>
            </div>
            
            <div class="notice">
                <p><strong>Availability Update:</strong> I can join as early as <strong>August 25, 2025</strong> (negotiable). Currently serving notice period at Cognizant.</p>
            </div>
            
            <p>I'm reaching out regarding the Data Engineer position at {company_name}{job_reference}. With my experience in building enterprise-scale data solutions, I believe I could make immediate contributions to your team.</p>
            
            <div class="highlight">
                <h3 style="margin-top: 0; color: #2c3e50;">Here's what I bring to the table:</h3>
                
                <table width="100%" cellpadding="5">
                    <tr>
                        <td width="50%" valign="top">
                            <strong>🔧 Core Technical Stack:</strong>
                            <ul>
                                <li><span class="achievement">Python/PySpark/SQL</span> Expert</li>
                                <li><span class="achievement">AWS/GCP</span> Cloud Specialist</li>
                                <li><span class="achievement">Databricks/Spark</span> Architect</li>
                                <li><span class="achievement">AI/ML</span> Implementation</li>
                            </ul>
                        </td>
                        <td width="50%" valign="top">
                            <strong>🏆 Proven Impact:</strong>
                            <ul>
                                <li>Saved <span class="impact">25,000 IT hours</span> annually</li>
                                <li>Reduced data issues by <span class="impact">40%</span></li>
                                <li>Improved system reliability by <span class="impact">15%</span></li>
                                <li>Cut query resolution by <span class="impact">50%</span></li>
                            </ul>
                        </td>
                    </tr>
                </table>
            </div>

            <h3 style="color: #2c3e50;">Key Achievements at Cognizant (Nike Account):</h3>
            
            <p><strong>Data Pipeline Automation</strong></p>
            <ul>
                <li>Automated monitoring for <span class="impact">3,000+ workflows</span>, reducing manual work by <span class="impact">80%</span></li>
                <li>Developed auto-healing mechanisms saving <span class="impact">25,000 hours/year</span></li>
            </ul>
            
            <p><strong>AI-Powered Chatbot</strong></p>
            <ul>
                <li>Built RAG-based solution improving response time by <span class="impact">40%</span></li>
                <li>Achieved <span class="impact">95% accuracy</span> in user interactions</li>
            </ul>
            
            <p><strong>Data Quality Framework</strong></p>
            <ul>
                <li>Reduced data discrepancies by <span class="impact">50%</span> through automated validation</li>
                <li>Created lineage tracking tool improving debugging by <span class="impact">30%</span></li>
            </ul>

            <h3 style="color: #2c3e50;">How I Can Contribute to {company_name}:</h3>
            {why_excited}

            <div style="text-align: center;">
                <a href="https://www.linkedin.com/in/mayur-kodche/" class="cta">View My LinkedIn Profile</a>
                <span style="display: inline-block; margin: 0 10px;">|</span>
                <a href="mailto:Kodchemayur@gmail.com?subject=Schedule%20Call%20-%20Data%20Engineer%20Role%20at%20{company_name}" class="cta">Schedule a Quick Call</a>
            </div>

            <div class="signature">
                <p>Best regards,</p>
                <p><strong>Mayur Kodche</strong></p>
                <p>Data Engineer | Cloud & AI Solutions</p>
                <p>📞 8459663466 | ✉ <a href="mailto:Kodchemayur@gmail.com">Kodchemayur@gmail.com</a></p>
                <p><a href="https://www.linkedin.com/in/mayur-kodche/">linkedin.com/in/mayur-kodche</a></p>
                <p><em>Available from August 25, 2025 (date negotiable)</em></p>
            </div>
        </body>
        </html>
        """

        # Attach the email body as HTML
        message.attach(MIMEText(body, 'html'))

        # Attach file if provided
        if attachment:
            with open(attachment, 'rb') as file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={os.path.basename(attachment)}'
                )
                message.attach(part)

        # Encode the message to base64
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        message = {'raw': raw_message}
        message = service.users().messages().send(userId=sender, body=message).execute()
        print(f"Message Id: {message['id']}")
        return message
    except HttpError as error:
        print(f"An error occurred: {error}")

# GenAI/Data Science roles with strong data engineering foundation
# def send_email(service, sender, to, first_name, company_name, job_id, attachment=None):
#     """Send an email for GenAI/Data Science roles with strong data engineering foundation"""
#     try:
#         message = MIMEMultipart()
#         message['to'] = to
#         message['subject'] = f"""Application for GenAI/Data Scientist Role at {company_name} - MTech Data Science & Cloud Engineering Expertise"""

#         body = f"""
#         <html>
#         <body>
#             <p><b>Hi {first_name},</b></p>
#             <p>I'm excited to apply for the GenAI/Data Scientist position at {company_name} (Job ID: <b>{job_id}</b>). With my <strong>MTech in Data Science & Engineering</strong> from BITS Pilani and hands-on experience in both <strong>LLM implementation</strong> and <strong>production data systems</strong>, I can bridge the gap between AI innovation and scalable deployment.</p>
            
#             <h3>What I Bring to {company_name}:</h3>
            
#             <h4>GenAI/LLM Expertise</h4>
#             <ul>
#                 <li>Built <strong>RAG chatbot</strong> (95% accuracy) using Mosaic AI, reducing technical query resolution by <strong>50%</strong> through Slack integration</li>
#                 <li>Processed <strong>10,000+ unstructured documents</strong> using vector search and text splitting, improving response time by <strong>40%</strong></li>
#                 <li>Published research on <strong>ML-based cloud security</strong> (DDoS mitigation) with applications in data pipeline protection</li>
#             </ul>
            
#             <h4>Production Data Engineering</h4>
#             <ul>
#                 <li>Automated <strong>3,000+ data pipelines</strong> (Airflow/Databricks) reducing manual effort by <strong>80%</strong></li>
#                 <li>Developed <strong>data quality frameworks</strong> using Spark Expectations, cutting issues by <strong>40%</strong></li>
#                 <li>Optimized <strong>AWS Glue/Redshift</strong> pipelines processing <strong>1M+ records/day</strong>, lowering costs by <strong>30%</strong></li>
#                 <li>Created <strong>data lineage UI</strong> improving governance efficiency by <strong>25%</strong> across 500+ pipelines</li>
#             </ul>
            
#             <h4>Academic Foundation</h4>
#             <ul>
#                 <li><strong>MTech in Data Science & Engineering</strong> (BITS Pilani) with focus on distributed systems and ML</li>
#                 <li>BTech in Computer Science (<strong>9.29 CGPA</strong>) with strong algorithmic fundamentals</li>
#                 <li>Currently upskilling in <strong>LLM fine-tuning</strong> and <strong>Azure AI services</strong></li>
#             </ul>
            
#             <p>I'm particularly excited about {company_name}'s work in [specific company focus area]. My unique combination of <strong>cloud data engineering</strong> skills and <strong>applied GenAI experience</strong> enables me to develop solutions that are both innovative and production-ready.</p>
            
#             <p>I've attached my resume and would welcome the opportunity to discuss how I could contribute to your team. Please let me know a convenient time for a conversation.</p>
            
#             <p>Best regards,<br>
#             <b>Mayur Kodche</b><br>
#             MTech Data Science & Engineering (BITS Pilani)<br>
#             +91-8459663466 | <a href="mailto:Kodchemayur@gmail.com">Kodchemayur@gmail.com</a><br>
#             <a href="https://www.linkedin.com/in/mayur-kodche/">LinkedIn</a> | <a href="https://github.com/kodchemayur">GitHub</a></p>
#         </body>
#         </html>
#         """

#         message.attach(MIMEText(body, 'html'))

#         if attachment:
#             with open(attachment, 'rb') as file:
#                 part = MIMEBase('application', 'octet-stream')
#                 part.set_payload(file.read())
#                 encoders.encode_base64(part)
#                 part.add_header(
#                     'Content-Disposition',
#                     f'attachment; filename={os.path.basename(attachment)}'
#                 )
#                 message.attach(part)

#         raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
#         message = {'raw': raw_message}
#         message = service.users().messages().send(userId=sender, body=message).execute()
#         print(f"Message Id: {message['id']}")
#         return message
#     except HttpError as error:
#         print(f"An error occurred: {error}")

def read_emails_from_excel(file_path):
    """Read email data from an Excel file."""
    df = pd.read_excel(file_path) 
    email_data = []
    for _, row in df.iterrows():
        first_name = row['First Name']
        email = row['Email']
        company_name = row['Company Name']
        job_id = row['Job Id']

        email_data.append((first_name, email, company_name, job_id))
    return email_data

def main():
    sender = "kodchemayur@gmail.com"  # Replace with your email

    # Path to your Excel file with email data
    excel_file = 'emails.xlsx'
    # Path to the document you want to attach
    attachment_path = 'Mayur_Kodche.pdf'  # Replace with your document's path

    # Authenticate and get the Gmail service
    service = authenticate_gmail()

    if service:
        email_data = read_emails_from_excel(excel_file)

        for first_name, email, company_name, job_id in email_data:
            send_email(service, sender, email, first_name, company_name, job_id, attachment_path)

if __name__ == '__main__':
    main()
