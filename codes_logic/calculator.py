from data_extractor import DataExtractor
from data_analyzer import DataAnalyzer

class Calculator:
    def __init__(self, filename, col1, col2, label_col):
        self.extractor = DataExtractor(filename, col1, col2, label_col)
        self.analyzer = DataAnalyzer()

    def execute(self):
        data = self.extractor.extract()
        return self.analyzer.find_min_diff(data)


