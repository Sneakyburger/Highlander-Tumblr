# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import UserProfile

@login_required(login_url='/login/')
def profile(request, username):
    owner = get_object_or_404(User,username=username)
    ownerprofile = get_object_or_404(UserProfile,user=owner)

    template = loader.get_template('profile/profilepage.html')
    return render_to_response('profile/profilepage.html', {'owner':owner, 'ownerprofile':ownerprofile}, context_instance=RequestContext(request))