# Calculator System

A modular command-line calculator application built in Python.

This project follows clean architecture, error handling, unit testing, 100% coverage, and GitHub Actions CI.

---

## Features

- REPL interface
- Addition, Subtraction, Multiplication, Division
- Input validation
- Error handling
- LBYL and EAFP approach
- CalculationFactory pattern
- History of calculations
- Commands: help, history, exit
- Unit testing with pytest
- 100% test coverage
- GitHub Actions automation

---

## Project Structure

calculator-system
app
calculator
calculation
operation
tests
.github
requirements.txt
README.md

---

## Setup

1. Clone repository

git clone https://github.com/bt326/calculator-system.git
cd calculator-system

2. Create virtual environment

python -m venv venv
source venv/bin/activate

Windows:
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

---

## Run Application

python -m app.main

---

## Use Calculator

Commands:

add
sub
mul
div
history
help
exit

Example:

add
Enter first number: 5
Enter second number: 3
Result: 8

---

## Run Tests

python -m pytest --cov=app

Coverage is maintained at 100%.

---

## Continuous Integration

GitHub Actions automatically runs tests and checks coverage on every push.

---


