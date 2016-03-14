from sblog.models import Article, Tag, Classification
from django.template import RequestContext
from django.shortcuts import render_to_response

def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    print blogs
    blog = blogs[0]
    print blog.caption 
    return render_to_response('index.html', {"blogs": blogs}, context_instance=RequestContext(request))
# Create your views here.

