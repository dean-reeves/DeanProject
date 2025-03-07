# func_py_image_resizer.py
from PIL import Image

def func_py_image_resizer(image_path, width, height):
    img = Image.open(image_path)
    img_resized = img.resize((width, height))
    img_resized.save(f"resized_{image_path}")
    return f"Saved resized_{image_path}"

print(func_py_image_resizer("image.jpg", 100, 100))
