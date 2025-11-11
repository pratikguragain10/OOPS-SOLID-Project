"""Module containing DataExtractor class for reading and extracting data from files."""

class DataExtractor:
    """Extracts structured data from space-separated or fixed-width files."""

    def __init__(self, filename: str, col1: int, col2: int, label_col: int):
        """
        Initialize the DataExtractor.

        Args:
            filename (str): Path to the data file
            col1 (int): Index of the first numeric column (1-based)
            col2 (int): Index of the second numeric column (1-based)
            label_col (int): Index of the label column (1-based)
        """
        self.filename = filename
        self.col1 = col1
        self.col2 = col2
        self.label_col = label_col

    def extract(self) -> list[tuple[str, int, int]]:
        """
        Extract data from the file as a list of tuples (label, value1, value2).

        Returns:
            list of tuples: Each tuple contains (label, val1, val2)
        """
        data = []
        with open(self.filename, "r") as f:
            for line in f:
                line = line.strip()
                # Skip empty or header lines
                if not line or line.startswith("Dy") or line.startswith("Team"):
                    continue
                parts = line.split()
                if len(parts) <= max(self.col1, self.col2, self.label_col) - 1:
                    continue
                try:
                    label = parts[self.label_col - 1]
                    val1 = int(parts[self.col1 - 1])
                    val2 = int(parts[self.col2 - 1])
                    data.append((label, val1, val2))
                except ValueError:
                    continue
        return data
