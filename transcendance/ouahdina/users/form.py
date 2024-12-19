# change
from django.contrib.auth.models import User

# to
from django.contrib.auth import get_user_model

User = get_user_model()