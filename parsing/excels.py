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
        path = os.getcwd()+"/data"
        if not os.path.isdir(path+"/prep"):
            os.mkdir(path+"/prep")
        newName = "data/prep/" + self.filename[5:] + "_" + filename + "." + format
        if format == "txt":
            data.to_csv(newName, index=False, header=None, sep="\n")


def multi_files(filenames):
    excels = [Excel("data/"+filename) for filename in filenames]
    for excel in excels:
        sentence = excel.select("SENTENCE")
        excel.save("only_speak", sentence, "txt")


if __name__ == "__main__":
    # single file
    filename = "data/" + "test_xlsx.xlsx"
    excel = Excel(filename)
    sentence = excel.select("SENTENCE")
    excel.save("only_speak", sentence, "txt")

    # multi files
    # filenames = ["A 음식점(15,726).xlsx", "B 의류(15,826).xlsx", "C 학원(4,773).xlsx",
    #              "D 소매점(14,949).xlsx", "E 생활서비스(11,087).xlsx", "F 카페(7,859).xlsx",
    #              "G 숙박업(7,113).xlsx", "H 관광여가오락(4,949).xlsx"
    #              ]
    # multi_files(filenames)
