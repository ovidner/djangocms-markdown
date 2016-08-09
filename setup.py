# -*- coding: utf-8 -*-

import io
from setuptools import setup, find_packages


def read(*filenames, **kwargs):
    """
    From http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
    """
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


setup(
    name="djangocms-markdown",
    version='0.3.2',
    description=read('DESCRIPTION'),
    long_description=read('README.md'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, django-cms, plugin, markdown, editor',
    author='Olle Vidner, Nicolas Noé and others.',
    author_email='nicolas@niconoe.eu',
    url="https://github.com/niconoe/djangocms-markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
        'django-cms>=3.0.0',
        'django-markdown-deux',
    ], extras_require = {
        'Django_less_than_17':  ["South>=1.0"]
    }
)
