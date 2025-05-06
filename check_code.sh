#!/bin/bash
echo "======== ISORT =========="
isort src tests
echo "======== BLACK =========="
black src tests
echo "======== FLAKE8 =========="
flake8 src tests
echo "======== MYPY =========="
mypy src tests
