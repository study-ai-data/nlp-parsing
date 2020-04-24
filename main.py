# !/usr/bin/env python
# -*- coding: utf-8 -*-

from parsing.excels import excel_single_file, excel_multi_files, excel_civil_complaint
from parsing.jsons import json_single_file, json_multi_files
from parsing.texts import *
from parsing.xmls import *


if __name__ == "__main__":
    """ Excel file """
    excel_single_file()         # single file
    excel_multi_files()         # multi files
    excel_civil_complaint()     # civil complaint

    """ Json file """
    json_single_file()          # single file
    json_multi_files()          # multi files
