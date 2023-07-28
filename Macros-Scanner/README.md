# Macros Scanner

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)

Macros Scanner is a simple Python script that checks whether a Microsoft Office file contains macros or not. It supports various Microsoft Office formats, including .doc, .docx, .xls, .xlsx, .ppt, .pptx, .xlsm, and .docm files.

## Usage

1. Clone this repository to your local machine.

```bash
git clone https://github.com/your_username/macros-scanner.git
cd macros-scanner
```
2. Run the Python script with the path to the Microsoft Office file as a command-line argument.
```
python macros_scanner.py <file_path>
```
Replace <file_path> with the path to the Microsoft Office file you want to scan for macros.

## Requirements
- Python 3.7 or higher is required to run the script.
- The comtypes library is used for interacting with Microsoft Office applications. You can install it using:
```
pip install comtypes
```

## Supported File Formats
The Macros Scanner supports the following Microsoft Office file formats:

- .doc (Word Document)
- .docx (Word Open XML Document)
- .xls (Excel Spreadsheet)
- .xlsx (Excel Open XML Spreadsheet)
- .ppt (PowerPoint Presentation)
- .pptx (PowerPoint Open XML Presentation)
- .xlsm (Excel Macro-Enabled Workbook)
- .docm (Word Macro-Enabled Document)

## How it Works
The script checks if the provided file is a Microsoft Office file and then uses the comtypes library to create an instance of the appropriate Office application (Word or Excel). It opens the file, checks if macros are enabled (using the HasVBProject property), and prints the result.

If macros are enabled, the script will display "Macros are enabled." Otherwise, it will show "Macros are disabled."

## Note
- This script only checks whether macros are enabled or disabled in the Microsoft Office file. It does not analyze or remove any existing macros.
