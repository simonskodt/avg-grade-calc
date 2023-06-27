# Grade Calculator

This repository contains a script that allows you to calculate the average of your grades from university, based on the Danish grading scale. By providing a PDF file with the respective grades, the script will process the data and provide you with the average grade.

## Usage

To use the script, follow these steps:

1. Update the `before_grades` and `after_grades` variables in the `parse.pdf.py` file. Set them to the words that appear before and after the actual grades in your PDF file. This will help the script locate the grades correctly.

2. Run the script by executing the following command in the terminal or command prompt, replacing <filename>.pdf with the name of your PDF file:

```cmd
python .\__main__.py <filename>.pdf
```

Note that you don't need to provide the full path to the PDF file since the script handles that internally.

3. The script will process the PDF file and calculate the grade average. The result will be printed to the console in the following format:

```cmd
Grade average: <average of grades>
```

I hope you find this script useful for calculating your grade average.
