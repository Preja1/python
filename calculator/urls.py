from django.urls import include, path
from calculator.views import calculate_view
urlpatterns=[
    path("calculator/",calculate_view),
]
#Class base view
from calculator.views2 import (
    #Test purpose
    CalculatorView,
    #Exact Crud views
    CalculatorReadView,
    CalculatorCreateView,
    CalculatorDeleteView,
    CalculatorUpdateView
)
urlpatterns+=[
    path("new/",include(
        [
        path("test/",CalculatorView.as_view()),
        path("",CalculatorReadView.as_view(),name="calc-list"),
        path("create/",CalculatorCreateView.as_view(),name="calc-create"),
        path("update/<str:pk>/",CalculatorUpdateView.as_view(),name="calc-update"),
        path("delete/<str:pk>//",CalculatorDeleteView.as_view(),name="calc-delete"), 
        ]
    ))
]      