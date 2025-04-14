from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import StudentPG,StudentPhd,StudentEquery
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from testapp.forms import SignUpform
from django.contrib.auth.mixins import LoginRequiredMixin
from testapp.models import Marksheet
from testapp.forms import EnrollmentSearchForm

def homepage(request):
    return render(request,'testapp/home.html')

def aboutpage(request):
    return render(request,'testapp/about.html')

def logoutpage(request):
    logout(request)
    return render(request,'testapp/logout.html')

@login_required
def indexpage(request):
    request.session['user_name'] = request.user.username
    request.session['login_time'] = str(request.user.last_login)
    return render(request, 'testapp/index.html')

def signuppage(request):
    form = SignUpform()
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
            return HttpResponseRedirect('/accounts/login')
        else:
            form.add_error(None, "There were errors with your form submission.")
    return render(request, 'testapp/signup.html', {'form': form})


class StudentList(LoginRequiredMixin,ListView):
    model=StudentPG
    ordering=['Inrollment_no']

class StudentDetail(DetailView):
    model=StudentPG

class StudentForm(LoginRequiredMixin,CreateView):
    model=StudentPG
    fields='__all__'
    success_url=('/list')

class StudentUpdate(LoginRequiredMixin,UpdateView):
    model=StudentPG
    fields='__all__'
    success_url='/list'
    
class StudentDelete(LoginRequiredMixin,DeleteView):
    model=StudentPG
    success_url='/list'
    

class StudentPhdList(LoginRequiredMixin,ListView):
    model=StudentPhd
    ordering=['Inrollment_no']

class StudentPhddetail(LoginRequiredMixin,DetailView):
    model=StudentPhd

class StudentPhdform(LoginRequiredMixin,CreateView):
    model=StudentPhd
    fields='__all__'
    success_url=('/listphd')

class StudentPhdUpdate(LoginRequiredMixin,UpdateView):
    model=StudentPhd
    fields='__all__'
    success_url='/listphd'

class StudentPhdDelete(LoginRequiredMixin,DeleteView):
    model=StudentPhd
    success_url='/listphd'

class StudentEnq(CreateView):
    model=StudentEquery
    fields="__all__"
    success_url = ('/thank/')

def thanks(request):
    return render(request,'testapp/thanks.html')

class MarksheetList(LoginRequiredMixin,ListView):
    model=Marksheet
    ordering=['Inrollment_no']

class MarksheetDetail(DetailView):
    model=Marksheet

class MarksheetForm(LoginRequiredMixin,CreateView):
    model=Marksheet
    fields='__all__'
    success_url='/mlist'

class MarksheetDelete(LoginRequiredMixin,DeleteView):
    model=Marksheet
    success_url='/mlist'
class MarksheetUpadate(LoginRequiredMixin,UpdateView):
    model=Marksheet
    fields='__all__'
    success_url='/mlist'

def search_marksheet(request):
    form = EnrollmentSearchForm(request.GET or None)
    marksheet = None
    not_found = False

    if form.is_valid():
        enrollment_no = form.cleaned_data['enrollment_no']
        try:
            marksheet = Marksheet.objects.get(Inrollment_no=enrollment_no)
            return render(request, 'testapp/marksheet_detail.html', {'marksheet': marksheet})
        except Marksheet.DoesNotExist:
            not_found = True

    return render(request, 'testapp/search.html', {
        'form': form,
        'marksheet': marksheet,
        'not_found': not_found,
    })
