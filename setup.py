#!/usr/bin/env python
from setuptools import setup, find_packages
import parsing

"""
해당 패키지는 pypi에 업로드 하지 않을 것임!
"""

setup(name=parsing.__name__,
      description=parsing.__description__,
      version=parsing.__version__,
      author=['Kyeongnam Kim'],
      author_email=['devokkn@gmail.com'],
      url=parsing.__url__,
      install_requires=parsing.__install_requires__,
      license=parsing.__license__,
      long_description=open('./README.md', 'r', encoding='utf-8').read(),
      long_description_content_type="text/markdown",
      packages=find_packages(),
      classifiers=[
            'Programming Language :: Python :: 3',
      ]
      )
