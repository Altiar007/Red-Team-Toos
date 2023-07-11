import sys
import os
import comtypes.client

def check_macros_enabled(file_path):
    # Get the file extension
    _, file_extension = os.path.splitext(file_path)
    
    # Check if the file is a Microsoft Office file
    if file_extension.lower() not in ('.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.xlsm', '.docm'):
        print("Not a Microsoft Office file.")
        return
    
    try:
        # Create an instance of the appropriate Office application
        if file_extension.lower() in ('.doc', '.docx', '.docm'):
            app = comtypes.client.CreateObject("Word.Application")
        elif file_extension.lower() in ('.xls', '.xlsx', '.xlsm'):
            app = comtypes.client.CreateObject("Excel.Application")
        
        # Disable displaying alerts
        app.DisplayAlerts = False
        
        # Open the file
        doc = app.Documents.Open(file_path) if file_extension.lower() in ('.doc', '.docx', '.docm') else app.Workbooks.Open(file_path)
        
        # Check if macros are enabled
        if doc.HasVBProject:
            print("Macros are enabled.")
        else:
            print("Macros are disabled.")
        
        # Close the file without saving changes
        doc.Close(False)
        app.Quit()
    except Exception as e:
        print("Error:", e)

# Get the file path from the command-line argument
if len(sys.argv) != 2:
    print("Usage: python macro_detection.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]
check_macros_enabled(file_path)
