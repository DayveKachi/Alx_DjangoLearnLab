from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def librarian_check(user):
    return user.profile.role == "LIB"

@user_passes_test(librarian_check)
def Librarian(request):
    return HttpResponse("<p>You are a Librarian</p>")
