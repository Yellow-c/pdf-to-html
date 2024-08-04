  import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    pdf_text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pdf_text += page.get_text()
    return pdf_text

def create_html_from_text(text, output_html_path):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PDF Content</title>
    </head>
    <body>
        <pre>{text}</pre>
    </body>
    </html>
    """
    with open(output_html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

def main():
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    for pdf_file in pdf_files:
        pdf_text = extract_text_from_pdf(pdf_file)
        output_html_path = pdf_file.replace('.pdf', '.html')
        create_html_from_text(pdf_text, output_html_path)

if __name__ == "__main__":
    main()
