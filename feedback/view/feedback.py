from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from feedback.models import Feedback

def feedback(request):
    if request.method == 'POST':
        tname = request.POST.get('tname')
        sname = request.POST.get('sname')
        dept = request.POST.get('dept')
        feedback_text = request.POST.get('feedback_text')
        rating = request.POST.get('rating')

        if tname and sname and dept and feedback_text and rating:

            feedback = Feedback.objects.create(
                tname=tname,
                sname=sname,
                dept=dept,
                feedback_text=feedback_text,
                rating=rating,
            )
            feedback.save()
            return HttpResponseRedirect('/thank_you/')
        
        else:
            messages.error(request, 'Please fill in all required fields.')

    return render(request, 'pages/feedback.html')
    
