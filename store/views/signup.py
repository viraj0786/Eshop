from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer


class Singup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email

        }

        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustmer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }

            return render(request, 'signup.html', data)

    def validateCustmer(self, customer):
        error_message = None;
        #  firstname
        if (not customer.first_name):
            error_message = "first name req !!"
        elif len(customer.first_name) > 6:
            error_message = "first must be 4 cher"
        # lastname
        elif (not customer.last_name):
            error_message = "last must be req"
        elif len(customer.last_name) > 10:
            error_message = "last must be 4 cher"
        # phone
        elif (not customer.phone):
            error_message = "phone must be req"
        elif len(customer.phone) > 10:
            error_message = "phone must be 10 cher"
        # email
        elif (not customer.email):
            error_message = "email must be req"
        elif len(customer.email) > 40:
            error_message = "email must be 10 cher"
        # password
        elif (not customer.password):
            error_message = "password must be req"
        elif len(customer.password) > 10:
            error_message = "password must be 10 cher"
        # exists
        elif customer.isExists():
            error_message = 'email is already exists'

        return error_message
