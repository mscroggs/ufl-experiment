# -*- coding: utf-8 -*-

from setuptools import setup
import sys

if sys.version_info < (3, 6):
    print("Python 3.6 or higher required, please upgrade.")
    sys.exit(1)

CLASSIFIERS = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
Intended Audience :: Science/Research
License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)
Operating System :: POSIX
Operating System :: POSIX :: Linux
Operating System :: MacOS :: MacOS X
Operating System :: Microsoft :: Windows
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Topic :: Scientific/Engineering :: Mathematics
Topic :: Software Development :: Libraries :: Python Modules
"""

setup(
    name="fenics-ufl",
    description="Unified Form Language",
    author="Martin Sandve Alnæs, Anders Logg",
    author_email="fenics-dev@googlegroups.com",
    url="https://github.com/FEniCS/ufl",
    setup_requires=["setuptools_scm"],
    use_scm_version={"parentdir_prefix_version": "ufl-"},
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
    packages=[
        "ufl",
        "ufl.utils",
        "ufl.finiteelement",
        "ufl.core",
        "ufl.corealg",
        "ufl.algorithms",
        "ufl.formatting",
    ],
    package_dir={"ufl": "ufl"},
    install_requires=["numpy"])
