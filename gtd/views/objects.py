from gtd.models import Thing
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def thing_list(request):
    thing_list = Thing.objects.all()
    return ListView(request, queryset=thing_lists)

def thing_detail(request, id):
    thing_detail = Thing.objects.get(id)
    return DetailView(request, queryset=thing_detail)

def context_list(request):
    context_list = Context.objects.all()
    return ListView(request, queryset=context_lists)

def context_detail(request, id):
    context_detail = Context.objects.get(id)
    return DetailView(request, queryset=context_detail)

def project_list(request):
    project_list = Project.objects.all()
    return ListView(request, queryset=project_lists)

def project_detail(request, id):
    project_detail = Project.objects.get(id)
    return DetailView(request, queryset=project_detail)
