from django.shortcuts import render


# Create your views here.
def home_page(request):
    # content.search_bar.enabled

    content = {
        'search_bar': True
    }
    return render(request, 'pages/home/index.html',)
