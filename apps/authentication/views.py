# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
import random
from smtplib import SMTPAuthenticationError

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from .models import ForgottenPasswordMailling
from core import settings
from .forms import LoginForm, SignUpForm

TWO_COMMON = [
    'password',
    '123456',
    '123456789',
    '12345678',
    '12345',
    '1234567',
    '1234567890',
    'qwerty',
    'abc123',
    '111111',
    'password1',
    '123123',
    'admin',
    'letmein',
    'welcome',
    'football',
    'iloveyou',
    'monkey',
    'login',
    'abc123456',
    'starwars',
    '1234',
    'solo',
    'passw0rd',
    'master',
    'shadow',
    'hello',
    'baseball',
    'superman',
    'trustno1',
    'batman',
    'iloveyou2',
    'michael',
    'sunshine',
    'jennifer',
    'password2',
    'charlie',
    '123456a',
    'superman1',
    'thomas',
    'hello1',
    'killer',
    'soccer',
    'jessica',
    'hockey',
    'george',
    'pokemon',
    'pokemon1',
    'daniel',
    'summer',
    'william',
    'ashley',
    'qazwsx',
    'matthew',
    'access',
    'flower',
    'jesus1',
    'bailey',
    'freedom',
    'computer',
    'tigger1',
    'whatever',
    'andrew1',
    'pepper',
    'chicken',
    'maggie1',
    'ginger',
    'purple1',
    'jordan23',
    'scooter1',
    'samantha1',
    'maverick1',
    'justin1',
    'horny1',
    'hello123',
    'scoobydoo1',
    'jason1',
    'qwert12345',
    'dallas1',
    'porsche911',
    'mustang1',
    'brandon1',
    'knight1',
    'harley1'
]

import re


def is_strong_password(password):
    """
    Vérifie si le mot de passe donné est fort
    """
    # Vérifier la longueur du mot de passe
    if len(password) < 8:
        return False

    # Vérifier la complexité du mot de passe
    regex = re.compile('^[a-zA-Z0-9]{8,}$')
    if not regex.match(password):
        return False

    # Vérifier si le mot de passe contient des informations personnelles
    if 'password' in password.lower():
        return False

    return True


def generate_confirmation_code():
    code = ""
    for i in range(6):
        code += str(random.randint(0, 9))
    return code


VERIFY_CODE = generate_confirmation_code()


def login_view(request):
    try:
        form = LoginForm(request.POST or None)

        msg = None

        if request.method == "POST":

            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/")
                else:
                    msg = 'Informations invalides'
            else:
                msg = 'Une erreur est survenue lors de la validation du formulaire'

        return render(request, "accounts/login.html", {"form": form, "msg": msg})
    except Exception:
        return render(request, 'home/page-500.html')


def register_user(request):
    try:
        msg = None
        success = False
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get("username")
                raw_password = form.cleaned_data.get("password1")
                user = authenticate(username=username, password=raw_password)

                msg = " Votre compte a bien été créé maintenant " + '<a href="/login">Connectez-Vous</a>.'
                success = True

                # return redirect("/login/")

            else:
                msg = 'Formulaire Invalide'
        else:
            form = SignUpForm()

        return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
    except Exception:
        return render(request, 'home/page-404.html')


def reset_password(request):
    r = 0
    try:
        ListeDesAdresseMail = []
        error = 1
        for mail in User.objects.all():
            ListeDesAdresseMail.append(mail.email)
        if request.method == 'POST':
            email = request.POST.get('confirmMail')
            if email is None or email not in ListeDesAdresseMail:
                error = 0
                return render(request, "accounts/reset_password.html", context={"error": error})
            send_confirmation_code(email)
            nom_user = User.objects.filter(email=email).first().username.__str__()
            ForgottenPasswordMailling.objects.create(ForgotMail=email)
            return render(request, "accounts/verifiy-code.html", context={'username': User.objects.filter(email=email).first().username.__str__()})
        return render(request, "accounts/reset_password.html", context={'code': r})
    except Exception as e:
        return render(request, "home/page-404.html")


def validation(request):
    try:
        r = ForgottenPasswordMailling.objects.filter().last().ForgotMail
        password_error = ''
        context = {'pass': True, 'pass_error': password_error}
        user = User.objects.filter(email=r)
        if r is not None:
            TWO_COMMON.append(user.filter(email=r).get().username)
        if request.method == 'POST':
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 is not None and password2 is not None:
                if password1 != password2:
                    password_error = "Les mots de passes sont différents"
                    return render(request, "accounts/verifiy-code.html", context={'pass': True,
                                                                                  'pass_error': password_error, })
                if password1 in TWO_COMMON and password2 in TWO_COMMON:
                    password_error = "Le mot de passe trop commun"
                    return render(request, "accounts/verifiy-code.html", context={'pass': True,
                                                                                  'pass_error': password_error})
                if not is_strong_password(password2):
                    password_error = "Le mot de passe ne respecte les critères requis"
                    return render(request, "accounts/verifiy-code.html", context={'pass': True,
                                                                                  'pass_error': password_error})
                if password_error == '':
                    user.update(password=make_password(password1))
                    return redirect('login')
                return render(request, "accounts/verifiy-code.html", context={'pass': True,
                                                                              'pass_error': password_error})
    except Exception:
        return render(request, 'home/page-500.html')


def send_confirmation_code(email):
    r = User.objects.filter(email=email).first().username
    s = User.objects.filter(email=email).first().first_name.__str__()
    t = User.objects.filter(email=email).first().last_name.__str__()
    st = s + ' ' + t
    subject = 'Code de confirmation pour la récupération de mot de passe'
    message = render_to_string('accounts/confirmation.html', {'complet': st, 'username': r, 'code': VERIFY_CODE})
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def verify_code(request):
    try:
        PasswordChange = False
        msg = ""
        if request.method == 'POST':
            Printedcode = request.POST.get('code')
            if Printedcode is not None and Printedcode == VERIFY_CODE:
                PasswordChange = True
        return render(request, "accounts/verifiy-code.html", context={'msg': msg, 'pass': PasswordChange})
    except Exception:
        return render(request, 'home/page-404.html')
