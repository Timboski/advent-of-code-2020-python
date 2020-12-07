#!/bin/bash

echo "Run the unit tests"
python -m unittest discover -v test

echo "Checking flake8 compliance"
flake8 advent2020 test

echo "Checking yapf formatting"
yapf -d -r advent2020 test