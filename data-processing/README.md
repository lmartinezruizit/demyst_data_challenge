# Problem 2: Data processing

This project is responsible for processing the data using PySpark for generating and anonymizing data. It includes scripts for generating random data and anonymizing existing data in CSV format, as well as unit tests to validate the functionality.

## Project Overview

The project is structured as follows:

```
.
├── Dockerfile
├── README.md
├── data_processing
│   ├── __init__.py
│   ├── anonymize_data.py
│   └── generate_data.py
├── docker-compose.yml
└── tests
    ├── __init__.py
    ├── test_anonymize_data.py
    └── test_generate_data.py
```

- **Dockerfile**: Defines the Docker image setup for the project, including the installation of Python 3.9 and PySpark 3.1.2.
- **README.md**: This file provides an overview of the project, setup instructions, and details about scripts and tests.
- **data_processing/**:
  - **anonymize_data.py**: PySpark script to anonymize CSV data by hashing specific columns (`first_name`, `last_name`, `address`) and writing the anonymized data to new CSV files.
  - **generate_data.py**: PySpark script to generate random data in the form of CSV files, including columns for `first_name`, `last_name`, `address`, and `date_of_birth`.
- **docker-compose.yml**: Docker Compose file to orchestrate the execution of Spark jobs (`generate_data.py` and `anonymize_data.py`) followed by running unit tests (`test_anonymize_data.py` and `test_generate_data.py`).
- **tests/**:
  - **test_anonymize_data.py**: Unit tests for `anonymize_data.py`, verifying the presence and content of anonymized CSV files.
  - **test_generate_data.py**: Unit tests for `generate_data.py`, ensuring that generated CSV files exist and contain data.

## Setup Instructions

### Prerequisites

Ensure you have the following installed locally:

- Docker
- Docker Compose

### Building and Running the Project

1. **Build the Docker image**:

   ```bash
   docker-compose build
   ```

   This command prepares the Docker image based on the configuration in `Dockerfile`.

2. **Run the container**:

   ```sh
   docker-compose up
   ```

   This will:
   - Run `generate_data.py` to create CSV files with random data.
   - Run `anonymize_data.py` to anonymize the generated data.
   - Execute unit tests to validate the data processing.

   The results will be mounted in the following directories:
   - `data/output_csv`: Contains the generated data.
   - `data/anonymized_output_csv`: Contains the anonymized data.

## Scripts

### `generate_data.py`

This script creates random data and saves it as CSV files. The dataset includes fields for `first_name`, `last_name`, `address`, and `date_of_birth`.

#### Generating Larger Datasets

To generate a larger dataset, modify the `num_records` parameter:

```python
num_records = 1000000
```

Increase this value to suit your needs, but be mindful of the resources required.

### `anonymize_data.py`

This script reads CSV files, anonymizes the `first_name`, `last_name`, and `address` fields by hashing them, and writes the results to new CSV files.

## Unit Tests

The project includes unit tests to validate the functionality of data generation and anonymization:

- **`test_generate_data.py`**: Tests the functionality of `generate_data.py` to ensure that CSV files are generated and contain data.
- **`test_anonymize_data.py`**: Tests the functionality of `anonymize_data.py` to verify that anonymized CSV files are created and processed correctly.

### Running Tests

Unit tests are executed automatically when starting the Docker container using `docker-compose up`. The test results will be displayed in the terminal.

## Additional Notes

### Spark Configuration

#### Parameters

Spark jobs are configured with the following settings:

- **Executor Memory**: 2GB (`spark.executor.memory=2g`)
- **Executor Cores**: 2 (`spark.executor.cores=2`)
- **Driver Memory**: 1GB (`spark.driver.memory=1g`)
- **Driver Cores**: 1 (`spark.driver.cores=1`)
- **Default Parallelism**: 4 (`spark.default.parallelism=4`)
- **SQL Shuffle Partitions**: 4 (`spark.sql.shuffle.partitions=4`)

#### Details

- **Executor Memory and Cores**: Define resources for each executor, which handles data processing in parallel.
- **Driver Memory and Cores**: Specify resources for the driver, which coordinates the Spark job.
- **Default Parallelism**: Sets the number of partitions for operations like joins and aggregations.
- **SQL Shuffle Partitions**: Controls the number of partitions during data shuffling for joins and aggregations in Spark SQL.

### Python Environment

Python 3.9 is set as the default Python version within the Docker container to ensure compatibility with PySpark 3.1.2 and other dependencies.
