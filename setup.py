import setuptools
from distutils.core import setup

setup(
    name='Jupyter-Beeper',
    version='1.0',
    author="Jean Yves Beaucamp (@jeanyvesb9)",
    author_email="jeanyvesb9@me.com",
    description="A beep generator for Jupyter Notebooks (and Jupyter-Lab) that doesn't display a reproduction widget.",
    url="https://github.com/jeanyvesb9/Jupyter-Beeper",
    packages=['Beeper'],
    keywords='beep beeper sounds ipython jupyter',
    install_requires=['ipython', 'numpy'],
)
