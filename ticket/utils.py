import qrcode
import os

def generate_qr_code(ticket_id):
    # Create QRCode object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to QRCode
    qr.add_data(f'http://127.0.0.1:8000/ticket/{ticket_id}')
    qr.make(fit=True)

    # Generate QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    file_path = os.path.join('media/', 'qrcodes', f'{ticket_id}.png')

    img.save(file_path)
