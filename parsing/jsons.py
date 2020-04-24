# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json


class Json:
    def __init__(self, filename):
        self.filename = os.path.splitext(filename)[0]
        self.format = os.path.splitext(filename)[1]
        with open(filename, "r", encoding="utf-8") as content:
            self.data = json.load(content)

    def sentence(self, tags):
        sentences = len(self.data[tags[0]])
        return [self.data[tags[0]][sentence][tags[1]] for sentence in range(1, sentences)]

    # save files
    def save(self, filename, sentences, format=None):
        format = self.format[1:] if format is None else format
        path = os.getcwd()+"/data/prep"
        if not os.path.isdir(path):
            os.mkdir(path)
        newName = "data/prep/" + self.filename[5:] + "_" + filename + "." + format
        if format == "txt":
            file = open(newName, 'w', encoding="utf-8")
            for sentence in sentences:
                file.write(sentence + "\n")
            file.close()


def json_multi_files():
    path = os.getcwd() + "/data"
    fileList = os.listdir(path)
    filenames = []
    for file in fileList:
        if file[:7] == "edited_":
            filenames.append(file)
    jsons = [Json("data/"+filename) for filename in filenames]
    for json_ in jsons:
        result = json_.sentence(["sentence", "text"])
        json_.save("only_speak", result, "txt")


def json_single_file():
    filename = "data/" + "ko_nia_normal_squad_all.json"
    json_ = Json(filename)
    result = json_.sentence(["sentence", "text"])
    json_.save("only_speak", result, "txt")


if __name__ == "__main__":
    # json_single_file()      # single file
    json_multi_files()      # multi files
