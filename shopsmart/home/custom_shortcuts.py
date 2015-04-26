__author__ = 'himanshu'
from django.template import RequestContext, loader
from django.http import HttpResponse

def render_with_no_context(request, page_name):
    template = loader.get_template(page_name)
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))



def render_with_context(request, page_name, context_dict):
    template = loader.get_template(page_name)
    context = RequestContext(request, context_dict)
    return HttpResponse(template.render(context))

