from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from .models import Module

def index(request):
        
    context = {
        'module_status': get_modules_all_dict(),
    }
    return render(request=request, template_name='index.html', context=context)



def modules(request):
    
    if request.method == 'POST':
        if 'moduleName' in request.POST:
            module = Module.objects.get(name=request.POST['moduleName'])

            # Validation if module exist in db
            if not module:
                messages.error(request, message='Module not found.')
            else:
                if module.status:
                    module.status = False
                else:
                    module.status = True
                module.save()
        elif 'allModules' in request.POST:
            all_modules_new_status = request.POST['allModules']
            if all_modules_new_status in ['ON', 'OFF']:
                if all_modules_new_status == 'ON':
                    new_boolean_value = True
                else:
                    new_boolean_value = False
                for module in Module.objects.all():
                    module.status = new_boolean_value
                    module.save()
                
            else:
                messages.error(request, message=f'Error, incorrect value for "allModules" : {all_modules_new_status}')
        
            # redirecting after changing status for all modules.
            return redirect(reverse('sam_app:index'))
    
    context = {
        'module_status': get_modules_all_dict(),
    }
    return render(request=request, template_name='modules.html', context=context)


def module_create(request):

    if request.method == 'POST':
        new_name = request.POST['moduleName']
        modules = Module.objects.all()
        for mod in modules:
            if mod.name != new_name:
                pass
        if new_name not in [n.name for n in modules]:
        # if all([mod.name != new_name for mod in modules]):
            new_module = Module()
            new_module.name = new_name
            new_module.save()
            messages.success(request, 'New module created')
        else:
            messages.error(request, message=f'Module with this name "{new_name}" already exist.')

        return redirect(reverse('sam_app:modules'))


    context = {
        'module_status': get_modules_all_dict(),
    }
    return render(request=request, template_name='module_create.html', context=context)


'''
Other functions and utilities, non views
'''
def get_modules_all_dict():
    return {module.name: module.status for module in Module.objects.all()}
