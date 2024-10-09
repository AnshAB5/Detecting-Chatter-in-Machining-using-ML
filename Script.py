import os
import re
import csv
import PySimpleGUI as sg
from PIL import Image
import io

# Ask user to select the folder containing images
folder_path = sg.popup_get_folder('Select folder containing images')
if not folder_path:
    sg.popup('No folder selected. Exiting.')
    exit()

# Open CSV file for writing
csv_file = open('output.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Index', 'Image File Name', 'Yes/No', 'doc value', 'RPM Value'])

# Initialize index
index = 1

# Get list of image files
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

for image_file in image_files:
    # Get full path of the image
    image_path = os.path.join(folder_path, image_file)
    
    # Extract 'doc' and 'RPM' values from filename
    doc_match = re.search(r'(\d+)\s*doc', image_file, re.IGNORECASE)
    rpm_match = re.search(r'(\d+)\s*RPM', image_file, re.IGNORECASE)
    
    doc_value = doc_match.group(1) if doc_match else ''
    rpm_value = rpm_match.group(1) if rpm_match else ''
    
    # Open and resize the image
    image = Image.open(image_path)
    max_size = (800, 600)
    image.thumbnail(max_size)
    
    # Convert the image to bytes for PySimpleGUI
    bio = io.BytesIO()
    image.save(bio, format='PNG')
    image_bytes = bio.getvalue()
    
    # Define the layout of the GUI
    layout = [
        [sg.Text(f"Image: {image_file}")],
        [sg.Image(data=image_bytes)],
        [sg.Text("Do you want to select 'Yes' or 'No'?")],
        [sg.Button('Yes'), sg.Button('No'), sg.Button('Exit')]
    ]
    
    # Create the window
    window = sg.Window('Image Viewer', layout)
    
    # Event loop to process "events" and get the "values" of inputs
    while True:
        event, values = window.read()
        if event in ('Yes', 'No'):
            yes_no_value = True if event == 'Yes' else False
            break
        elif event in (sg.WIN_CLOSED, 'Exit'):
            csv_file.close()
            window.close()
            exit()
    window.close()
    
    # Write data to CSV
    csv_writer.writerow([index, image_file, yes_no_value, doc_value, rpm_value])
    
    # Increment index
    index += 1

# Close CSV file
csv_file.close()
sg.popup('Data collection complete. CSV file has been saved.')