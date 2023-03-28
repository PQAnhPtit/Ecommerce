# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from cart.models import cart_details
from django.http import JsonResponse
import json


@csrf_exempt
def add_cart_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        cart = cart_details.objects.create(
            user_id=data['user_id'],
            product_id=data['product_id'],
            amount=data['amount'],
            price=data['price']
        )

        resp = {}
        if cart:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = {
                'id': cart.id,
                'user_id': cart.user_id,
                'product_id': cart.product_id,
                'amount': cart.amount,
                'price': cart.price
            }
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Data is invalid.'

        return HttpResponse(json.dumps(resp), content_type='application/json')

    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid request method'
        })



@csrf_exempt
def delete_cart_data(request, id):
    try:
        cart = cart_details.objects.get(id=id)
        cart.delete()
        resp = {
            'status': 'Success',
            'status_code': '200',
            'message': 'deleted successfully.'
        }
    except cart_details.DoesNotExist:
        resp = {
            'status': 'Failed',
            'status_code': '404',
            'message': 'not found.'
        }
    return HttpResponse(json.dumps(resp), content_type='application/json')
