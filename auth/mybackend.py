from user.models import User


def authenticate(email=None, password=None):
    try:
        user = User.objects.get(email=email)
        print(user)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
    return None
