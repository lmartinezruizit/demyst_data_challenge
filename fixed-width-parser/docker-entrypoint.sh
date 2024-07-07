#!/bin/bash

set -e

if [ "$1" = 'test' ]; then
    # Run tests
    poetry run pytest
elif [ "$1" = 'parse' ]; then
    # Run parse script
    poetry run python -m fixed_width_parser.parse_fixed_width_file
else
    # Default to parse script if no argument provided
    poetry run python -m fixed_width_parser.parse_fixed_width_file
fi
