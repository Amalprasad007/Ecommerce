from .models import User,categorys
def categories(request):
    return {
        'categories': categorys.objects.filter(catsts="1")
    }