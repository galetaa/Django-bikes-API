from django.urls import path
from .views import BikeListView, RentalCreateView, RentalReturnView, UserRentalHistoryView


urlpatterns = [
    path('', BikeListView.as_view(), name='bike-list'),
    path('rent/', RentalCreateView.as_view(), name='rent-bike'),
    path('return/<int:pk>/', RentalReturnView.as_view(), name='return-bike'),
    path('history/', UserRentalHistoryView.as_view(), name='rental-history'),
]