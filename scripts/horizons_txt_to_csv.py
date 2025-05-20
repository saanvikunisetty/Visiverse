import csv

def parse_horizons_txt_to_csv(input_txt_path, output_csv_path):
    with open(input_txt_path, 'r') as file:
        lines = file.readlines()

    start = None
    end = None
    for i, line in enumerate(lines):
        if line.strip() == '$$SOE':
            start = i + 1
        elif line.strip() == '$$EOE':
            end_= i
            break

    if start is None or end is None:
        raise ValueError("Data delimiters not found")
    
    data_lines = lines[start:end]
    data_rows = [line.strip().split(',') for line in data_lines if line.strip()]

    with open(output_csv_path, 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data_rows)
        print("Converted" + input_txt_path + " to clean CSV file " + output_csv_path)