from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm
from django.contrib import messages

#def home(request):
# return render(request, 'app/home.html')

class ProductView(View):
	def get(self, request):
		tablets_capsules = Product.objects.filter(category='TC')
		supplements = Product.objects.filter(category='S')
		general = tablets_capsules | supplements
		herbs = Product.objects.filter(category='H')
		health_drinks = Product.objects.filter(category='HD')
		ayurvedic = herbs | health_drinks
		covid_essentials = Product.objects.filter(category='CE')
		personal_care = Product.objects.filter(category='PC')
		healthcare = covid_essentials | personal_care
		return render(request, 'app/home.html', {'tablets_capsules' : tablets_capsules,'supplements' : supplements,'general' : general,'herbs' : herbs,'health_drinks' : health_drinks,'ayurvedic' : ayurvedic,'covid_essentials' : covid_essentials,'personal_care' : personal_care,'healthcare' : healthcare })


#def product_detail(request):
# return render(request, 'app/productdetail.html')

class ProductDetailView(View):
	def get(self, request, pk):
		product = Product.objects.get(pk=pk)
		return render(request, 'app/productdetail.html', {'product' : product})


def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def tablets_capsules(request):
	tablets_capsules = Product.objects.filter(category='TC')
	return render(request, 'app/tablets_capsules.html', {'tablets_capsules' : tablets_capsules})

def supplements(request):
	supplements = Product.objects.filter(category='S')
	return render(request, 'app/supplements.html', {'supplements' : supplements})

def herbs(request):
	herbs = Product.objects.filter(category='H')
	return render(request, 'app/herbs.html', {'herbs' : herbs})

def health_drinks(request):
	health_drinks = Product.objects.filter(category='HD')
	return render(request, 'app/health_drinks.html', {'health_drinks' : health_drinks})

def covid_essentials(request):
	covid_essentials = Product.objects.filter(category='CE')
	return render(request, 'app/covid_essentials.html', {'covid_essentials' : covid_essentials})

def personal_care(request):
	personal_care = Product.objects.filter(category='PC')
	return render(request, 'app/personal_care.html', {'personal_care' : personal_care})

class CustomerRegistrationView(View):
	def get(self, request):
		form = CustomerRegistrationForm()
		return render(request, 'app/customerregistration.html', {'form' : form})
	
	def post(self, request):
		form = CustomerRegistrationForm(request.POST)
		if form.is_valid():
			messages.success(request, 'Congratulations!! Registered Successfully')
			form.save()
		return render(request, 'app/customerregistration.html', {'form' : form})

def checkout(request):
 return render(request, 'app/checkout.html')
