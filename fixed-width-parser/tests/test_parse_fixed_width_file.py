import unittest
import csv
from fixed_width_parser.generate_fixed_width_file import generate_fixed_width_file
from fixed_width_parser.parse_fixed_width_file import parse_fixed_width_file


class TestParseFixedWidthFile(unittest.TestCase):
    def setUp(self):
        self.spec = [
            ("first_name", 15),
            ("last_name", 15),
            ("address", 30),
            ("date_of_birth", 10),
        ]
        self.data = [("Marta", "Lopez", "12A Francis Road", "1990-01-01")]
        generate_fixed_width_file("data/test_data.txt", self.spec, self.data)

    def test_parse_fixed_width_file(self):
        parse_fixed_width_file("data/test_data.txt", "data/test_output.csv", self.spec)
        with open("data/test_output.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            row = next(reader)
            self.assertEqual(
                header, ["first_name", "last_name", "address", "date_of_birth"]
            )
            self.assertEqual(row, ["Marta", "Lopez", "12A Francis Road", "1990-01-01"])


if __name__ == "__main__":
    unittest.main()
