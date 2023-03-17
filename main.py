import re


def process_text(input_file, output_file):
    # Open input and output files
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        # Read input file and replace multiple spaces with one
        text = re.sub(r'\s+', ' ', f_in.read())

        # Remove spaces before and after punctuation marks
        text = re.sub(r'\s+([.,!?;])', r'\1', text)
        text = re.sub(r'([.,!?;])(\S)', r'\1 \2', text)

        # Write processed text to output file
        f_out.write(text)


# Example usage
process_text('tests/input_1.txt', 'tests/output_1.txt')
