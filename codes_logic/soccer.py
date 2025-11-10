"""Find the soccer team with the smallest goal difference using the Calculator class."""

from calculator import Calculator

if __name__ == "__main__":
    TEAM_COLUMN = 1
    GOALS_FOR_COLUMN = 6
    GOALS_AGAINST_COLUMN = 8

    calc = Calculator(
        "../data/football.dat",
        GOALS_FOR_COLUMN,
        GOALS_AGAINST_COLUMN,
        TEAM_COLUMN
    )
    team, diff = calc.execute()
    print(f"Team with smallest goal diff: {team} ({diff})")
