import setuptools
from distutils.core import setup
from os import path 

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Jupyter-Beeper',
    version='1.0.1',
    author="Jean Yves Beaucamp (@jeanyvesb9)",
    author_email="jeanyvesb9@me.com",
    description="A beep generator for Jupyter Notebooks (and Jupyter-Lab) that doesn't display an audio reproduction widget.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/jeanyvesb9/Jupyter-Beeper",
    packages=['jupyter_beeper'],
    keywords='beep beeper sounds ipython jupyter',
    install_requires=['ipython', 'numpy'],
)
