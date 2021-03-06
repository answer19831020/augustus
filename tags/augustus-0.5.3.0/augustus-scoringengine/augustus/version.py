#!/usr/bin/env python

# Copyright (C) 2006-2011  Open Data ("Open Data" refers to
# one or more of the following companies: Open Data Partners LLC,
# Open Data Research LLC, or Open Data Capital LLC.)
#
# This file is part of Augustus.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Augustus Version
__version__ = '0.5.3.0'

def _python_check():
    """Checks for a minimum and maximum Python version that is required for Augustus."""
    import sys
    if sys.version_info < (2,5):
        print "ERROR: Augustus requires at least Python 2.5"
        sys.exit()
    elif sys.version_info[0] >= 3:
        print "ERROR: Augustus does not run under Python 3.x"
        sys.exit()

