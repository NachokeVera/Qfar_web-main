from django.contrib.auth import authenticate, login as auth_login

def login_user(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return user, None
    else:
        return None, 'Usuario o contraseña incorrectos.'