import csv
from fixed_width_parser.generate_fixed_width_file import spec


def parse_fixed_width_file(input_filename, output_filename, spec):
    with open(input_filename, "r", encoding="utf-8") as infile, open(
        output_filename, "w", newline="", encoding="utf-8"
    ) as outfile:
        writer = csv.writer(outfile)
        writer.writerow([name for name, width in spec])
        for line in infile:
            record = []
            start = 0
            for name, width in spec:
                record.append(line[start : start + width].strip())
                start += width
            writer.writerow(record)


parse_fixed_width_file("data/data.txt", "data/output.csv", spec)
