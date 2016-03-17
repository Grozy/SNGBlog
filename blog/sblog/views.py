from sblog.models import Article, Tag, Classification, Author
from django.template import RequestContext
from django.shortcuts import render_to_response
from markdown import markdown

def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    for post in blogs:
        post.content = markdown(post.content, extensions=['markdown.extensions.extra'])

    classifications = Classification.objects.all()
    number_of_blogs = len(blogs)

    params = {}

    params['classifications'] = classifications

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

    return render_to_response('index.html', params, context_instance=RequestContext(request))
# Create your views here.

