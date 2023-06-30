import csv
from translate import Translator

file_path = input('Ingrese la ruta del CSV a traducir:\n')

# Read the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    csv_data = list(reader)

# Perform translation
translator = Translator(to_lang="es")
translated_data = []
total_lines = len(csv_data)
completed_lines = 0
for row in csv_data:

    # Print completion advancement
    translated_row = [translator.translate(cell) for cell in row]
    translated_data.append(translated_row)
        
    completed_lines += 1
    progress = (completed_lines / total_lines) * 100
    print(f"Progress: {completed_lines}/{total_lines} ({progress:.2f}%)")

# Write translated data to a new CSV file
with open('translation.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(translated_data)

print("Tu traducción está lista!")

