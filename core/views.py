from unicodedata import category
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import ServicesSlider,Testimonial,Achievements,Adress,Blog,Repositary,Project,HomepageProfile,Contact,Subscribers,Mailmessage,AboutProfile,AboutServices,Aboutskills,AboutPersonalAwards,Socialmedia
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from portfolio.settings import EMAIL_HOST_USER
# Create your views here.

def home(request):
    sliders = ServicesSlider.objects.all()
    testimonials = Testimonial.objects.all()
    achievements = Achievements.objects.all()
    homeprofiles = HomepageProfile.objects.all()
    socialmedias = Socialmedia.objects.all() 
    
    data = {
        'sliders': sliders,
        'testimonials': testimonials,
        'achievements': achievements,
        'homeprofiles': homeprofiles,
        'socialmedias': socialmedias,

        }
    return render(request, 'home.html', data)



def blog(request):
    blogs = Blog.objects.order_by('-created_at')
    paginator = Paginator(blogs, 8)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    trending_blogs = Blog.objects.order_by('-created_at').filter(is_featured=True)
    socialmedias = Socialmedia.objects.all()
    
    data = {
        'blogs': paged_blogs,
        'trending_blogs': trending_blogs,
        'socialmedias': socialmedias,

    }
    return render(request, 'blog.html',data)

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    trending_blogs = Blog.objects.order_by('-created_at').filter(is_featured=True)
    socialmedias = Socialmedia.objects.all()
    data = {
        'blog': blog,
        'trending_blogs': trending_blogs,
        'socialmedias': socialmedias,
    }
    return render(request, 'blog_detail.html',data)

def repositaries(request):
    repos = Repositary.objects.all()
    paginator = Paginator(repos,10)
    page = request.GET.get('page')
    paged_repos = paginator.get_page(page)
    trending_blogs = Blog.objects.order_by('-created_at').filter(is_featured=True)
    socialmedias = Socialmedia.objects.all()
    data = {
        'repos': paged_repos,
        'trending_blogs': trending_blogs,
        'socialmedias': socialmedias,
    }
    return render(request, 'repositaries.html',data)

def project(request):
    projects = Project.objects.order_by('-created_at')
    paginator = Paginator(projects, 8)
    page = request.GET.get('page')
    paged_projects = paginator.get_page(page)
    trending_projetcs = Project.objects.order_by('-created_at').filter(is_featured=True)
    socialmedias = Socialmedia.objects.all()
    data = {
        'projects': paged_projects,
        'trending_projects': trending_projetcs,
        'socialmedias': socialmedias,
    }
    return render(request,'project.html',data)



def project_detail(request,slug):
    project = Project.objects.get(slug=slug)
    trending_projects = Project.objects.order_by('-created_at').filter(is_featured=True)
    socialmedias = Socialmedia.objects.all()
    data = {
        'project': project,
        'trending_projects': trending_projects,
        'socialmedias': socialmedias,
    }
    return render(request,'project_detail.html',data)

def searchblogs(request):
    blogs = Blog.objects.order_by('-created_at')
    trending_projetcs = Project.objects.order_by('-created_at').filter(is_featured=True)
    socialmedias = Socialmedia.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search']
        if search_term:
            blogs = blogs.filter(Q(description__icontains=search_term) | Q(title__icontains=search_term) | Q(category__icontains=search_term))

            
        
    data = {
        'blogs': blogs,
        'trending_blogs': trending_projetcs,
        'socialmedias': socialmedias,
        
 
    } 
    return render(request, 'searchblogs.html',data)

def searchprojects(request):
    projects = Project.objects.order_by('-created_at')
    trending_projetcs = Project.objects.order_by('-created_at').filter(is_featured=True)
    socialmedias = Socialmedia.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search']
        if search_term:
            projects = projects.filter(Q(description__icontains=search_term) | Q(title__icontains=search_term) | Q(category__icontains=search_term))
            
    data = {
        'projects': projects,
        'trending_projects': trending_projetcs,
        'socialmedias': socialmedias,
    } 
    return render(request, 'searchprojects.html',data)

def contact(request):
    adress = Adress.objects.all()
    socialmedias = Socialmedia.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Thanks for contacting us. We will get back to you soon.')
        return redirect('contact')
        

    data = {
        'adress': adress,
        'socialmedias': socialmedias,
    }
    return render(request, 'contact.html',data)


def about(request):
    if request.method == 'POST':
        email = request.POST['email']
        subscriber = Subscribers(email=email)
        subscriber.save()
        messages.success(request, 'Thanks for subscribing and now you are going to receive the latest updates about blogs and projects.')
        message = '''
        You have been subscribed to our website and you will receive the latest updates about blogs and projects.
        \n\n\n\n\n\n\n\n\n\n


Thanks for subscribing.
Sandeep Rayudu Boya

        '''
        send_mail(
            'Subscription',
            message,
            EMAIL_HOST_USER,
            [email],
        )

        return redirect('about')

    aboutprofiles = AboutProfile.objects.all()
    aboutskills = Aboutskills.objects.all()
    aboutservices = AboutServices.objects.all()
    aboutpersonalawards = AboutPersonalAwards.objects.all()
    socialmedias = Socialmedia.objects.all()
    
    
    data = {
        'aboutprofiles': aboutprofiles,
        'aboutskills': aboutskills,
        'aboutservices': aboutservices,
        'aboutpersonalawards': aboutpersonalawards,
        'socialmedias': socialmedias,
    }
    



    

    return render(request, 'about.html',data)