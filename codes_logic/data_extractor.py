class DataExtractor:
    def __init__(self, filename, col1, col2, label_col):
        self.filename = filename
        self.col1 = col1
        self.col2 = col2
        self.label_col = label_col

    def extract(self):
        data = []
        with open(self.filename, "r") as f:
            for line in f:
                line = line.strip()
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

