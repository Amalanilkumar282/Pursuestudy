"""
QR Code Generator for Virtual Visiting Card
This script generates a QR code linking to the hosted version of the virtual visiting card.
"""

import qrcode
from PIL import Image
import os

def generate_qr_code(url, output_filename="virtual_card_qr.png"):
    """
    Generate a QR code for the given URL and save it as an image.
    
    Args:
        url (str): The URL to encode in the QR code
        output_filename (str): The filename to save the QR code image as
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(output_filename)
    print(f"QR code generated and saved as '{output_filename}'")
    print(f"QR code links to: {url}")

if __name__ == "__main__":
    # Replace this URL with the actual hosted URL of your virtual visiting card
    card_url = "https://pursuestudy.vercel.app/Geethanjali.html"
    
    # Generate the QR code
    generate_qr_code(card_url)
