from django.shortcuts import render, get_object_or_404, redirect
from .models import Zone, Category
from .forms import ZoneForm

def zone_list(request):
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    zones = Zone.objects.filter(is_active=True).order_by('title')
    if query:
        zones = zones.filter(title__icontains=query)
    if category_slug:
        zones = zones.filter(category__slug=category_slug)
    categories = Category.objects.all()
    return render(request, 'catalog/zone_list.html', {
        'zones': zones,
        'query': query,
        'categories': categories,
        'selected_category': category_slug,
    })

def zone_detail(request, pk):
    zone = get_object_or_404(Zone, pk=pk)
    return render(request, 'catalog/zone_detail.html', {'zone': zone})

def zone_add(request):
    if request.method == 'POST':
        form = ZoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('zone_list')
    else:
        form = ZoneForm()
    return render(request, 'catalog/zone_form.html', {'form': form})

def about(request):
    return render(request, 'catalog/about.html')