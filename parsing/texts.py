# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class Text:
    def __init__(self, filename):
        self.filename = os.path.splitext(filename)[0]
        self.format = os.path.splitext(filename)[1]

    def correcting(self):
        return

    def save(self, filename, data):
        path = os.getcwd() + "/data/tgt"
        if not os.path.isdir(path):
            os.mkdir(path)
        # newName = "data/tgt/" + self.filename[]
        print(self.filename[5:])


def text_multi_files():
    filenames = []
    texts = [Text("data/"+filename) for filename in filenames]
    # for text in texts:
    #     text.save("prep1", sentence, "txt")


def text_single_file():
    return


if __name__ == "__main__":
    # text_single_file()
    text_multi_files()
