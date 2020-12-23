from unittest import TestCase
from auditpol.subcategories import Subcategory


class TestSubcategory(TestCase):
    def test_valid_id(self):
        subcategory = Subcategory(id='{00000000-0000-0000-0000-000000000000}', name='Example')
        self.assertEqual(subcategory.id, '{00000000-0000-0000-0000-000000000000}')

    def test_invalid_id_type(self):
        with self.assertRaises(TypeError):
            Subcategory(id=None, name='Example')

    def test_valid_name(self):
        subcategory = Subcategory(id='{00000000-0000-0000-0000-000000000000}', name='Example')
        self.assertEqual(subcategory.name, 'Example')

    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            Subcategory(id='{00000000-0000-0000-0000-000000000000}', name=None)

    def test_default_description(self):
        subcategory = Subcategory(id='{00000000-0000-0000-0000-000000000000}', name='Example')
        self.assertEqual(subcategory.description, '')

    def test_valid_description(self):
        subcategory = Subcategory(id='{00000000-0000-0000-0000-000000000000}', name='Example', description='Description')
        self.assertEqual(subcategory.description, 'Description')

    def test_invalid_description_type(self):
        with self.assertRaises(TypeError):
            Subcategory(id='{00000000-0000-0000-0000-000000000000}', name='Example', description=None)
