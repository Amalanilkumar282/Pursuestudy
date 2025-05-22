# Virtual Visiting Card

This project contains a responsive HTML page for a virtual visiting card and a Python script to generate a QR code that links to the hosted version of the card.

## Files

- `index.html`: The responsive HTML visiting card
- `generate_qr.py`: Python script to generate a QR code
- `virtual_card_qr.png`: The generated QR code (after running the Python script)

## HTML Visiting Card

The `index.html` file contains a responsive virtual visiting card that displays:

- Full Name (with a user icon)
- Email address (with a mail icon, clickable mailto: link)
- Employee ID (with an ID badge icon)

The card uses Bootstrap and Bootstrap Icons for styling and icons. It is responsive and works on both mobile and desktop devices.

## QR Code Generator

The `generate_qr.py` script generates a QR code that links to the hosted version of the virtual visiting card.

### Requirements

To run the QR code generator script, you need to install the following Python packages:

```
pip install qrcode[pil]
```

### Usage

1. Edit the URL in the `generate_qr.py` script to point to where your card will be hosted.
2. Run the script:

```
python generate_qr.py
```

3. The script will generate a file named `virtual_card_qr.png` in the same directory.

## Customization

To customize the virtual visiting card, edit the `index.html` file:

1. Replace "John Doe" with the actual name
2. Replace "john.doe@example.com" with the actual email address
3. Replace "EMP123456" with the actual employee ID

## Deployment

To deploy the virtual visiting card:

1. Host the `index.html` file on a web server
2. Update the URL in `generate_qr.py` to match your hosted URL
3. Regenerate the QR code
4. The QR code can be printed on physical visiting cards or shared digitally
