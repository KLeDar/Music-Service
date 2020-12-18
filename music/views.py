from django.contrib.auth import login
from django.http import HttpResponseNotFound, Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from music.forms import RegistrationForm
from music.models import Song


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm
        context = {'title': 'Регистрация нового пользователя',
                   'form': form
                   }
        return render(request, 'registration.html', context=context)

    def post(self, request):
        form = RegistrationForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            form.clean()
            login(request, form.save())
            return HttpResponseRedirect('/')
        else:
            context = {'title': 'Регистрация нового пользователя',
                       'form': form,
                       }
            return render(request, 'registration.html', context=context)


class GuestView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('main')
        context = {'title': 'Music Service',
                   }
        return render(request, 'guest.html', context=context)


class MainView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            raise Http404
        if request.user.is_superuser:
            return redirect('/admin/')
        song = Song.objects.all()
        context = {'title': 'Music Service',
                   'user_fullname': get_header_name(request),
                   'song': song,
                   }

        return render(request, 'main.html', context=context)


def add_to_favorites(request):
    if request.method == "POST":
        song_id = request.POST.get("song_id")
        try:
            add_fav_song = Song.objects.get(id=song_id)
        except Song.DoesNotExist:
            raise Http404
        add_fav_song.favorite_by.add(request.user)
        add_fav_song.save()
        return HttpResponseRedirect(reverse('main'))


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Ошибка 404, Простите извините!')


def custom_handler500(request):
    return HttpResponse("Ой, что то сломалось... Ошибка 500, Простите извините!")


def get_header_name(request):
    if request.user.get_full_name():
        return request.user.get_full_name()
    else:
        return request.user.username
