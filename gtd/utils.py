from django.http import QueryDict
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def query_dict(querystring, exclude):
    qdict = QueryDict(querystring).copy()
    query_string = str()

    if type(exclude) != tuple:
        raise Exception("exclude must be a tuple")

    for item in exclude:
        if item in qdict:
            qdict.pop(item)

    query_dict_urlencode = qdict.urlencode() 

    if query_dict_urlencode != '':
        query_string = query_dict_urlencode + "&"

    query_string.replace('&', '&amp;')

    return query_string
    
def paginate(obj, page, per_page=12):
    paginator = Paginator(obj, per_page)
    
    if not page:
        page = 1

    try:
        object_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        object_list = paginator.page(paginator.num_pages)

    return object_list
