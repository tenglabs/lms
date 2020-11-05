from django.urls import path
from . import views
from .views import LessonDetailView
urlpatterns = [


	#path('simple-checkout/', views.simpleCheckout, name="simple-checkout"),

    path('', views.home_page, name='home'),



	

    path('courses/', views.store, name="store"),
    path('my_courses/', views.mycourses, name="my_courses"),
    path('checkout/<int:pk>/', views.checkout, name="checkout"),
    path('checkout/<int:pk>/share', views.share, name="share"),
    #path('checkout/<int:pk>/like', PostLikeView.as_view(), name='post-like'),
    path('checkout/<int:pk>/<lesson_slug>',
         LessonDetailView.as_view(), name='lesson-detail'),
    path('complete/', views.paymentComplete, name="complete"),
]