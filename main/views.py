import random

from django.shortcuts import render

# # Create your views here.
from django.views.generic import ListView
from .models import Electronic, Product, Category

class Index(ListView):

    model = Electronic
    template_name = 'main/index.html'
    context_object_name = 'electronic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number'] = '<script>alert("Danger!");</script>'
        context['number1'] = random.randrange(1, 100)
        return context

class Home_page(ListView):
    model = Product
    template_name = 'main/home.html'
    context_object_name = 'product'

def dtl_view(request):

    category = Category.objects.all()
    prod = Product.objects.all()
    context={'category' : category}
    return  render(request,'main/home.html', context)

def index_api(request):
    return render(request, 'main/index_api')

@api_view(['GET','POST'])
def golubi(request):
    golubis = Golubi.objects.all()
    if request.method=='POST':
        serializer =GolubiSeriolizer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data)
    return Response(data.data)

