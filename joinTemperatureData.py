import os
import csv

def extract_header_info(header_lines):
    name = header_lines[0].split(":")[1].strip()
    code = header_lines[1].split(":")[1].strip()
    return name, code

def process_csv_files():
    """Process all CSV files in the specified folder."""
    folder_y = 'Dados Estacoes' 
    output_file = 'combined_data.csv'

    with open(output_file, 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['Data Medicao', 'Nome', 'Codigo Estacao', 'TEMPERATURA MEDIA MENSAL (AUT)(°C)'])

        for filename in os.listdir(folder_y):
            if filename.endswith('.csv'):
                file_path = os.path.join(folder_y, filename)

                with open(file_path, 'r', encoding='utf-8') as f_in:
                    lines = f_in.readlines()
                    name, code = extract_header_info(lines[:8])  # Assuming header is always 8 lines

                    reader = csv.reader(lines[10:], delimiter=';')  # Start reading from the 11th line (skipping the column names)
                    next(reader)  # Skip the first line of the reader (column names)
                    for row in reader:
                        if row:  # Avoid processing empty rows
                            data_medicao = row[0]
                            temp_media = row[1].replace(',', '.')
                            writer.writerow([data_medicao, name, code, temp_media])

# Process the files
process_csv_files()

