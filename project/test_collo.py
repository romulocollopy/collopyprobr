import collo
import unittest

from collo import MockArticles

class ViewsTestCase(unittest.TestCase):

    def setUp(self):
        collo.app.config['TESTING'] = True
        self.app = collo.app.test_client()

    def test_index_200(self):
        rv = self.app.get('/')
        self.assertEqual(200, rv._status_code)

    def test_index_uses_template(self):
        rv = self.app.get('/')
        assert b'<html lang="pt-br">' in rv.data

    def test_entry_detail(self):
        rv = self.app.get('/articles/mock-applications/')
        self.assertEqual(200, rv._status_code)

    def test_entry_detail_data(self):
        rv = self.app.get('/articles/mock-applications/')
        assert 'Rômulo Collopy'.encode('utf-8') in rv.data

if __name__ == '__main__':
    unittest.main()

