"""
Find soccer team with smallest goal difference
"""

from calculator import Calculator

if __name__ == "__main__":
    team_col = 1       
    goals_for = 6
    goals_against = 8

    calc = Calculator("../data/football.dat", goals_for, goals_against, team_col)
    team, diff = calc.execute()
    print(f"Team with smallest goal diff: {team} ({diff})")
