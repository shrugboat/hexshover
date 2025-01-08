import sys
import os
import glob
import re

def replace_section(file_path, data, start_position):
    with open(file_path, 'r+b') as file:
        file.seek(start_position)
        file.write(data)

def read_hex_file(hex_file_path):
    with open(hex_file_path, 'rb') as file:
        return file.read()

def get_start_position_from_filename(filename):
    # Extract the hexadecimal part from the end of the filename
    match = re.search(r'0x[0-9A-Fa-f]+', filename)
    if match:
        hex_part = match.group()
        return int(hex_part, 16)
    else:
        raise ValueError(f"No hexadecimal part found in filename: {filename}")

if __name__ == "__main__":
    target_file_path = sys.argv[1]
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Adjusted to only list .hex files and ignore subdirectories
    hex_files = [f for f in glob.glob(os.path.join(script_dir, '*.hex')) if os.path.isfile(f)]

    for hex_file in hex_files:
        start_position = get_start_position_from_filename(os.path.basename(hex_file))
        replacement_data = read_hex_file(hex_file)
        replace_section(target_file_path, replacement_data, start_position)
