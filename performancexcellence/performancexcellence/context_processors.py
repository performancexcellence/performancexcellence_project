from users.models import Profile
from athletes.models import Athlete

def profile(request):
    try:
        profile = Profile.objects.get(user = request.user)
        if profile.is_athlete:
            athlete = Athlete.objects.get(profile = profile)
        else:
            athlete = {}
        context = {"current_profile": profile,
                   "current_athlete": athlete}
    except:
        context = {"current_profile": {},
                   "current_athlete": {}}
    return context