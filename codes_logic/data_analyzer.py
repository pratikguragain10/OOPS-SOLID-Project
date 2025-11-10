class DataAnalyzer:
    def find_min_diff(self, data):
        min_diff = float("inf")
        label_with_min_diff = None
        for label, val1, val2 in data:
            diff = abs(val1 - val2)
            if diff < min_diff:
                min_diff = diff
                label_with_min_diff = label
        return label_with_min_diff, min_diff


