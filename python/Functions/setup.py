from distutils.core import setup
from Cython.Build import cythonize

setup(name="Functions", ext_modules = cythonize('Functions.pyx'))
