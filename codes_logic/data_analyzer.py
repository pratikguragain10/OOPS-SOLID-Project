"""Module containing DataAnalyzer class for finding minimum differences in datasets."""

class DataAnalyzer:
    """Analyzes data to find the label with the minimum difference between two values."""

    def find_min_diff(self, data: list[tuple[str, int, int]]) -> tuple[str, int]:
        """
        Find the label with the minimum absolute difference between two numeric values.

        Args:
            data (list of tuples): Each tuple is (label, value1, value2)

        Returns:
            tuple: (label_with_min_diff, min_diff)
        """
        min_diff = float("inf")
        label_with_min_diff = None
        for label, val1, val2 in data:
            diff = abs(val1 - val2)
            if diff < min_diff:
                min_diff = diff
                label_with_min_diff = label
        return label_with_min_diff, min_diff
