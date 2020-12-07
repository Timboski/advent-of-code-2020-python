#!/bin/bash

echo "Run the unit tests"
if ! python -m unittest discover -v test; then
  echo "Error: Unit Tests Failed"
  exit 1
fi

echo "Checking flake8 compliance"
if ! flake8 advent2020 test; then
  echo "Error: Code fails flake8 compliance"
  exit 2
fi

echo "Checking yapf formatting"
if ! yapf -d -r advent2020 test; then
  echo "Error: Code not yapf formatted correctly"
  exit 3
fi
