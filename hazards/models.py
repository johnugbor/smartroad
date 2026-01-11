from django.contrib.gis.db import models # Import from GIS, not standard models
from django.conf import settings

class Hazard(models.Model):
    HAZARD_TYPES = [
        ('VEHICULAR', 'Vehicular Accident'),
        ('MOTORCYCLE', 'Motorcycle Accident'),
        ('PEDESTRIAN', 'Pedestrian Incident'),
        ('OBSTACLE', 'Road Obstacle'),
        ('POTHOLE', 'Deep Pothole'),
        ('BROKEN_VEHICLE', 'Broken Down Vehicle'),
    ]
    
    STATUS_CHOICES = [
        ('PENDING', 'Pending Verification'),
        ('VERIFIED', 'Verified'),
        ('RESOLVED', 'Resolved/Fixed'),
        ('FALSE', 'False Report'),
    ]

    # Who reported it?
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
    # GEOSPATIAL FIELD: Stores Longitude/Latitude
    location = models.PointField(srid=4326) 
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=HAZARD_TYPES)
    
    # Validation Logic
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} - {self.status}"

class HazardMedia(models.Model):
    """Stores images and videos for hazards"""
    hazard = models.ForeignKey(Hazard, related_name='media', on_delete=models.CASCADE)
    file = models.FileField(upload_to='hazard_media/%Y/%m/%d/')
    is_video = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)