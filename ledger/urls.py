from django.urls import path
from . import views
urlpatterns = [
    path('record/', views.record, name='record'),
    path('update/<int:ledger_id>/', views.update_ledge, name="update_ledge"),
    path('delete/<int:ledger_id>/', views.delete_ledger, name="delete_ledger"),
    path('detail/<int:ledger_id>/', views.detail_ledger, name="detail_ledger"),
]
