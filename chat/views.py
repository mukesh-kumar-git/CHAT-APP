from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.

@login_required
def user_list(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/users.html', {'users': users})

@login_required
def chat_view(request, user_id):
    other_user = User.objects.get(id=user_id)
    return render(request, 'chat/chat.html', {'other_user': other_user})

@csrf_exempt
@login_required
def send_message(request):
    if request.method == 'POST':
        sender = request.user
        receiver_id = request.POST.get('receiver')
        text = request.POST.get('message')
        receiver = User.objects.get(id=receiver_id)
        Message.objects.create(
            sender=sender,
            receiver=receiver,
            text=text
        )
        return JsonResponse({'status': 'ok'})

@login_required
def user_list(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/users.html', {'users': users})


@login_required
def chat_view(request, user_id):
    other_user = User.objects.get(id=user_id)
    return render(request, 'chat/chat.html', {'other_user': other_user})


@login_required
@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        receiver = User.objects.get(id=request.POST.get('receiver'))
        text = request.POST.get('message', '').strip()
        file = request.FILES.get('file')
        if text == '' and not file:
            return JsonResponse({'status': 'empty'})
        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            text=text,
            file=file
        )
        return JsonResponse({'status': 'ok'})



def get_messages(request, user_id):
    other_user = User.objects.get(id=user_id)

    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by('timestamp')

    data = []
    for msg in messages:
        data.append({
            'sender': msg.sender.username,
            'text': msg.text,
            'file': msg.file.url if msg.file else '',
            'time': msg.timestamp.strftime('%H:%M')
        })

    return JsonResponse(data, safe=False)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            # Just check password, no constraints
            if not password1:
                messages.error(request, "Password cannot be empty.")
            elif password1 != password2:
                messages.error(request, "Passwords do not match.")
            else:
                form.save()
                return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
