from django.shortcuts import get_object_or_404, redirect, render

from menu.models.menu_model import MenuModel
from menu.forms import MenuForm

# Create your views here.
def menu_list(request):
    search_field= request.GET.get('search')
    if search_field :
        menu = MenuModel.objects.filter(id__icontains=search_field)
        context = {
            'menus': menu,
            'search_field':search_field,
        }
    else:    
        menu= MenuModel.objects.all()
        context = {
            'menus': menu,
        }
             
    return render(request, 'menu/menus.html', context)

def menu_create(request):
    if request.method == 'POST':
     form = MenuForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('menu:menulist')
    else:
       form = MenuForm()
    return render(request, 'forms.html', {'form': form})

def modifier_menu(request, id):
   menu = get_object_or_404(MenuModel, id=id)
   if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu:menulist')
   else:
        form = MenuForm(instance=menu)
   return render(request, 'forms.html', {'form': form})

def supprimer_menu(request, id):

    menu = get_object_or_404(MenuModel, id=id)
    menu.delete()
    return redirect('menu:menulist')