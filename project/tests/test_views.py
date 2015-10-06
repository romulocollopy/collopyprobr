import pytest
from .. import main


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
        assert 'Rômulo Collopy'.encode('utf-8') in rv.data

