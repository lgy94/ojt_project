from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .sens import sens
import urllib.request
import json


# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('-id')
    return render(request, 'home.html', {'blogs': blogs})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})


def create(request):
    return render(request, 'create.html')


def papago(request):
    client_id = "477js80edl"
    client_secret = "hTIBnR5M7d30ZWB9EL5ziZZOhroBOBwbonVOoZFM"
    encText = urllib.parse.quote(request)
    data = "source=ko&target=en&text=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"

    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    response_body = response.read()
    result = response_body.decode('utf-8')
    info = json.loads(result)
    text = info["message"]["result"]["translatedText"]
    return text


def postcreate(request):
    blog = Blog()
    blog.title = papago(request.POST['title'])
    blog.body = papago(request.POST['body'])
    blog.pub_date = timezone.datetime.now()
    blog.save()
    sens(blog.title)
    return redirect('/blog/detail/' + str(blog.id))


def update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method == "POST":
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/detail/' + str(blog.id))
    else:
        return render(request, 'update.html')


def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/blog')
