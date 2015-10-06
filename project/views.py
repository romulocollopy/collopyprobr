
from flask import render_template, Blueprint
from models import MockArticle as Article


views = Blueprint('views', __name__, template_folder='templates')


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/articles/<path:post_slug>/')
def entry_detail(post_slug=None):
    articles = Article()
    article = articles.find(post_slug)
    if not article:
        return 'Oops! The article "%s" was not found.'\
                    % post_slug, 404
    return render_template('article_detail.html', article=article)
