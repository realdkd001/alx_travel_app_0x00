from rest_framework import serializers
from .models import User, Listing, Booking

# Serializer for Listing Model
class ListingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    
    
    class Meta:
        model = Listing
        fields = ['listing_id', 'user', 'title', 'price', 'description', 'location', 'created_at']
        read_only_fields = ['listing_id', 'created_at']

# Serializer for Booking Model
class BookingSerializer(serializers.ModelSerializer):
    listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all(), required=True)
    host = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)
    status = serializers.CharField(required=True)
    
    class Meta:
        model = Booking
        fields = ['booking_id', 'listing', 'host', 'status', 'start_date', 'end_date', 'created_at']
        read_only_fields = ['booking_id', 'created_at', 'host']
