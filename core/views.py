from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from .models import Publication, Comment


# Create your views here.


def homepage(request):
    return render(request, "home.html")


def aboutpage(request):
    return HttpResponse("Hello World")

def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)  # Get user by email
            user = authenticate(request, username=user.username, password=password)  # Authenticate with username
        except User.DoesNotExist:
            user = None  # If email is not found, authentication fails

        print(email, password)
        print(user)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("publications")  
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "signin.html")


def signup_page(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = f"{firstname} {lastname}"  # Allow duplicate usernames
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Validations
        if not firstname or not lastname or not email or not password1 or not password2:
            messages.error(request, "All fields are required.")
        elif password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif len(password1) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
        else:
            try:
                validate_email(email) 
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.first_name = firstname
                user.last_name = lastname
                user.save()
                login(request,user)
                messages.success(request, "Account created successfully!")
                return redirect("homepage")  

            except ValidationError:
                messages.error(request, "Invalid email format.")
            except IntegrityError:
                messages.error(request, "Email already registered.")  

    return render(request, "signup.html")



def publication_detail(request, slug):
    publication = get_object_or_404(Publication, slug=slug)
    comments =  Comment.objects.filter(publication_id=publication).order_by("-created_at")

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You need to log in to comment.")
            return redirect("login_page")
        
        comment_value = request.POST.get("comment_value")
        if comment_value:
            Comment.objects.create(
                user=request.user,
                publication=publication,
                comment_value=comment_value,
            )
            messages.success(request, "Comment added successfully!")
            return redirect("publication_detail", publication_id=publication.id)
        else:
            messages.error(request, "Comment cannot be empty.")

    return render(request, "publication.html", {
        "publication": publication,
        "comments": comments,
    })



@login_required
def publications_page(request):
    #fetch all publications from publication model only title and likes
    publications = Publication.objects.all().values('title', 'likes', 'slug')
    publications_list = list(publications)
    print(publications_list)
    #pass publication as context
    context = {'publications': publications_list}
    return  render(request, "publications.html", context)


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("homepage")