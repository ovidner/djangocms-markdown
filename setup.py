import os
from setuptools import setup, find_packages
import djangocms_markdown


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="djangocms-markdown",
    version=djangocms_markdown.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, django-cms, plugin, markdown, editor',
    author='Olle Vidner',
    author_email='olle@vidner.se',
    url="https://github.com/ovidner/djangocms-markdown",
    packages=find_packages(),
    include_package_data=True,
)
