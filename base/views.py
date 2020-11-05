from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Product, Order , Lesson
from django.shortcuts import redirect
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, get_object_or_404
from users.models import Profile
from .forms import ShareForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def simpleCheckout(request):
	return render(request, 'base/simple_checkout.html')

def home_page(request):
	kek = Product.objects.all()
	paginator = Paginator(kek, 5)

	page_number = request.GET.get('page')
	products = paginator.get_page(page_number)
	context = {'products': products}

	return render(request, 'base/index.html', context)

def store(request):
	kek = Product.objects.all()

	paginator = Paginator(kek, 9)

	page_number = request.GET.get('page')
	products = paginator.get_page(page_number)
	context = {'products':products}
	return render(request, 'base/store.html', context)

	
@login_required
def checkout(request, pk):
	product = Product.objects.get(id=pk)
	
	profiles = Profile.objects.filter(usr=request.user).prefetch_related("members")
	for profile in profiles:
		members = profile.members.all()
	for member in members:
		mid = member
		print(mid)			
	
		#product.students.add(mid)	
		
			
		
			
	
		


	

	context = {'product':product,
				'profiles':profiles,
				'members':members,
				 }
	return render(request, 'base/checkout.html', context)

def mycourses(request):
	kek = Product.objects.filter(Q(students=request.user) | Q(free=True)).order_by('free')

	paginator = Paginator(kek, 9)

	page_number = request.GET.get('page')
	products = paginator.get_page(page_number)
	context = {'products':products}
	return render(request, 'base/my_courses.html', context)


@login_required
def share(request, pk):
	product = Product.objects.get(id=pk)
	
	profiles = Profile.objects.filter(usr=request.user).prefetch_related("members")
	for profile in profiles:
		members = profile.members.all()
	for member in members:
		mid = member
		print(mid)			
	
		product.students.add(mid)	
		
			
		
			
	
		


	

	context = {'product':product,
				'profiles':profiles,
				'members':members,
				 }
	return render(request, 'base/shared.html', context)

		


class LessonDetailView(LoginRequiredMixin, View):

    def get(self, request, lesson_slug,pk, *args, **kwargs):
        course = get_object_or_404(Product, id=pk)
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        context = { 'lesson': lesson,
					'course': course}
        return render(request, "base/lesson_detail.html",context)

def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Product.objects.get(id=body['productId'])
	product.students.add(request.user)
	Order.objects.create(
		product=product
		)

	return redirect('/', safe=False)