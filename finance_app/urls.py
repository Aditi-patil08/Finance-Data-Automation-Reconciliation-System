from django.urls import path
from . import views

urlpatterns = [
    path('run-reconciliation/', views.run_recon),
    path('summary/', views.summary),
    path('reconciliation/', views.reconciliation_view),
    path('category-breakdown/', views.category_breakdown),
]