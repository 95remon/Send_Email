from flask import Flask, request, jsonify
from exchangelib import DELEGATE, Account, Credentials, Message, Mailbox, Configuration, HTMLBody
import json
import argparse
import logging
from datetime import datetime , timedelta

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

@app.route('/alert/<alert_type>', methods=['POST'])
def alert(alert_type):
    config = load_config()
    data = request.json

    if not data:
        return jsonify({'message': 'Invalid data'}), 400

    if alert_type not in config['alerts']:
        return jsonify({'message': 'Invalid alert type'}), 400

    alert_config = config['alerts'][alert_type]
    email_details, error = send_email(data, config, alert_config)

    if error:
        return jsonify({'message': f'Failed to send email: {error}', 'email_details': email_details}), 500

    return jsonify({
        'message': f'Alert {alert_type} received and email sent',
        'email_details': email_details
    }), 200


def send_email(data, config, alert_config):
    EXCHANGE_EMAIL = config['exchange_email']
    EXCHANGE_PASSWORD = config['exchange_password']
    SUBJECT = alert_config['subject']
    credentials = Credentials(EXCHANGE_EMAIL, EXCHANGE_PASSWORD)
    account = Account(EXCHANGE_EMAIL, credentials=credentials, autodiscover=True)

    # Conditional logic for recipients based on the subject

    to_recipients = ['example@example.com','example@example.com']
    cc_recipients = ['example@example.com', 'example@example.com', 'example@example.com']

    
    SUBJECT = "Your Subject"
    subject = SUBJECT

    # Construct HTML body
    body_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Template</title>
    <style>
        <Add your Email Style here>
    </style>
</head>
<body style="margin: 0; padding: 0; font-family: Segoe UI; font-size:11px; background-color: #ffffff;" align="center">
    {data}
</body>
</html>
"""
    
    message = Message(
        account=account,
        subject=subject,
        body=HTMLBody(body_html),
        to_recipients=to_recipients,
        cc_recipients=cc_recipients
    )

    try:
        message.send()
        logging.debug("Email sent successfully")
        error = None
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        error = str(e)

    # Return email details for debugging
    email_details = {
        'data' : data,
        'subject': subject,
        'to_recipients': to_recipients,
        'cc_recipients': cc_recipients,
        'body': body_html
    }

    return email_details, error


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)