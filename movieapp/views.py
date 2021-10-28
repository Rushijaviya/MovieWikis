from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests


def index(request):

    soon_url = "https://imdb-api.com/en/API/ComingSoon/k_pftzqnp0"
    soon = requests.get(soon_url).json()
    release_url = ("https://imdb-api.com/en/API/InTheaters/k_pftzqnp0")
    release = requests.get(release_url).json()
    top_url = "https://imdb-api.com/en/API/BoxOffice/k_pftzqnp0"
    top = requests.get(top_url).json()
    lastest_url = "https://imdb-api.com/en/API/InTheaters/k_pftzqnp0"
    lastest = requests.get(lastest_url).json()
    context = {"soon": soon, "release": release,
               "top": top, "lastest": lastest}
    return render(request, "home.html", context)


def movies(request):
    return render(request, "movies.html")


def login(request):
    return render(request, "login.html")


def celebrities(request):
    return render(request, "celebrities.html")


def moviedetails(request, pk):
    print(pk)
    url = 'https://imdb-api.com/en/API/Title/k_lwm5x736/'+pk+'/Trailer,Ratings,Wikipedia,'
    details = requests.get(url).json()
    context = {"details": details}

    return render(request, "movie-details.html", context)


def top_movies(request):
    return render(request, "top-movies.html")


def blog(request):
    return render(request, "blog.html")


def blog_details(request):
    return render(request, "blog-details.html")


def register_user(request):

    if request.method == 'POST':
        user_form = userForm(request.POST)
        user_info_form = userInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user
            user_info.save()

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)

            return redirect('home')

        else:
            context = {'user_form.errors': user_form.errors,
                       'user_info_form.errors': user_info_form.errors}
            return render(request, 'user/register.html', context)
    else:

        user_form = userForm()
        user_info_form = userInfoForm()

        context = {'user_form': user_form,
                   'user_info_form': user_info_form}

        return render(request, 'user/register.html', context)


def searchresult(request):

    if request.method == "POST":
        Query = request.POST.get("Query")
        query_url = "https://imdb-api.com/en/API/SearchMovie/k_08ug9l32/"+Query
        query = requests.get(query_url).json()
        print(query)
        context = {"query": query}
    return render(request, 'result.html', context)
