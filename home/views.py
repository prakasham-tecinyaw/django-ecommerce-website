from django.http.request import HttpHeaders
from home.models import Account
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from home.forms import AccountAuthenticationForm, RegistrationForm, ProfileUpdateForm

# micro views import
from shop.micro_views import home_page_shop_list, total_cart_quantity
# Create your views here.

def HomePage( request, *args, **kwargs ):

    if request.user.is_authenticated:
        customer = request.user
        shops = home_page_shop_list()
        orders = total_cart_quantity(customer)
        context ={'shops':shops,'get_cart_total':orders}
    # return object
    else:
        shops = home_page_shop_list()
        context ={'shops':shops}

    return render( request, 'index.html', context ) 

def RegisterView( request, *args, **kwargs ):

    user = request.user

    if user.is_authenticated:
        return redirect( 'home' )
    
    context = { }

    if request.POST:
        form = RegistrationForm( request.POST )

        if form.is_valid():

            form.save()

            email = form.cleaned_data.get( 'email' ).lower()

            raw_password = form.cleaned_data.get( 'password1' )

            account = authenticate( email = email, password = raw_password )

            login( request, account )

            destination = kwargs.get( "next" )

            if destination: # if destinaton != None

                return redirect( destination )

            return redirect( "home" )
        else:
            context[ 'registration_form' ] = form

    return render( request, 'account/sign_up.html', context )

def LogoutView( request, *args, **kwargs ):

    logout( request )

    return redirect( 'home' )

def LoginView( request, *args, **kwargs ):

    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect( 'home' )

    destination = get_redirect_if_exists(request)
    print("destination: " + str(destination))

    if request.POST:
        form = AccountAuthenticationForm( request.POST )

        if form.is_valid():

            email = request.POST['email']

            password = request.POST['password']

            user = authenticate( email = email, password = password )

            if user:
                login( request, user )

                if destination:

                    return redirect( destination )

                return redirect ( "home" )
        else:
            context['login_form'] = form

    return render( request, "account/login.html", context )

def get_redirect_if_exists(request):
	redirect = None

	if request.GET:

		if request.GET.get("next"):

			redirect = str(request.GET.get("next"))

	return redirect

# def PasswordChangeView(request, *args, **kwargs):
#     return render( request, 'account/password/password_change.html' )

@login_required(login_url='login')
def ProfileView(request, *args, **kwargs):

    context = {}
    user_id = kwargs.get("user_id")
    try:
        account = Account.objects.get(pk=user_id)
    except:
        return HttpResponse("Something went wrong.")
    if account:
        context['id'] = account.id
        context['full_name'] = account.full_name
        context['address'] = account.address
        context['phone_number'] = account.phone_number
        context['email'] = account.email
        context['date_joined'] = account.date_joined
        context['is_active'] = account.is_active

        orders = total_cart_quantity(user_id)
        context['get_cart_total'] = orders

    return render(request, "account/profile.html", context)

@login_required(login_url='login')
def EditProfileView( request, *args, **kwargs):

    user_id = kwargs.get("user_id")
    account = Account.objects.get(pk=user_id)

    if account.pk != request.user.pk:

        return HttpResponse("You cannot edit someone elses profile.")

    context ={}

    if request.POST:
        form = ProfileUpdateForm( request.POST, instance=request.user )
        if form.is_valid():
            form.save()
            # new_username = form.cleaned_data['username']
            return redirect("profile", user_id=account.pk)
        else:
            form = ProfileUpdateForm( request.POST, instance=request.user,
                 initial = {
                     "id": account.pk,
                     "email":account.email,
                     "full_name":account.full_name,
                     "address":account.address,
                     "phone_number":account.phone_number,

                 }
            )
            context['form'] = form
    else:
        form = ProfileUpdateForm(
                 initial = {
                     "id": account.pk,
                     "email":account.email,
                     "full_name":account.full_name,
                     "address":account.address,
                     "phone_number":account.phone_number,

                 }
            )

        context['form'] = form
    
    return render(request, 'account/edit_profile.html', context )