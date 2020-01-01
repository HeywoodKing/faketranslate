# -*- encoding: utf-8 -*-
"""
@File           : setup.py
@Time           : 2019/12/30 21:46
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : faketranslate
@description    : 描述
"""
from __future__ import with_statement
import sys
from codecs import open

if sys.version_info < (2, 5):
    sys.exit('Python 2.5 or greater is required.')

import os
import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# with open(os.path.join(BASE_DIR, 'faketranslate', 'metadata.py')) as f:
#     meta_file = f.read()
# # 读取metadata.py文件内容
# md = dict(re.findall(r"__([a-z]+)__\s*=\s*'([^']+)'", meta_file))

# with open(os.path.join(BASE_DIR, 'README.md'), 'r', encoding='utf-8') as f:
#     long_description = f.read()


try:
    from pypandoc import convert


    def read_md(f):
        return convert(f, 'rst')
except ImportError:
    convert = None
    print('warning:pypandoc not found')

README = os.path.join(os.path.dirname(__file__), 'README.md')


def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return '.'.join(map(str, version_tuple[:-1])) + version_tuple[-1]

    return '.'.join(map(str, version_tuple))


init = os.path.join(os.path.dirname(__file__), 'faketranslate', '__init__.py')

version_line = list(
    filter(lambda l: l.startswith("VERSION"), open(init))
)[0]

VERSION = get_version(eval(version_line.split('=')[-1]))

setup(
    name='fake-translate',
    version=VERSION,
    description='An efficient and practical translation tool',
    long_description=read_md(README),
    long_description_content_type='text/markdown',
    author='hywell',
    author_email='opencoding@hotmail.com',
    maintainer='hywell',
    maintainer_email='opencoding@hotmail.com',
    url='https://github.com/HeywoodKing/faketranslate',
    download_url='https://github.com/HeywoodKing/faketranslate',
    license='AGPLv3+',
    keywords='python translate',
    project_urls={
        'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
        'Funding': 'https://donate.pypi.org',
        'Source': 'https://github.com/pypa/sampleproject/',
        'Tracker': 'https://github.com/pypa/sampleproject/issues',

    },
    # py_modules=['faketranslate'],
    # packages=['faketranslate'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    platforms=["all"],
    install_requires=[
        'requests>=2.22.0',
        'fake_useragent>=0.1.11',
    ],
    python_requires='>=2.6',
    zip_safe=False,
    include_package_data=True,
    # entry_points={
    #     'console_scripts': [
    #         'faketranslate=faketranslate:main'
    #     ],
    # },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
)
