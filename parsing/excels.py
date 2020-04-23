import pandas as pd
import os


class Excel:
    def __init__(self, filename):
        self.filename = os.path.splitext(filename)[0]
        self.format = os.path.splitext(filename)[1]
        if self.format == ".xlsx":
            self.data = pd.read_excel(filename, encoding="utf-8")
        else:  # csv
            self.data = pd.read_csv(filename, encoding="utf-8")

    # show [shape, head, tail, index, columns, values, describe]
    def info(self, kind, cnt=5):
        if kind is "shape":
            print("shape:", self.data.shape)
        elif kind is "head":
            print("head:", self.data.head(cnt))
        elif kind is "tail":
            print("tail:", self.data.tail(cnt))
        elif kind is "index":
            print("index:", self.data.index)
        elif kind is "columns":
            print("columns:\n", self.data.columns)
        elif kind is "values":
            print("values:\n", self.data.values)
        elif kind is "describe" or "desc":
            print("describe:\n", self.data.describe())

    # transpose index and columns
    def transpose(self):
        return self.data.T

    # sorting
    def sort(self, axis=0, ascending=True):
        return self.data.sort_index(axis, ascending)

    # select data
    def select(self, col_name):
        return self.data[col_name]

    # save files
    def save(self, filename, data, format=None):
        format = self.format[1:] if format is None else format
        newName = self.filename + "_" + filename + "." + format
        if format == "txt":
            data.to_csv(newName, index=False, header=None, sep="\n")


if __name__ == "__main__":
    filename = "data/" + "test_xlsx.xlsx"
    excel = Excel(filename)
    sentence = excel.select("SENTENCE")
    excel.save("only_speak", sentence, "txt")
