from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def member_check(user):
    return user.profile.role == "MEM"

@user_passes_test(member_check)
def Member(request):
    return HttpResponse("<p>You are a Member</p>")
