from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("script/mfaeiu3.pyx", 
                              compiler_directives={'language_level' : 3}))
