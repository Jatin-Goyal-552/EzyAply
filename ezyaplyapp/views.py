from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ApplyForm, AddInternshipForm, MadeAnnouncementForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import collections
import pandas as pd
import csv
from django.core.mail import send_mail
from django.conf import settings
import numpy as np
import urllib.request
import os
from io import BytesIO
import zipfile
import os
import zipfile
from io import BytesIO
from django.contrib.auth.decorators import user_passes_test


name = ''
response_id = ''

def super_user_check(user):
    return user.is_superuser

def register(request):
    global username, email, password, OTP
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            print("email", email)
            OTP = np.random.randint(100000, 999999)
            email_subject = "OTP verification for Your account"
            email_body = "Thanks for showing intrest in EzyAply. OTP for your account is {}".format(
                OTP)
            print(send_mail(email_subject, email_body,
                  settings.EMAIL_HOST_USER, [email], fail_silently=False))
            return render(request, 'otp2.html')
    context = {'form': form}
    return render(request, 'register.html', context)


def check_otp(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        print(OTP, otp)
        if OTP == int(otp):
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            print('user created')
            messages.info(
                request, "You are now registered... Please login to continue.")
            return redirect('login')
        else:
            messages.info(request, "OTP didn't match, Please register again.")
            return render(request, 'otp2.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST.get('your_name')
        print(username)
        password = request.POST.get('your_pass')
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect('admin_home')
            global name
            name = username
            try:
                profile = Profile.objects.get(user=request.user.id)

                return redirect('home')
            except:
                return redirect('form_profile', id=request.user.id)
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'login.html')


def logout1(request):
    logout(request)
    return redirect('login')


@user_passes_test(super_user_check, login_url='login')
def admin_home(request):
    internship = Internships.objects.all().order_by('-iid') 
             # print(internship[0].iid)
    if request.method == 'POST':
        duration = request.POST['duration']
        print("duration", duration, type(duration))
        if duration != '0':
            internship = Internships.objects.filter(duration__lte=duration).order_by('-iid')
        semester = request.POST['semester']
        print("semester", semester, type(semester))
        if semester != '0':
            internship = internship.filter(semester=semester).order_by('-iid')
        stipend = request.POST['stipend']
        print("stipend", stipend, type(stipend))
        if stipend != '0':
            internship = internship.filter(stipend__gte=stipend).order_by('-iid')
        cpi = request.POST['cpi']
        print("cpi", cpi, type(cpi))
        if cpi != '0':
            internship = internship.filter(cpi__gte=cpi).order_by('-iid')
        
    context = {
        'name': request.user,
        'internships': internship,
            'user_id': request.user.id
    }
    print(context)
    return render(request, 'admin_home.html', context)


@login_required(login_url='login')
def home(request):
    internship = Internships.objects.all().order_by('-iid')
    print(internship[0].iid)
    if request.method == 'POST':
        duration = request.POST['duration']
        print("duration", duration, type(duration))
        if duration != '0':
            internship = Internships.objects.filter(duration__lte=duration).order_by('-iid')
        semester = request.POST['semester']
        print("semester", semester, type(semester))
        if semester != '0':
            internship = internship.filter(semester=semester).order_by('-iid')
        stipend = request.POST['stipend']
        print("stipend", stipend, type(stipend))
        if stipend != '0':
            internship = internship.filter(stipend__gte=stipend).order_by('-iid')
        cpi = request.POST['cpi']
        print("cpi", cpi, type(cpi))
        if cpi != '0':
            internship = internship.filter(cpi__gte=cpi).order_by('-iid')
    context = {
        'name': request.user,
        'internships': internship,
        'user_id': request.user.id
    }
    print(context)
    return render(request, 'home.html', context)

@login_required(login_url='login')
def apply(request, id):
    intern = Internships.objects.filter(iid=id)
    try:
        profile = Profile.objects.filter(user=request.user.id)
        initial_data = {
            'a_id': 1,
            'user': request.user.id,
            'internship': intern[0].iid,
            'user_name': profile[0].user_name,
            'user_email': profile[0].user_email,
            'phone_number': profile[0].phone_number,
            'sem': profile[0].sem,
            'cpi': profile[0].cpi,
            'precentage_10': profile[0].precentage_10,
            'precentage_12': profile[0].precentage_12,
            'resume': profile[0].resume
        }
    except:
        messages.warning(
            request, 'Before Applying...Please Add Your Profile First. ')
        return redirect('profile')

    # initial_data=profile
    print("------------------------")
    print(initial_data)
    form = ApplyForm(initial=initial_data)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES, initial=initial_data)
        # form["phone_number"]=id
        # print(data)
        # if data == request.user.id:
        if form.is_valid():
            form.save()
            company_name=intern[0].company_name
            # users = User.objects.all()
            # lst = []
            # for user in users:
            #     print(user.email)
            #     lst.append(user.email)
            email_subject = "Applied For Internship On EzyAply"
            email_body = f"You have applied for internship of {company_name}. Please check EzyAply app for more details."
            print("mail",send_mail(email_subject, email_body,settings.EMAIL_HOST_USER, [request.user.email], fail_silently=False))
            return redirect('internship_applied', id=request.user.id)
        else:
            print("--------", form.errors)
            return redirect('home')

    context = {'form': form,
               'user_id': request.user.id}
    return render(request, 'apply.html', context)


@login_required(login_url='login')
def internship_applied(request, id):
    # applied=Apply.objects.filter(user=request.user.id)
    # user_applied=User.objects.filter(id=request.user.id)
    applied = Apply.objects.filter(user=request.user.id).order_by('-a_id')
    # print("-------------------",str(applied[0].internship)[0])
    print("applied", applied)
    internship = []
    try:
        for i in range(len(applied)):
            internship.append(Internships.objects.filter(
                iid=applied[i].internship.iid)[0])
        print(";en", len(applied))
        print('internship', internship)
    except:
        context = {
            'user_id': request.user.id}
        return render(request, 'no_internship_applied.html', context)
    print("========", internship)
    context = {'applieds': applied,
               'user_id': request.user.id,
               'internships': internship,
               'combine': zip(applied, internship)}

    return render(request, 'internship_applied.html', context)

@user_passes_test(super_user_check, login_url='login')
def add_internship(request):
    form = AddInternshipForm()
    if request.method == 'POST':
        form = AddInternshipForm(request.POST)
        if form.is_valid():
            form.save()
            company_name=form.cleaned_data['company_name']
            users = User.objects.all()
            lst = []
            for user in users:
                print(user.email)
                lst.append(user.email)
            email_subject = "Internship Added On EzyAply"
            email_body = f"Admin added internship of {company_name}. Please check EzyAply app for more details."
            print("mail",send_mail(email_subject, email_body,settings.EMAIL_HOST_USER, lst, fail_silently=False))
            return redirect('admin_home')
        else:
            return redirect('add_internship')
    context = {'form': form,
               'user_id': request.user.id}
    return render(request, 'add_internship.html', context)

@user_passes_test(super_user_check, login_url='login')
def view_responses(request, id):
    responses = Apply.objects.filter(internship=id)
    global response_id
    response_id = id
    print("===============------", responses)
    context = {
        'responses': responses,
        'email': request.user.email,
        'id': id
    }
    return render(request, 'view_responses.html', context)

@user_passes_test(super_user_check, login_url='login')
def download(request):
    global response_id
    print("============", response_id)
    dic = collections.defaultdict(list)
    responses = Apply.objects.filter(internship=response_id)
    for i in range(len(responses)):
        dic['user'].append(responses[i].user.username)
        dic['user_name'].append(responses[i].user_name)
        dic['user_email'].append(responses[i].user_email)
        dic['phone_number'].append(responses[i].phone_number)
        dic['sem'].append(responses[i].sem)
        dic['cpi'].append(responses[i].cpi)
        dic['precentage_10'].append(responses[i].precentage_10)
        dic['precentage_12'].append(responses[i].precentage_12)
    print(dic)
    df = pd.DataFrame(dic)

    response = HttpResponse(content_type='text/csv')
    # your filename
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    writer = csv.writer(response)
    writer.writerow(['S.No.', 'Name', 'User Name', 'User Email', 'Phone Number', 'Semester', 'CPI', '10th Precentage', '12th Precentage'])
    for ind in range(df.shape[0]):
        writer.writerow([ind, df['user'][ind], df['user_name'][ind], df['user_email'][ind],df['phone_number'][ind],df['sem'][ind],df['cpi'][ind],df['precentage_10'][ind],df['precentage_12'][ind]])

    return response

@user_passes_test(super_user_check, login_url='login')
def announcement(request):
    form = MadeAnnouncementForm()
    if request.method == 'POST':
        form = MadeAnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            users = User.objects.all()
            lst = []
            for user in users:
                print(user.email)
                lst.append(user.email)
            email_subject = "Announcement Made On EzyAply"
            email_body = f"Admin has made an important announcement. Please check EzyAply for more details."
            print("mail",send_mail(email_subject, email_body,settings.EMAIL_HOST_USER, lst, fail_silently=False))
            return redirect('all_announcement')
        else:
            return redirect('announcement')
    context = {'form': form,
               'user_id': request.user.id}
    return render(request, 'announcement.html', context)

@login_required(login_url='login')
def all_announcements(request):
    announcements = Announcement.objects.all().order_by('-an_id')
    context = {
        'announcements': announcements,
    }
    return render(request, 'all_announcement.html', context)

@login_required(login_url='login')
def all_announcements_student(request):
    announcements = Announcement.objects.all().order_by('-an_id')
    context = {
        'announcements': announcements,
        'user_id': request.user.id
    }
    return render(request, 'all_announcements_student.html', context)

@user_passes_test(super_user_check, login_url='login')
def edit_internship(request, id):
    intern = Internships.objects.get(iid=id)
    
    form = AddInternshipForm(instance=intern)
    if request.method == 'POST':
        form = AddInternshipForm(request.POST, instance=intern)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
        else:
            return redirect('edit_internship')
    context = {'form': form,
               'user_id': request.user.id}
    return render(request, 'edit_internship.html', context)

@user_passes_test(super_user_check, login_url='login')
def delete_internship(request, id):
    intern = Internships.objects.get(iid=id)
    intern.delete()
    return redirect('admin_home')

@user_passes_test(super_user_check, login_url='login')
def edit_announcement(request, id):
    announcement = Announcement.objects.get(an_id=id)
    form = MadeAnnouncementForm(instance=announcement)
    if request.method == 'POST':
        form = MadeAnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('all_announcement')
        else:
            return redirect('edit_announcement')
    context = {'form': form,
               'user_id': request.user.id}
    return render(request, 'edit_announcement.html', context)

@user_passes_test(super_user_check, login_url='login')
def delete_announcement(request, id):
    announcement = Announcement.objects.get(an_id=id)
    announcement.delete()
    return redirect('all_announcement')

@login_required(login_url='login')
def profile(request):
    # user=User.objects.get(id=request.user.id)
    try:
        profile = Profile.objects.filter(user=request.user.id)
        print("profile", profile[0].user)
        print("hello")
        return render(request, 'profile.html', {
            'profile': profile[0],
            'user_id': request.user.id,
                'email': request.user.email,
        })

    except:
        print("hii")
        return render(request, 'add_profile.html', {'user_id': request.user.id})

@login_required(login_url='login')
def edit_profile(request, id):
    profile = Profile.objects.get(p_id=id)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print("-----", form.errors)
            return redirect('edit_profile')
    context = {'form': form,
               'user_id': request.user.id}
    return render(request, 'edit_profile.html', context)

@login_required(login_url='login')
def form_profile(request, id):
    initial_data = {
        'user': request.user.id,
    }
    form = ProfileForm(initial=initial_data)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, initial=initial_data)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return redirect('form_profile')
    context = {'form': form,
               'user_id': request.user.id}
    return render(request, 'form_profile.html', context)

@user_passes_test(super_user_check, login_url='login')
def download_resume(request):
    responses = Apply.objects.filter(internship=response_id)
    filenames = []
    for response in responses:
        filenames.append("media/" + response.resume.name)
    print(filenames)
    zip_subdir = f"allresume{response_id}"
    zip_filename = "%s.zip" % zip_subdir

    s = BytesIO()
    zf = zipfile.ZipFile(s, "w")

    for fpath in filenames:
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)
        zf.write(fpath, zip_path)

    zf.close()

    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp 