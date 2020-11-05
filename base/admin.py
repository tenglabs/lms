
from django.contrib import admin
from django import forms
from .models import Product, Lesson , Order
#from ckeditor_uploader.widgets import CKEditorUploadingWidget


#class LessonAdminForm(forms.ModelForm):
#    content = forms.CharField(widget=CKEditorUploadingWidget())
#    class Meta:
#        model = Lesson
#        fields = '__all__'


class InLineLesson(admin.TabularInline):
   
    model = Lesson
    extra = 1
    max_num = 49



class CourseAdmin(admin.ModelAdmin):
    inlines = [InLineLesson]
    list_display = ('title', 'description' )


    
   
    fieldsets = (
        (None, {
            'fields': (
                
                'title',
                'free',
                'price',
                'cover_image',
                'description',
                
                
                'students'
            )
        }),
    )

admin.site.register(Product, CourseAdmin)