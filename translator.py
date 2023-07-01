import csv
import requests

file_path = input('Ingrese la ruta del CSV a traducir:\n')

# Specify the URL of your LibreTranslate server
server_url = 'http://localhost:5000'

# Translation parameters
from_lang = 'en'
to_lang = 'es'

# API endpoint for translation
api_endpoint = f'{server_url}/translate'

# Read the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    csv_data = list(reader)

# Perform translation
translated_data = []
total_lines = len(csv_data)
completed_lines = 0
for row in csv_data:
    text = row
    payload = {
    'q': text,
    'source': from_lang,
    'target': to_lang
    }

    # Print completion advancement
    completed_lines += 1
    progress = (completed_lines / total_lines) * 100
    print(f"Progress: {completed_lines}/{total_lines} ({progress:.2f}%)")

    try:
        # Send POST request to the server
        response = requests.post(api_endpoint, json=payload)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            translated_text = response.json()['translatedText']
            print(f'Translated text: {translated_text}')
            translated_data.append([translated_text])  # Append translated text to the list
        else:
            print(f'Error: {response.status_code} - {response.text}')

    except requests.exceptions.RequestException as e:
        print(f'Request Exception: {e}')

# Write translated data to a new CSV file
with open('translation.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(translated_data)

print("Tu traducción está lista!")

