import pytest
from .. import main

class MockArticles:
    articles = {}

    def prepopulate(self):
        self.articles['mock-applications'] = {
            'title': 'Trabalhando com o Mock',
            'subtitle': 'O que e onde mockar seus testes',
            'content': '<p>Oi tudo bom?</p>',
            'publish_date': datetime.strptime('2015-09-12', "%Y-%m-%d"),
            'author': 'Rômulo mainpy'
        }

    def find(self, key):
        return self.articles.get(key, None)

    def insert_one(self, slug, content=None):
        content = content or {}

        if slug in self.articles.keys():
            raise KeyError('Article already exists')
        self.articles[slug] = content

class TestViews:

    @pytest.fixture
    def app(self):
        main.app.config['TESTING'] = True
        return main.app.test_client()

    def test_index_200(self, app):
        rv = app.get('/')
        assert 200 == rv._status_code

    def test_index_uses_template(self, app):
        rv = app.get('/')
        assert b'<html lang="pt-br">' in rv.data

    def test_entry_detail(self, app):
        rv = app.get('/articles/mock-applications/')
        assert 200 == rv._status_code

    def test_entry_detail_data(self, app):
        rv = app.get('/articles/mock-applications/')
        assert 'Rômulo mainpy'.encode('utf-8') in rv.data

