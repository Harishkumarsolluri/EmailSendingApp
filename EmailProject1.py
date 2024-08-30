import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import json
st.title('Email Sender App with Attachment')
# Your email credentials
st.sidebar.header('Email Configuration')
smtp_server = st.sidebar.text_input('SMTP Server', 'smtp.gmail.com')
smtp_port = st.sidebar.number_input('SMTP Port', 587)
login = st.sidebar.text_input('Login Email')
password = st.sidebar.text_input('Password', type='password')

st.header('Compose Email')
sender_email = st.text_input('Sender Email',login)
receiver_email = st.text_input('Receiver Email')
subject = st.text_input('Subject')
message = st.text_area('Message')
attachment = st.file_uploader("Choose a file", type=["txt", "pdf", "png", "jpg", "jpeg", "gif", "docx", "xlsx"])

if st.button("Send Email"):
    try:
            # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

            # Add body to email
        msg.attach(MIMEText(message, 'plain'))
        msg.attach(MIMEApplication(file.read(), Name=attachment))

            # Connect to the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email,receiver_email, msg.as_string())

        # Disconnect from the server
        server.quit()

        print(f"Email successfully sent to {receiver_email}")
    except Exception as e:
        print(f"Error sending email to {receiver_email}: {e}")
