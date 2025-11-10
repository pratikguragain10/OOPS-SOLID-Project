"""
Find the day with the smallest temperature spread
"""

from calculator import Calculator

if __name__ == "__main__":
    day_col = 1       
    max_temp = 2      
    min_temp = 3      

    calc = Calculator("../data/weather.dat", max_temp, min_temp, day_col)
    day, diff = calc.execute()
    print(f"Day with smallest temperature spread: {day} ({diff})")

