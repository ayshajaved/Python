import qrcode
from qrcode.constants import ERROR_CORRECT_H

qr = qrcode.QRCode(
    version=2,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data("https://www.linkedin.com/in/ayesha-javed-0a3647315/")
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="yellow")
img.save("mylinkedin.png")
