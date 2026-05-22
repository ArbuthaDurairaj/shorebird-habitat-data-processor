# File: test_shorebird_manager.py
# Author: Arbutha Durairaj
# Course: CST8002 – Programming Language Research
# Professor: Stanley Pieda
# Due date: 29 March 2026
# Description: Unit tests for the ShorebirdManager class to verify
# CRUD functionality within the Business layer.
#
#
# References:
#
#[6] Python Software Foundation, "unittest — Unit testing framework," Python 3 Documentation, 2026. [Online]. 
# Available: https://docs.python.org/3/library/unittest.html. [Accessed 6 February 2026].
#
#

"""
Unit Testing Module - ShorebirdManager

This module verifies the correctness of Business layer
operations using Python's built-in unittest framework.
"""

import unittest
from src.business.shorebird_manager import ShorebirdManager
from src.model.shorebird_record import ShorebirdRecord
from src.persistence.sqlite_repository import get_connection

class TestShorebirdManager(unittest.TestCase):

    """
    Test cases for validating CRUD operations
    in the ShorebirdManager class.
    """
    @classmethod
    def setUpClass(cls):
        print("\nUnit tests executed by Arbutha Durairaj")

    def setUp(self):
        """
        Initializes a new ShorebirdManager instance
        before each test to ensure isolation.
        """
        self.manager = ShorebirdManager()
        
        # CLEAR TABLE before each test
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM shorebirds")
        conn.commit()
        conn.close()
        
        # Refresh in-memory records
        self.manager.records = []

    def test_create_record(self):
        """
        Verifies that a record can be successfully added
        to the manager.
        """

        self.manager.create_record("S1", "A1", "2020-01-01", "10:00", "BCDO", 5)
        self.assertEqual(len(self.manager.get_all()), 1)

    def test_delete_record(self):
        """
        Verifies that a record can be successfully deleted
        from the manager.
        """
        
        self.manager.create_record("S1", "A1", "2020-01-01", "10:00", "BCDO", 5)
        self.manager.delete_record(0)

        self.assertEqual(len(self.manager.get_all()), 0)

    def test_update_record(self):
        """
        Verifies that an existing record can be updated
        correctly within the manager.
        """
        self.manager.create_record("S1", "A1", "2020-01-01", "10:00", "BCDO", 5)
        updated = self.manager.build_record("S2", "A2", "2020-02-01", "11:00", "ABCD", 10)
        self.manager.update_record(0, updated)


        self.assertEqual(self.manager.get_all()[0].site_id, "S2")
        self.assertEqual(self.manager.get_all()[0].area, "A2")

if __name__ == "__main__":
    unittest.main()
