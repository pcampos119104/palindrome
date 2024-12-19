import marimo

__generated_with = "0.9.30"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import os
    import django
    import sys
    sys.path.insert(0,'/app')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "palindrome.settings")
    os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")

    django.setup()
    return django, mo, os, sys


@app.cell
def __():
    from django.contrib.auth import get_user_model
    User=get_user_model()
    user, created = User.objects.get_or_create(username='Pedro', email='email@asdf.asdf')
    if created:
        user.set_password('password')
        user.save()

    print(user)
    return User, created, get_user_model, user


if __name__ == "__main__":
    app.run()
