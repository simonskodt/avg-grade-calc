import parse_pdf
import calc

import argparse
import os
import sys

def main(file_path):
    pdf_content = parse_pdf.read_pdf(file_path)
    trimmed = parse_pdf.trim_content(pdf_content)
    grades = parse_pdf.extract_grades(trimmed)
    avg_grades = calc.calc_avg(grades)

    print(f"Grade average: {avg_grades}")

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="Name of the PDF file")
    args = parser.parse_args()
    if not args.file.lower().endswith(".pdf"):
        sys.stderr.write('Error: file is not a PDF file\n')
        exit(1)

    return args

def construct_file_path(args):
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, args)
    if not os.path.isfile(file_path):
        sys.stderr.write('Error: file does not exist\n')
        exit(1)

    return file_path

if __name__ == "__main__":
    args = parse_arguments()
    file_path = construct_file_path(args.file)
    
    main(file_path)