import logging
from flask import current_app, jsonify
import json
import requests

# from app.services.openai_service import generate_response
import re

from dotenv import load_dotenv
import os

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


def log_http_response(response):
    logging.info(f"Status: {response.status_code}")
    logging.info(f"Content-type: {response.headers.get('content-type')}")
    logging.info(f"Body: {response.text}")


def get_text_message_input(recipient, text):
    return json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            # "type": "text",
            "type": "template",
            # "text": {"preview_url": False, "body": text},
            "template": {
                "namespace": "f701d0b1_eed6_466e_bedb_128a0e30871b",
                "name": "features",
                "language": {"code": "ml", "policy": "deterministic"},
            },
        }
    )


def generate_response(response):
    # Return text in uppercase
    return response.upper()


def send_message(data):
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {current_app.config['ACCESS_TOKEN']}",
    }

    url = f"https://graph.facebook.com/{current_app.config['VERSION']}/{current_app.config['PHONE_NUMBER_ID']}/messages"

    print(f"Data Sending {data}")
    try:
        response = requests.post(
            url, data=data, headers=headers, timeout=10
        )  # 10 seconds timeout as an example
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.Timeout:
        logging.error("Timeout occurred while sending message")
        return jsonify({"status": "error", "message": "Request timed out"}), 408
    except (
        requests.RequestException
    ) as e:  # This will catch any general request exception
        logging.error(f"Request failed due to: {e}")
        return jsonify({"status": "error", "message": "Failed to send message"}), 500
    else:
        # Process the response as normal
        log_http_response(response)
        return response


def process_text_for_whatsapp(text):
    # Remove brackets
    pattern = r"\【.*?\】"
    # Substitute the pattern with an empty string
    text = re.sub(pattern, "", text).strip()

    # Pattern to find double asterisks including the word(s) in between
    pattern = r"\*\*(.*?)\*\*"

    # Replacement pattern with single asterisks
    replacement = r"*\1*"

    # Substitute occurrences of the pattern with the replacement
    whatsapp_style_text = re.sub(pattern, replacement, text)

    return whatsapp_style_text


# Function has some errors : To download files
def save_img(media_id):
    url = f"https://graph.facebook.com/v18.0/{media_id}/"

    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    response = requests.get(url, headers=headers, stream=True)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Specify the local path where you want to save the image
        local_path = "image.jpeg"  # Replace with the desired local path and filename

        # Saving the image to the local path
        with open(local_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)

        print(f"Image saved successfully at {local_path}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        print(response.text)


def process_whatsapp_message(body):
    wa_id = body["entry"][0]["changes"][0]["value"]["contacts"][0]["wa_id"]
    name = body["entry"][0]["changes"][0]["value"]["contacts"][0]["profile"]["name"]
    print("BODY:", body)

    # Check in coming data if its a button or image. If button give corresponding text message for image run the model and give the results 
    # message = dict()
    # if "message" in body["entry"][0]["changes"][0]["value"]:
    #     message = body["entry"][0]["changes"][0]["value"]["messages"][0]
    # elif "button" in body["entry"][0]["changes"][0]["value"]["messages"][0]:
    #     print("Buttton")
    # print(message["image"]["id"])
    # save_img(message["image"]["id"])
    message = body["entry"][0]["changes"][0]["value"]["messages"][0]
    print(f"{message=}")
    if message["type"] == "button" :
        print("Its a button")
        
    message_body = message["text"]["body"]

    # TODO: implement custom function here
    print(f"{message_body}")
    response = generate_response(message_body)

    # OpenAI Integration
    # response = generate_response(message_body, wa_id, name)
    # response = process_text_for_whatsapp(response)

    data = get_text_message_input(current_app.config["RECIPIENT_WAID"], response)
    send_message(data)


def is_valid_whatsapp_message(body):
    """
    Check if the incoming webhook event has a valid WhatsApp message structure.
    """
    return (
        body.get("object")
        and body.get("entry")
        and body["entry"][0].get("changes")
        and body["entry"][0]["changes"][0].get("value")
        and body["entry"][0]["changes"][0]["value"].get("messages")
        and body["entry"][0]["changes"][0]["value"]["messages"][0]
    )
