# install all the libraries needed
# create a function that collects a text and converts it to a qcode
# save the qrcode as an image

from asyncio import constants
from select import select
from turtle import fillcolor
import qrcode

def generate_qrcode(text):
    
    qr = qrcode.QRCode(
        version = 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("qrim.png")

if __name__ == "__main__":
    selected_link = input("choose your link to create qrcode: ")
    generate_qrcode(selected_link)
