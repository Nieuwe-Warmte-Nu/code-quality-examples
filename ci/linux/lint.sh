#!/usr/bin/env sh

. .venv/bin/activate
flake8 ./src/code_quality_examples
pylint ./src/code_quality_examples
