from rest_framework import generics
from .models import Bike, Rental
from .serializers import BikeSerializer, RentalSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework import serializers


class BikeListView(generics.ListAPIView):
    queryset = Bike.objects.filter(is_available=True)
    serializer_class = BikeSerializer


class RentalCreateView(generics.CreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        bike = serializer.validated_data['bike']
        if not bike.is_available:
            raise serializers.ValidationError('This bike is not available for rent.')
        if Rental.objects.filter(user=self.request.user, end_time__isnull=True).exists():
            raise serializers.ValidationError('You already have a bike rented.')
        bike.is_available = False
        bike.save()
        serializer.save(user=self.request.user)


class RentalReturnView(generics.UpdateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.end_time:
            raise serializers.ValidationError('This bike has already been returned.')
        instance.end_time = timezone.now()
        instance.bike.is_available = True
        instance.bike.save()
        serializer.save()


class UserRentalHistoryView(generics.ListAPIView):
    serializer_class = RentalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Rental.objects.filter(user=self.request.user)
