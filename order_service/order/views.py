# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from order.models import order_details
from django.http import JsonResponse
import json


@csrf_exempt
def add_order_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        order = order_details.objects.create(
            user_id=data['user_id'],
            cart_id=data['cart_id'],
            created_date=data['created_date'],
            total_price=data['total_price']
        )

        resp = {}
        if order:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = {
                'id': order.id,
                'user_id': order.user_id,
                'cart_id': order.cart_id,
                'created_date': order.created_date,
                'total_price': order.total_price
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
def delete_order_data(request, id):
    try:
        order = order_details.objects.get(id=id)
        order.delete()
        resp = {
            'status': 'Success',
            'status_code': '200',
            'message': 'deleted successfully.'
        }
    except order_details.DoesNotExist:
        resp = {
            'status': 'Failed',
            'status_code': '404',
            'message': 'not found.'
        }
    return HttpResponse(json.dumps(resp), content_type='application/json')
