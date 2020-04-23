__name__ = 'NLParse'
__description__ = 'parsing natural language files'
__version__ = '0.0.0'
__url__ = 'https://github.com/study-ai-data/nlp-parsings'
__download_url__ = 'https://github.com/study-ai-data/nlp-parsing'
__install_requires__ = [
    "pandas",
    "xlrd",
]
__license__ = 'MIT'


from parsing.texts import *
from parsing.excels import *
from parsing.jsons import *
from parsing.xmls import *
from parsing.texts import *
