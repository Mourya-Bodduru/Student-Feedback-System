from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    username = request.user.username
    return render(request, 'pages/dashboard.html', {'username': username})
