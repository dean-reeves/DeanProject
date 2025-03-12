# func_py_email_extractor.py
import re

def func_py_email_extractor(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

sample_text = "Contact us at support@example.com or sales@company.org
