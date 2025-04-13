# Email Automation Script for Job Applications

This Python script automates the process of sending personalized job application emails to multiple recipients. It reads email addresses and names from a CSV file, composes a personalized email, and sends it to each recipient. The script also attaches your resume to the email.

## Features:
- Sends personalized emails to a list of recipients from a CSV file.
- Attaches a PDF resume to each email.
- Uses Gmail's SMTP server for sending emails.

## Requirements:
- Python 3.x
- Gmail account (with App Password enabled for authentication)
- `recipients.csv` file containing the recipient names and email addresses.
- Your resume in PDF format (or any other supported format).

## Prerequisites:
1. **Enable App Password in Gmail**:
   - Go to your [Google Account Settings](https://myaccount.google.com/).
   - Enable 2-Step Verification.
   - Create an **App Password** for your email application. Select "Mail" as the app and "Other" as the device, then name it (e.g., "Python Script").
   - Copy the generated App Password and use it in the script.

2. **Install Python Dependencies**:
   - No external libraries are required for this script, as it uses built-in Python modules such as `smtplib`, `csv`, and `email`.
   
## Setup and Usage:

### Step 1: Prepare Your Files
1. **Create a CSV File (`**recipients.csv**`)**:
   - The CSV file should have the following format:
   
   ```csv
   Name,Email
   User1,user1@gmail.com
   User2,user2@gmail.com

Each row should contain the recipient's name and email address.

Place Your Resume:

Place your resume in PDF format in the same directory as the script. The file should be named **resume.pdf** (you can change the name in the script if needed).

Step 2: Configure the Script
Open the script mailer.py in a text editor.

Replace the following variables with your Gmail credentials and App Password:

sender_email: Your Gmail email address.

app_password: The App Password you generated in Step 1.

Ensure your resume's filename is correct in resume_path (if not resume.pdf).

Step 3: Run the Script
Place mailer.py, recipients.csv, and resume.pdf in the same directory.

Open a terminal or command prompt in that directory.

Run the script using Python 3:
python3 mailer.py

Step 4: Check Email Delivery
After running the script, it will send personalized emails to all recipients listed in recipients.csv with your resume attached.

The terminal will show a success or failure message for each email sent.

Troubleshooting:
FileNotFoundError: Ensure that the recipients.csv and resume.pdf are in the same directory as the script.

App Password Error: Double-check that you’ve generated the correct App Password for your Gmail account and that 2-Step Verification is enabled.

Notes:
The script uses Gmail's SMTP server (smtp.gmail.com) with port 587.

If you plan to send a large number of emails, consider using an email service like SendGrid to avoid Gmail's sending limits.

This script is for educational purposes. Make sure to use it responsibly and avoid sending spam emails.

License:
This project is licensed under the MIT License - see the LICENSE file for details.
