import pywhatkit


"""
Important Note:

- Make sure to install the required libraries:
pip install -r requirements.txt

- Your whatsapp must be open in the browser for this to work. means you must be logged in to your whatsapp web account.

- This script sends a WhatsApp message and an image to a specified phone number at a scheduled time.
It uses the pywhatkit library to automate WhatsApp messaging and image sharing.

"""

if __name__ == "__main__":
    # Set the time to send the message (24-hour format)
    hour = 15  # 3 PM
    minute = 24  # 30 minutes past the hour

    # Define the message and phone number
    message = "Hello !"
    image_path = "pexel_clone.png"
    phone_no = "+923422238842"
    
    # This is a simple script to send a WhatsApp message using pywhatkit
    pywhatkit.sendwhatmsg(phone_no, message, hour, minute)

    # This is a simple script to send a WhatsApp image using pywhatkit
    pywhatkit.sendwhats_image(phone_no, image_path, caption)