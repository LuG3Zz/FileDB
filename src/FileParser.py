import csv

DATA_FORMAT_CSV = "csv"


def csvToRowSet(filepath):
    with open(filepath, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            for cell in row:
                cells = Cell("str", "100", cell)
            print(row)
        rows = Row(cells)

    return RowSet(rows)

class TableDef:
    def __init__(self,name,) -> None:
        self.name = name

class Cell:
    def __init__(self, type, size, val) -> None:
        self.type = type
        self.size = size
        self.val = val


class Row:
    def __init__(self, cells) -> None:
        self.cells = cells


class RowSet:
    def __init__(self, rows) -> None:
        self.rows = rows


class DatabaseEngine:
    def __init__(self) -> None:
        pass

    def readTableFromFile(self, filepath, format=DATA_FORMAT_CSV):
        if format == DATA_FORMAT_CSV:
            return csvToRowSet(filepath)
        # elif format == DATA_FORMAT_JSON:
        #     return jsonToRowSet(filepath)


# 创建和存储数据
def create():
    def __init__(self):
        pass


if __name__ == "__main__":
    csvToRowSet("./test.csv")
