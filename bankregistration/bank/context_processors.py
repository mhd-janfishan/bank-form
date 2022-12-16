from .models import Districts

def menu_links(request):
    links=Districts.objects.all()
    return dict(links=links)
