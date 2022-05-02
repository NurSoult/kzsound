"""from django import template
from news.models import *

register = template.Library()


@register.inclusion_tag('news/list_news.html')
def show_news(sort=None, news_selected=0):
    if not sort:
        news = Article.objects.all()
    else:
        news = Article.objects.order_by(sort)

    return {"news2": news, "news_selected": news_selected}

"""