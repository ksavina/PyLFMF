from setuptools import setup

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir

import sys

__version__ = "1.0"

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

ext_modules = [
    Pybind11Extension("PyLFMF",
        ["src/PyLFMF/src/main.cpp", "src/PyLFMF/src/Airy.cpp", "src/PyLFMF/src/FlatEarthCurveCorrection.cpp",
        "src/PyLFMF/src/LFMF.cpp", "src/PyLFMF/src/ResidueSeries.cpp", "src/PyLFMF/src/ValidateInputs.cpp",
        "src/PyLFMF/src/WiRoot.cpp", "src/PyLFMF/src/werf.cpp"],
        define_macros = [('VERSION_INFO', __version__)],
        ),
]

setup(
    name="PyLFMF",
    version=__version__,
    author="Kirill Savina & Daniel Sherstnev",
    author_email="ksavina@nes.ru",
    url="https://github.com/ksavina/PyLFMF/",
    description="A wrapper for NTIA/LFMF's groundwave propagarion tool",
    long_description="",
    ext_modules=ext_modules,
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)
