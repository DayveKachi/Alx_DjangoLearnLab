from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def admin_check(user):
    return user.profile.role == "ADM"

@user_passes_test(admin_check)
def Admin(request):
    return HttpResponse("<p>You are an Admin</p>")
