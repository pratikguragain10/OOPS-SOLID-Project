"""Find the day with the smallest temperature spread using the Calculator class."""

from SOLID.calculator import Calculator

if __name__ == "__main__":
    DAY_COLUMN = 1
    MAX_TEMP_COLUMN = 2
    MIN_TEMP_COLUMN = 3

    calc = Calculator(
        "../data/weather.dat",
        MAX_TEMP_COLUMN,
        MIN_TEMP_COLUMN,
        DAY_COLUMN
    )
    day, diff = calc.execute()
    print(f"Day with smallest temperature spread: {day} ({diff})")
