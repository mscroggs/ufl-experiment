# flake8: noqa
"""This module defines the UFL finite element classes."""

# Copyright (C) 2008-2016 Martin Sandve Alnæs
#
# This file is part of UFL (https://www.fenicsproject.org)
#
# SPDX-License-Identifier:    LGPL-3.0-or-later
#
# Modified by Kristian B. Oelgaard
# Modified by Marie E. Rognes 2010, 2012
# Modified by Andrew T. T. McRae 2014
# Modified by Lawrence Mitchell 2014

from .finiteelementbase import FiniteElementBase
from .finiteelement import FiniteElement
from .mixedelement import MixedElement, VectorElement, TensorElement
from .enrichedelement import EnrichedElement, NodalEnrichedElement

# Export list for ufl.classes
__all_classes__ = [
    "FiniteElementBase",
    "FiniteElement",
    "MixedElement",
    "VectorElement",
    "TensorElement",
]
