import PyPDF2
import re

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        content = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            content += text

        return content
    
def trim_content(text):
    before_grades = "Marks Credits"
    after_grades = "Foundations of Computing"

    start_index = text.find(before_grades)
    end_index = text.find(after_grades)

    if start_index != -1 and end_index != -1:
        start_index += len(before_grades)
        desired_portion = text[start_index:end_index].strip()

    return desired_portion

def extract_grades(raw_grades):
    remove_newline = raw_grades.split("\n")
    grades = list(map(int, remove_newline))
    return grades