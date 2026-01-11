from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user manager where email is the unique identifier
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None  # We disable the username field
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    
    # Gamification Fields
    RANK_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('BRONZE', 'Bronze'),
        ('SILVER', 'Silver'),
        ('GOLD', 'Gold'),
        ('DIAMOND', 'Diamond'),
        ('GRANDMASTER', 'Grandmaster'),
    ]
    current_rank = models.CharField(max_length=20, choices=RANK_CHOICES, default='BEGINNER')
    reputation_score = models.IntegerField(default=0)
    
    # Roles
    is_towing_operator = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email