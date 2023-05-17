from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Module

def index(request):

    modules_dictionary = {}
    for module in Module.objects.all():
        modules_dictionary.update({module.name: module.status})

    context = {
        'module_status': modules_dictionary,
    }
    return render(request=request, template_name='index.html', context=context)



def modules(request):
    modules_dictionary = {}
    for module in Module.objects.all():
        modules_dictionary.update({module.name: module.status})

    context = {
        'module_status': modules_dictionary,
    }
    return render(request=request, template_name='modules.html', context=context)


def module_create(request):

    if request.method == 'POST':
        new_module = Module()
        new_module.name = request.POST.get('moduleName', '')
        new_module.save()
        return redirect('/modules')

    modules_dictionary = {}

    context = {
        'module_status': modules_dictionary,
    }
    return render(request=request, template_name='module_create.html', context=context)