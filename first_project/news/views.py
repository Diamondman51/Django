from django.shortcuts import render

# Create your views here.


def all_news(req):
    return render(req, 'index.html')


def one_news(req, num):
    ls = {
        'images': ['https://myrepublica.nagariknetwork.com/uploads/media/dfdfdfdfd_20210928153823.jpg', ]
    }
    return re