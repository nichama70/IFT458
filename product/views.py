from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views import generic

from .models import Device

def index(request):
    device_list = Device.objects.order_by('-model_number')[:5]
    context = {'device_list': device_list}
    return render(request, 'product/index.html',context)

class DetailView(generic.DetailView):
    model = Device
    template_name = 'polls/detail.html'

def detail(request, device_id):
    device_ins = get_object_or_404(Device, pk=device_id)
    return render(request, 'product/detail.html', {'device':device_ins})

def test_results(request, device_id):
    response = "You're looking at the results of device %s."
    return HttpResponse(response % device_id)

def new_entry(request, device_id):
    device_ins = get_object_or_404(Device, pk=device_id)
    return render(request, 'product/new.html', {'device':device_ins})