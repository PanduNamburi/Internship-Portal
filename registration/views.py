from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Applicant
from .forms import ApplicantForm
from django.http import JsonResponse

def home(request):
    """Home page view"""
    return render(request, 'registration/home.html')

def register(request):
    """Intern/Volunteer registration form view"""
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been submitted successfully! We will contact you soon.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ApplicantForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def admin_dashboard(request):
    """Admin dashboard to view all applicants"""
    applicants = Applicant.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        applicants = applicants.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(department__icontains=search_query)
        )
    
    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter:
        applicants = applicants.filter(status=status_filter)
    
    # Filter by position type
    position_filter = request.GET.get('position_type', '')
    if position_filter:
        applicants = applicants.filter(position_type=position_filter)
    
    # Pagination
    paginator = Paginator(applicants, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'status_filter': status_filter,
        'position_filter': position_filter,
        'status_choices': Applicant.STATUS_CHOICES,
        'position_choices': Applicant.POSITION_CHOICES,
    }
    
    return render(request, 'registration/admin_dashboard.html', context)

@login_required
def applicant_detail(request, applicant_id):
    """View detailed information about a specific applicant"""
    applicant = get_object_or_404(Applicant, id=applicant_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        admin_notes = request.POST.get('admin_notes')
        
        if new_status in dict(Applicant.STATUS_CHOICES):
            applicant.status = new_status
            applicant.admin_notes = admin_notes
            applicant.save()
            messages.success(request, f'Application status updated to {new_status}.')
            return redirect('admin_dashboard')
    
    return render(request, 'registration/applicant_detail.html', {'applicant': applicant})

@login_required
def update_status(request, applicant_id):
    """Update applicant status via AJAX"""
    if request.method == 'POST':
        applicant = get_object_or_404(Applicant, id=applicant_id)
        new_status = request.POST.get('status')
        
        if new_status in dict(Applicant.STATUS_CHOICES):
            applicant.status = new_status
            applicant.save()
            return JsonResponse({'success': True, 'status': new_status})
    
    return JsonResponse({'success': False})
