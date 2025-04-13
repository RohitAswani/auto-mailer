import smtplib
import csv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Your Gmail credentials
sender_email = "rohitaswani.53@gmail.com"
app_password = "YourAppPassword-WithoutSpace"

# Email content setup
subject = "Application for DevOps Engineer Role"

# Check if the CSV file exists
if not os.path.exists("recipients.csv"):
    print("❌ recipients.csv not found in the current directory.")
    exit(1)

# Check if resume exists
resume_path = "resume.pdf"
if not os.path.exists(resume_path):
    print(f"❌ {resume_path} not found. Please place your resume in the same directory as the script.")
    exit(1)

# Connect to Gmail SMTP
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
except Exception as e:
    print(f"❌ Error while connecting to Gmail SMTP: {e}")
    exit(1)

# Read CSV and send emails
with open("recipients.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        receiver_email = row["Email"]
        name = row["Name"]

        # Create personalized message
        body = f"""Hi {name},

I hope this message finds you well.

I am excited to apply for the DevOps Engineer role in your organisation. With 2+ years of experience in AWS, Terraform, CI/CD, and cloud infrastructure, I have successfully automated deployments, optimized infrastructure, and implemented security best practices.

In my current role at GrowExx, I:
✔ Migrated 18+ on-prem projects to AWS ECS Fargate, ensuring zero downtime & 100% data integrity
✔ Automated CI/CD pipelines (Jenkins, GitHub Actions), reducing deployment failures by 50%
✔ Optimized Docker & Terraform workflows, enhancing cloud efficiency and security compliance
✔ Deployed scalable applications using Fargate & AWS services

I am particularly excited about this opportunity as it aligns with my expertise in Infrastructure as Code, Cloud Automation, and DevOps.

Let me know if you'd like to connect further.

Thanks & regards,  
Rohit Aswani
"""

        # Create email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Attach the resume
        try:
            with open(resume_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={os.path.basename(resume_path)}",
                )
                message.attach(part)
        except Exception as e:
            print(f"❌ Error attaching resume: {e}")
            continue

        # Send the email
        try:
            server.sendmail(sender_email, receiver_email, message.as_string())
            print(f"✅ Email sent to {name} at {receiver_email}")
        except Exception as e:
            print(f"❌ Failed to send email to {receiver_email}: {e}")

# Close the server connection
server.quit()
