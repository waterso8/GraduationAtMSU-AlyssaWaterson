
# coding: utf-8

# In[ ]:


import unittest
import pandas as pd
from dataframetest import dftest

class TestStringInt(unittest.TestCase):
    def test_types(self):
        self.assertRaises(TypeError, dftest, str)

