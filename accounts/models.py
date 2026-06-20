from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    ROLE_CHOICES = (
        ('farmer', 'Farmer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='farmer')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    farm_location = models.CharField(max_length=255, blank=True)
    farm_size = models.FloatField(null=True, blank=True, help_text="Size of farm in acres")
    preferred_crop = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

# Signals to automatically create/update FarmerProfile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        FarmerProfile.objects.create(user=instance, full_name=instance.get_full_name() or instance.username)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # If the user profile doesn't exist, create it (e.g. for existing users during upgrade)
    if not hasattr(instance, 'profile'):
        FarmerProfile.objects.create(user=instance, full_name=instance.get_full_name() or instance.username)
    instance.profile.save()
