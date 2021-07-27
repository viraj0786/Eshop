from django.contrib.auth.hashers import  check_password
from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        pasword = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(pasword, customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message = 'email or pass invaild'
        else:
            error_message = 'email or password invaild'
        print(customer)
        print(email, pasword)
        return render(request, 'login.html', {'error': error_message})
