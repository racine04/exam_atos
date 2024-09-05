from django.shortcuts import get_object_or_404, redirect, render

from plat.models.plat_model import PlatModel
from plat.forms import PlatForm

# Create your views here.
def plat_list(request):
    search_field= request.GET.get('search')
    if search_field :
        plat = PlatModel.objects.filter(name__icontains=search_field)
        context = {
            'plats': plat,
            'search_field':search_field,
        }
    else:    
        plat= PlatModel.objects.all()
        context = {
            'plats': plat,
        }
    return render(request, 'plat/plats.html', context)

def plat_create(request):
    if request.method == 'POST':
     form = PlatForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('plat:platlist')
    else:
       form = PlatForm()
    return render(request, 'forms.html', {'form': form})

def modifier_plat(request, id):
   plat = get_object_or_404(PlatModel, id=id)
   if request.method == 'POST':
        form = PlatForm(request.POST, instance=plat)
        if form.is_valid():
            form.save()
            return redirect('plat:platlist')
   else:
        form = PlatForm(instance=plat)
   return render(request, 'forms.html', {'form': form})

def supprimer_plat(request, id):

    plat = get_object_or_404(PlatModel, id=id)
    plat.delete()
    return redirect('plat:platlist')