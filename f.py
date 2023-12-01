import os
import sys
import tensorflow as tf
from sys import stdout
from sklearn.preprocessing import LabelEncoder

# Function to count lines in a file
def count_lines(file_path):
    count = 0
    with open(file_path) as file:
        for _ in file:
            count += 1
    return count


def output_table(header, data):
    pad_size = 15
    print(f'{header:<{pad_size}} | {data:<{pad_size}}')


def process_directory(root_directory):
    extension_count = {}
    total_lines = 0

    for root, _, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
            _, file_extension = os.path.splitext(file_path)

            if file_extension in extension_count:
                extension_count[file_extension] += count_lines(file_path)
            else:
                extension_count[file_extension] = count_lines(file_path)

    print('\nFILE TYPE'.ljust(15), '| LINE COUNT'.ljust(15))
    print('-' * 32)

    for extension, lines_count in extension_count.items():
        output_table(extension, lines_count)
        total_lines += lines_count

    output_table('TOTAL', total_lines)

if len(sys.argv) < 2:
    print("Please provide the root directory as a command line argument.")
    sys.exit(1)

process_directory(sys.argv[1])
