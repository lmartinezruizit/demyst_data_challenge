# Use an official Python runtime as a parent image
FROM python:3.12-slim


# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the project dependencies
RUN poetry install

# Default command to run (override with environment variable)
CMD ["poetry", "run", "python", "-m", "fixed_width_parser.parse_fixed_width_file"]

# Set entrypoint script to choose between parse and test
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]