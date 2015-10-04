#!/usr/bin/env python

from datetime import datetime

from flask import Flask
from flask import render_template

from flask.ext.pymongo import PyMongo


app = Flask('collopyprobr')
db = PyMongo(app)

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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/articles/<path:post_slug>/')
def entry_detail(post_slug=None):
    articles = MockArticles()
    articles.prepopulate()
    article=articles.find(post_slug)
    if not article:
        return 'Oops! The article "%s" was not found.'\
                    % post_slug, 404
    return render_template('article_detail.html', article=article)

if __name__ == '__main__':
    app.debug = True
    app.run()
