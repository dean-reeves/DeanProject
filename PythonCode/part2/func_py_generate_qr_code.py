# func_py_generate_qr_code.py
import qrcode

def func_py_generate_qr_code(data, filename="qrcode.png"):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)

func_py_generate_qr_code("https://www.python.org")
