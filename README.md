## Data Munging (OOP & SOLID Principles)

## Project Overview

This repository contains Python scripts that apply Object-Oriented Programming (OOP) and SOLID design principles to solve the classic Data Munging Problem from CodeKata.

- The goal is to analyze structured text data and extract insights such as:

    - The day with the smallest temperature spread (Weather data)

    - The team with the smallest goal difference (Soccer data)

- All code is written with simplicity and modularity in mind.

- Each class follows the Single Responsibility Principle (SRP) — handling one task only (data extraction, analysis, or orchestration).

- The project uses only built-in libraries for data parsing (no pandas or NumPy).


## Installation & Requirements

- Install Python 3.10+
- Install dependencies:
- pip install -r requirements.txt

## How to Run

- Run from the project root:

- Example: Weather data analysis
- python weather.py

- Example: Soccer data analysis
- python soccer.py


- Both scripts print the result in the console (e.g., the day or team with the smallest difference).

## All scripts follow this structure:

- extract() → Reads and filters data

- analyze() → Finds minimum difference

- execute() → Runs the complete workflow

## Notes & Best Practices

- .gitignore prevents tracking of data files, cache, and virtual environments

- requirements.txt contains only standard dependencies (no heavy packages)

- Code passes flake8/pylint and follows Python best practices

- All computation happens during file reading — no unnecessary data storage

- Readable variable names (no single-letter identifiers)

- Fully modular and easy to extend for new datasets