from .models import Profile

def profile_context(request):
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    return {
        'profile_global': profile
    }
