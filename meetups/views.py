from django.shortcuts import render, redirect
from .models import Meetups, Participant
from .forms import RegistrationForm

def index(request):
    meetups = Meetups.objects.all()
    return render(request, 'meetups/index.html',context={
        'meetups':meetups,
        'show_meetups': True
        })


def meetup_details(request, meetup_id):

    try:
        meetup = Meetups.objects.get(meetup_id=meetup_id)
        
        if request.method == 'GET':
            registartion_from = RegistrationForm()

        elif request.method == 'POST':
            
            # the post request body is mapped to reg form
            registartion_from = RegistrationForm(request.POST)
            
            if registartion_from.is_valid():
                
                paricipant_email = registartion_from.cleaned_data['email']
                #so if they already registered user is in db, that is not an issue anymore
                participant, _ =  Participant.objects.get_or_create(email = paricipant_email)
                meetup.participants.add(participant )
                print('sssss')
                return redirect('confirmation', meetup_id)

        return render(request, 'meetups/meetup-details.html',
                        context={
                            'meetup_found': True,
                            'meetup': meetup,
                            'form' : registartion_from
                            })
    except Exception as ex:
        return render(request, 'meetups/meetup-details.html', context= {
            'meetup_found': False
        })
    

def confirm_registration(request, meetup_id):
    meetup = Meetups.objects.get(meetup_id=meetup_id)
    return render(request, 'meetups/confirmation.html',
                  context={
                      'organiser_email': meetup.organiser_email
                  } )
