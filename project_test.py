from project import *
import unittest

class TestUS22(unittest.TestCase):
    def test_individual(self):
        self.assertEqual(unique_indiv_id('test_file.ged'), True)

class TestUS42(unittest.TestCase):
    def test_date(self):
        self.assertEqual(date_checker('test_file.ged'), True)

class TestUS29(unittest.TestCase):
    def test_dead(self):
        self.assertEqual(list_deceased('test_file.ged'), False)

class TestUS01(unittest.TestCase):
    def test_date(self):
        self.assertEqual(dates_after_current('test_file.ged'), True)

class TestUS16(unittest.TestCase):
    def test_malelastnames(self):
        self.assertEqual(male_lastname('test_file.ged'), False)

class TestUS18(unittest.TestCase):
    def test_sibs_nomarry(self):
        self.assertEqual(sibs_nomarry('test_file.ged'), True)

class TestUS12(unittest.TestCase):
    def test_parents_notold(self):
        self.assertEqual(parents_notold('test_file.ged'), True)

class TestUS30(unittest.TestCase):
    def test_livingmarried(self):
        self.assertEqual(livingmarried('test_file.ged'), True)