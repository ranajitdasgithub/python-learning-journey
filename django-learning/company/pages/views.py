from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {
        'inventory_list':["Widget 1",'Widget 2','Widget 3'],
        "greeting":"Thank you for visiting our website"
    }
    return render(request, 'homepage.html', context)