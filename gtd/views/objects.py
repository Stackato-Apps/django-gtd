from gtd.models import Thing
from django.views.generic.list_detail import object_list, object_detail

def thing_list(request):
    thing_list = Thing.objects.all()
    return object_list(request, queryset=thing_lists)

def thing_detail(request, id):
    thing_detail = Thing.objects.get(id)
    return object_detail(request, queryset=thing_detail)

def context_list(request):
    context_list = Context.objects.all()
    return object_list(request, queryset=context_lists)

def context_detail(request, id):
    context_detail = Context.objects.get(id)
    return object_detail(request, queryset=context_detail)

def project_list(request):
    project_list = Project.objects.all()
    return object_list(request, queryset=project_lists)

def project_detail(request, id):
    project_detail = Project.objects.get(id)
    return object_detail(request, queryset=project_detail)
