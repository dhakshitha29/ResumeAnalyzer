import pdfplumber

def parse_resume(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''.join(page.extract_text() for page in pdf.pages)
    print(text)  # This will help you debug and check the raw extracted text
    return text

