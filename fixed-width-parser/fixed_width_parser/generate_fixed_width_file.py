spec = [("first_name", 15), ("last_name", 15), ("address", 30), ("date_of_birth", 10)]

data = [
    ("Marta", "Lopez", "12A Francis Road", "1990-01-01"),
    ("Bob", "Williams", "45 Blair St", "1985-05-23"),
    ("Antonio", "Kroos", "78 Bondi Road", "1992-12-11"),
]


def generate_fixed_width_file(filename, spec, data):
    with open(filename, "w", encoding="utf-8") as file:
        for record in data:
            line = "".join(
                str(value).ljust(width) for value, (name, width) in zip(record, spec)
            )
            file.write(line + "\n")


generate_fixed_width_file("data/data.txt", spec, data)
