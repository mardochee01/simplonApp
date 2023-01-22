from django.shortcuts import render
from .forms import ParticipantRegistration
from .models import Participant
# Create your views here.
def registration(request):
    if request.method == 'POST':
        fm = ParticipantRegistration(request.POST)
        if fm.is_valid():
            ln = fm.cleaned_data['lastName']
            fn = fm.cleaned_data['firstName']
            pn = fm.cleaned_data['phoneNumber']
            em = fm.cleaned_data['email']
            reg = Participant(lastName = ln, firstName = fn, phoneNumber = pn, email = em)
            reg.save()
            fm = ParticipantRegistration()
    else:
        fm = ParticipantRegistration()
    return render(request, 'participant/registration.html', {'form':fm})


def show(request):
    part = Participant.objects.all()
    return render(request, 'participant/show.html', {'part':part})