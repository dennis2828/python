from math import pi
import sys
import random as rdm
from enum import Enum

import test

print(pi)

for item in dir(rdm):
    print(item)

test.test("re")

print(__name__)
print(test.__name__)