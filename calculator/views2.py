from django.views import generic

class CalculatorView(generic.TemplateView):
    template_name="calculator.html"

#CRUD Views
#Create read, update ,delete
from calculator.models import CalculatorHistory
from django.urls import reverse_lazy

class CalculatorCreateView(generic.CreateView):
    template_name="common/form.html"
    queryset=CalculatorHistory.objects.all()
    fields="__all__"
    success_url=reverse_lazy("calc-list")

    def get_context_data(self, **kwargs):
        data= super().get_context_data(**kwargs)
        data.update(
            title="Create New Calculator History "
        )
        return data

class CalculatorReadView(generic.ListView):
    template_name="calculator/index.html"
    queryset=CalculatorHistory.objects.all()
    context_object_name="objects"
    # default="object_list"

    def get_context_data(self, **kwargs):
        data= super().get_context_data(**kwargs)
        data.update(
            title=" All Calculator history "
        )
        return data

class CalculatorUpdateView(generic.UpdateView):
    template_name="common/form.html"
    queryset=CalculatorHistory.objects.all()
    fields="__all__"
    success_url = reverse_lazy("calc-list")

    def get_context_data(self, **kwargs):
        data= super().get_context_data(**kwargs)
        data.update(
            title="Update Calculator history "
        )
        return data

class CalculatorDeleteView(generic.DeleteView):
    template_name="common/form.html"
    queryset=CalculatorHistory.objects.all()
    success_url = reverse_lazy("calc-list")

    def get_context_data(self, **kwargs):
        data= super().get_context_data(**kwargs)
        data.update(
            title="Are you sure to delete this history "
        )
        return data