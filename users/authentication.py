from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()

class EmailOrPhoneBackend(ModelBackend):
    """
    Custom backend to allow login via Email OR Phone Number.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        
        try:
            # Check if input matches email OR phone_number
            user = UserModel.objects.get(Q(email=username) | Q(phone_number=username))
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None