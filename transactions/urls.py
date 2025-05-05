from django.urls import path
from .views import TransactionListView, TransactionCreateView, TransactionUpdateView

app_name = 'transactions'

urlpatterns = [
    path('', TransactionListView.as_view(), name='list'),
    path('new/', TransactionCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', TransactionUpdateView.as_view(), name='edit'),
]
