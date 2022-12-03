import re
from django.contrib import messages
from django.contrib.messages import constants
from django.core.mail import EmailMultiAlternatives


def fields_empty(request, username, email):
    if (len(username.strip()) == 0) or (len(email.strip()) == 0):
        messages.add_message(request, constants.ERROR, 'Os campos username e email não podem ficar vazios!')
        return False
    return True


def password_is_valid(request, password, confirm_password):
    qtd_caracteres = 6

    if len(password) < qtd_caracteres:
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter 6 ou mais caracteres!')
        return False

    if not password == confirm_password:
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
        return False
    
    if not re.search('[A-Z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas!')
        return False

    if not re.search('[a-z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas!')
        return False

    if not re.search('[1-9]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contém números!')
        return False

    return True