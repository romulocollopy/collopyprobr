from datetime import datetime


class MockArticle:

    def __init__(self, articles=None):
        self.articles = articles or {}
        self.prepopulate()

    def prepopulate(self):
        content = {
            'title': 'Trabalhando com o Mock',
            'subtitle': 'O que e onde mockar seus testes',
            'content': '<p>Oi tudo bom?</p>',
            'publish_date': datetime.strptime('2015-09-12', "%Y-%m-%d"),
            'author': 'Rômulo Collopy'
        }
        self.insert_one('mock-applications', content)

    def find(self, key):
        return self.articles.get(key, None)

    def insert_one(self, slug, content=None):
        content = content or {}

        if slug in self.articles.keys():
            raise KeyError('Article already exists')
        self.articles[slug] = content

