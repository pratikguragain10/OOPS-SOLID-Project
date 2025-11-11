"""Module containing the Calculator class to run data extraction and analysis."""

from SOLID.data_extractor import DataExtractor
from SOLID.data_analyzer import DataAnalyzer

class Calculator:
    """Orchestrates the extraction and analysis of data from a file."""

    def __init__(self, filename, col1, col2, label_col):
        """
        Initialize Calculator with a file and column indices.

        Args:
            filename (str): Path to the data file
            col1 (int): First numeric column index
            col2 (int): Second numeric column index
            label_col (int): Label column index
        """
        self.extractor = DataExtractor(filename, col1, col2, label_col)
        self.analyzer = DataAnalyzer()

    def execute(self):
        """
        Run the extraction and analysis workflow.

        Returns:
            tuple: (label_with_min_diff, min_diff)
        """
        data = self.extractor.extract()
        return self.analyzer.find_min_diff(data)
