from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from customer_model.models import user_registration

### This function is created for validating the user.
def user_validation(uname, password):
    user_data = user_registration.objects.filter(email = uname, password = password)
    if user_data:
        return "Valid User"
    else:
        return "Invalid User"


@csrf_exempt
def user_login(request):
    uname = request.POST.get("User Name")
    password = request.POST.get("Password")
    resp = {}
    if uname and password:
        respdata = user_validation(uname, password)
        if respdata == "Valid User":
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Welcome to Ecommerce website......'
        elif respdata == "Invalid User":
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Invalid credentials.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type='application/json')


