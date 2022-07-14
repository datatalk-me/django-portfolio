from django.contrib import admin
from .models import ServicesSlider,Testimonial,Achievements,Adress,Blog,Repositary,Project,HomepageProfile,Contact,Subscribers,Mailmessage,AboutPersonalAwards,AboutServices,AboutProfile,Aboutskills,Socialmedia
from django.utils.html import format_html
from django.core.mail import send_mail
# Register your models here.


class TestimonialAdmin(admin.ModelAdmin):

    def client_photo(self, obj):
        return format_html('<img src="{}" width="40"  />'.format(obj.client_image.url))

    list_display = ('client_photo','client_name', 'client_place', 'created_at')
    list_filter = ('client_place', 'created_at')
    search_fields = ('client_name', 'client_place', 'created_at')
    ordering = ('client_name', 'client_place', 'created_at')
    date_hierarchy = 'created_at'
    fields = ('client_name', 'client_place', 'client_image', 'review', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'client_name': ('client_name',)}
    save_on_top = True
    save_as = True
    class Meta:
        model = Testimonial
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'


class blogAdmin(admin.ModelAdmin):

    def blog_image(self, obj):
        return format_html('<img src="{}" width="40"  />'.format(obj.image.url))

    list_display = ('blog_image','title','slug', 'author','is_featured', 'created_at')
    list_filter = ('author','category','created_at')
    list_editable = ('is_featured',)
    search_fields = ('title','slug','category','author', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title','category','author', 'created_at')
    date_hierarchy = 'created_at'
    fields = ('title','slug','snippet', 'description', 'image', 'category', 'author', 'time_to_read', 'is_featured', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    save_on_top = True
    save_as = True
    class Meta:
        model = Blog
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

class projectAdmin(admin.ModelAdmin):
    
        def project_image(self, obj):
            return format_html('<img src="{}" width="40"  />'.format(obj.image.url))
    
        list_display = ('project_image','title','slug', 'author','is_featured', 'created_at')
        list_filter = ('author','category','created_at')
        list_editable = ('is_featured',)
        search_fields = ('title','slug','category','author', 'created_at')
        prepopulated_fields = {'slug': ('title',)}
        ordering = ('title','category','author', 'created_at')
        date_hierarchy = 'created_at'
        fields = ('title','slug','snippet', 'description', 'image', 'category', 'author', 'time_to_read', 'is_featured', 'created_at')
        readonly_fields = ('created_at', 'updated_at')
        save_on_top = True
        save_as = True
        class Meta:
            model = Project
            verbose_name = 'Project'
            verbose_name_plural = 'Projects'




# these models are form home page
admin.site.register(HomepageProfile)
admin.site.register(ServicesSlider)
admin.site.register(Testimonial,TestimonialAdmin)
admin.site.register(Achievements)

# these models are from about page
admin.site.register(Subscribers)
admin.site.register(Mailmessage)
admin.site.register(AboutPersonalAwards)
admin.site.register(AboutServices)
admin.site.register(AboutProfile)
admin.site.register(Aboutskills)
admin.site.register(Socialmedia)





# these models for blog page
admin.site.register(Blog,blogAdmin)

# these models for project page
admin.site.register(Project,projectAdmin)

# these models for my work page
admin.site.register(Repositary)

# these models are from contact page
admin.site.register(Adress)
admin.site.register(Contact)