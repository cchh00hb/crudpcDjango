from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import PC, Composant
from .forms import PCForm, ComposantForm

def liste_pcs(request):
    pcs = PC.objects.all()
    return render(request, 'myapp/liste_pcs.html', {'pcs': pcs})

def detail_pc(request, pc_id):
    pc = get_object_or_404(PC, pk=pc_id)
    composants = pc.composants.all()
    return render(request, 'myapp/detail_pc.html', {'pc': pc, 'composants': composants})

def ajouter_pc(request):
    if request.method == 'POST':
        form = PCForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_pcs')
    else:
        form = PCForm()
    return render(request, 'myapp/form_pc.html', {'form': form})

def modifier_pc(request, pc_id):
    pc = get_object_or_404(PC, pk=pc_id)
    if request.method == 'POST':
        form = PCForm(request.POST, instance=pc)
        if form.is_valid():
            form.save()
            return redirect('liste_pcs')
    else:
        form = PCForm(instance=pc)
    return render(request, 'myapp/form_pc.html', {'form': form})

def supprimer_pc(request, pc_id):
    pc = get_object_or_404(PC, pk=pc_id)
    pc.delete()
    return redirect('liste_pcs')

def ajouter_composant(request, pc_id):
    pc = get_object_or_404(PC, pk=pc_id)
    if request.method == 'POST':
        form = ComposantForm(request.POST)
        if form.is_valid():
            composant = form.save(commit=False)
            composant.pc = pc
            composant.save()
            return redirect('detail_pc', pc_id=pc.id)
    else:
        form = ComposantForm()
    return render(request, 'myapp/form_composant.html', {'form': form, 'pc': pc})
