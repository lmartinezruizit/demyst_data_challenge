
# Problem 1: Parse fixed width file

This project involves generating and parsing fixed-width files and converting them into delimited CSV files. The fields in the fixed-width file include: `first_name`, `last_name`, `address`, and `date_of_birth`.

## Project Structure

```
.
├── Dockerfile
├── README.md
├── data
├── docker-entrypoint.sh
├── docker-compose.yml
├── fixed_width_parser
│   ├── __init__.py
│   ├── generate_fixed_width_file.py
│   └── parse_fixed_width_file.py
├── poetry.lock
├── pyproject.toml
└── tests
    ├── __init__.py
    ├── test_generate_fixed_width_file.py
    └── test_parse_fixed_width_file.py
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Repository

**Clone the repository:**
   ```bash
   git clone https://github.com/lmartinezruizit/demyst_data_challenge.git
   cd fixed-width-parser
   ```

### Local Development with Poetry

1. **Install Poetry:**
   If you haven't already installed Poetry, follow the instructions [here](https://python-poetry.org/docs/).

2. **Install Dependencies:**
   ```bash
   poetry install
   ```

### Docker Compose

1. **Build and Run Containers:**
   Ensure Docker and Docker Compose are installed on your system.
   ```bash
   docker-compose build
   docker-compose up
   ```

## Usage

### Local Development with Poetry

1. **Generate a Fixed-Width File:**
   ```bash
   poetry run python -m fixed_width_parser.generate_fixed_width_file
   ```

2. **Parse the Fixed-Width File:**
   ```bash
   poetry run python -m fixed_width_parser.parse_fixed_width_file
   ```

3. **Run Tests:**
   ```bash
   poetry run pytest
   ```

### Docker Compose

1. **Run Specific Part (Parse by Default):**
   ```bash
   docker-compose run --rm parser
   ```

2. **Run Tests:**
   ```bash
   docker-compose run --rm test
   ```

3. **Full Pipeline (Generate and Parse):**
   ```bash
   docker-compose up

### Data Paths

- Input fixed-width file: `data/data.txt`
- Output delimited file: `data/output.csv`

### Configuration

The configuration for the fixed-width parser, including field widths and output delimiter, is defined in `fixed_width_parser/generate_fixed_width_file.py`.

### Data Volumes

When running the project or tests with `docker-compose`, the results are mounted in the following locations:
- Fixed-width file: `./data/data.txt`
- Parsed CSV file: `./data/output.csv`

## Example

### Input Fixed-Width File (`data.txt`)

```
Marta          Lopez          12A Francis Road              1990-01-01
Bob            Williams       45 Blair St                   1985-05-23
Antonio        Kroos          78 Bondi Road                 1992-12-11
```

### Output Delimited File (`output.csv`)

```
first_name,last_name,address,date_of_birth
Marta,Lopez,12A Francis Road,1990-01-01
Bob,Williams,45 Blair St,1985-05-23
Antonio,Kroos,78 Bondi Road,1992-12-11
```

## Docker Setup

### Dockerfile

The `Dockerfile` sets up the environment using Python 3.12-slim and installs Poetry for dependency management.

### docker-compose.yml

The `docker-compose.yml` file defines two services: `parser` for running the fixed-width file parser and `test` for running the unit tests.

### docker-entrypoint.sh

This script allows for flexible command execution within the Docker container, enabling either parsing or testing based on the provided argument.

## Files and Directories

- **`Dockerfile`**: Defines the Docker image configuration.
- **`docker-compose.yml`**: Manages multi-container Docker applications.
- **`docker-entrypoint.sh`**: Allows for flexible command execution within the Docker container.
- **`fixed_width_parser/generate_fixed_width_file.py`**: Generates a fixed-width file.
- **`fixed_width_parser/parse_fixed_width_file.py`**: Parses the fixed-width file and converts it to CSV.
- **`tests/`**: Contains unit tests for the fixed-width file parser.

## Notes

- Input and output files (`data/data.txt` and `output.csv`) are mounted in the Docker container, allowing for easy access to the processed data.
- Docker and Docker Compose ensure consistency across different environments and simplify dependency management.
