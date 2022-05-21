#from setuptools import setup
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("mfaeiu4.pyx", 
                              compiler_directives={'language_level' : 3}))