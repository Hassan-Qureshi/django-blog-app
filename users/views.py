from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'User {user} registered successfully!'.format(user=username))
            return redirect('log-in')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        # User Information update like username, email etc.
        user_info_update = UserUpdateForm(request.POST, instance=request.user)
        # User Profile Photo Update
        photo_update = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)

        if user_info_update.is_valid() and photo_update.is_valid():
            user_info_update.save()
            photo_update.save()
            messages.success(request, "Your profile is updated successfully!")
            return redirect("profile")
    else:
        user_info_update = UserUpdateForm(instance=request.user)
        photo_update = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_info_update': user_info_update,
        'photo_update': photo_update
    }
    return render(request, 'users/profile.html', context=context)
