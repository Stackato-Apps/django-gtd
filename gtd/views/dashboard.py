from gtd.views import render_response
from gtd.models import Thing, Context, Project
from gtd.utils import query_dict, paginate
from django.shortcuts import get_object_or_404

def dashboard(request):
    status = request.GET.get('status', None)
    context_id = request.GET.get('context', None)
    project_id = request.GET.get('project', None)        
    thing_list = Thing.objects.select_related().filter(deleted=False)

    view_context = dict()

    if status:
        thing_list = thing_list.filter(status=status)
        if int(status) == Thing.STATE_DEFERRED:
            thing_list = thing_list.order_by('schedule')
            
    if context_id:
        context_id = int(context_id)
        context = get_object_or_404(Context, pk=context_id)
        thing_list = thing_list.filter(context=context_id)
        view_context.update({'context': context})

    if project_id:
        project_id = int(project_id)
        project = get_object_or_404(Project, pk=project_id)
        thing_list = thing_list.filter(project=project_id)
        view_context.update({'project': project})
        
    things = paginate(thing_list, request.GET.get('page', None))

    #TODO: Register as a template tag to choose exclude params in template
    query_string = query_dict(request.GET.urlencode(), exclude=('page','context', 'project'))
    
    projects = Project.objects.filter(active=True)
    contexts = Context.objects.all()
    
    view_context.update({
        'things': things,
        'projects': projects,
        'contexts': contexts,
        'query_string': query_string,
        'status': status,
        'project_id': project_id,
        'context_id': context_id
    })
    
    return render_response(request, 'gtd/dashboard.html', view_context)

