import unittest
from fixed_width_parser.generate_fixed_width_file import generate_fixed_width_file


class TestGenerateFixedWidthFile(unittest.TestCase):
    def setUp(self):
        self.spec = [
            ("first_name", 15),
            ("last_name", 15),
            ("address", 30),
            ("date_of_birth", 10),
        ]
        self.data = [("Marta", "Lopez", "12A Francis Road", "1990-01-01")]
        self.expected_line = (
            "Marta          Lopez          12A Francis Road              1990-01-01\n"
        )

    def test_generate_fixed_width_file(self):
        generate_fixed_width_file("data/test_data.txt", self.spec, self.data)
        with open("data/test_data.txt", "r", encoding="utf-8") as file:
            self.assertEqual(file.readline(), self.expected_line)


if __name__ == "__main__":
    unittest.main()
