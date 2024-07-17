from django.http import HttpResponse

# Create your views here.
def index(requests):
    return HttpResponse("Hello, world.")
def some_url(request):
    return HttpResponse("Some url을 구현해 봤습니다.")