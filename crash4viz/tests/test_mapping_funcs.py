"""Unit tests for ensuring elements of the data are loaded correctly.
Run these tests from the top-most directory of the WAcrashviz package."""

import unittest
import os
import inspect
import sys
CURRENTDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENTDIR = os.path.dirname(CURRENTDIR)
PARENT = os.path.dirname(PARENTDIR)
sys.path.insert(0, PARENT)
from crash4viz import mapping_funcs
import warnings

class TestMappingFuncs(unittest.TestCase):
    """Tests to ensure that basic components of the framework is being
    loaded correctly and paths are pointed to the right places."""

    def setUp(self):
        """Disable pandas dtype warning."""

        warnings.simplefilter('ignore')

    def test_clean_dataframe(self):
        """Test that the dataframe has been wrangled correctly."""

        year = '2013'
        data = mapping_funcs.read_dataframe(year)

        num_columns = 22

        self.assertEqual(len(data.columns), num_columns,
                         "Dataframe not wrangled correctly")

    def test_paths(self):
        """Test that the paths defined in the module that direct to important
        resources is correct."""

        self.assertRegex(mapping_funcs.PACKAGE_DIR, 'crash4viz',
                         "Path to crash4viz module is incorrect")

        self.assertRegex(mapping_funcs.MAPS_DIR, '/outputs',
                         "Maps are not being saved in MyMaps directory")

        self.assertRegex(mapping_funcs.DATA_DIR, '/crash-merged',
                         "Path to HSIS crash data is incorrect")

if __name__ == '__main__':
    unittest.main()
