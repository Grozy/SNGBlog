from sblog.models import Article, Tag, Classification, Author
from django.template import RequestContext
from django.shortcuts import render_to_response

import os
from blog.settings import BASE_DIR

def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    number_of_blogs = len(blogs)
    params = {}

    print(os.path.join(BASE_DIR, "static/"))

    if number_of_blogs > 0:
        blog = blogs[0]
        params['newest'] = blog
        params['others'] = []



        if number_of_blogs > 1:
            other_blogs = blogs[1:]

            idx = 0
            rows = []
            col = []
            for a_blog in other_blogs:
                if idx % 2 == 0 and idx != 0:
                    rows.append(col)
                    col = []

                if other_blogs[-1:][0] == a_blog:
                    rows.append(col)

                col.append(a_blog)
                idx += 1

            params['others'] = rows


    print(params)
    return render_to_response('index.html', params, context_instance=RequestContext(request))
# Create your views here.

