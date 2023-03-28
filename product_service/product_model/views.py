# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from product_model.models import product_details
from django.http import JsonResponse
import json
import requests
from requests import Response

@csrf_exempt
def get_book(request):
    url = 'http://127.0.0.1:9001/getbook/'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    return HttpResponse(json.dumps(val1), content_type='application/json')


@csrf_exempt
def get_clothe(request):
    url = 'http://127.0.0.1:9002/getclothe/'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    return HttpResponse(json.dumps(val1), content_type='application/json')


@csrf_exempt
def get_shoe(request):
    url = 'http://127.0.0.1:9003/getshoe/'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    return HttpResponse(json.dumps(val1), content_type='application/json')

@csrf_exempt
def get_electronic(request):
    url = 'http://127.0.0.1:9004/getelectronic/'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    return HttpResponse(json.dumps(val1), content_type='application/json')





# @csrf_exempt
# def get_product_data(request):
#     data = []
#     resp = {}
#     # This will fetch the data from the database.
#     prodata = product_details.objects.all()
#     for tbl_value in prodata.values():
#         data.append(tbl_value)
#     # If data is available then it returns the data.
#     if data:
#         resp['status'] = 'Success'
#         resp['status_code'] = '200'
#         resp['data'] = data
#     else:
#         resp['status'] = 'Failed'
#         resp['status_code'] = '400'
#         resp['message'] = 'Data is not available.'
#     return HttpResponse(json.dumps(resp), content_type='application/json')
#
#
# @csrf_exempt
# def add_product_data(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#
#         product = product_details.objects.create(
#             product_id=data['product_id'],
#             product_category=data['product_category'],
#             product_name=data['product_name'],
#             availability=data['availability'],
#             price=data['price']
#         )
#
#         resp = {}
#         if product:
#             resp['status'] = 'Success'
#             resp['status_code'] = '200'
#             resp['data'] = {
#                 'id': product.id,
#                 'product_id': product.product_id,
#                 'product_category': product.product_category,
#                 'product_name': product.product_name,
#                 'availability': product.availability,
#                 'price': product.price
#             }
#         else:
#             resp['status'] = 'Failed'
#             resp['status_code'] = '400'
#             resp['message'] = 'Data is invalid.'
#
#         return HttpResponse(json.dumps(resp), content_type='application/json')
#
#     else:
#         return JsonResponse({
#             'status': 'error',
#             'message': 'Invalid request method'
#         })
#
#
# @csrf_exempt
# def update_product_data(request, product_id):
#     resp = {}
#     # Get the product instance to update
#     try:
#         product = product_details.objects.get(product_id=product_id)
#     except product_details.DoesNotExist:
#         resp['status'] = 'Failed'
#         resp['status_code'] = '400'
#         resp['message'] = 'Product not found.'
#         return HttpResponse(json.dumps(resp), content_type='application/json')
#
#     # Parse the request data
#     try:
#         data = json.loads(request.body)
#     except json.JSONDecodeError:
#         resp['status'] = 'Failed'
#         resp['status_code'] = '400'
#         resp['message'] = 'Invalid JSON data.'
#         return HttpResponse(json.dumps(resp), content_type='application/json')
#
#     # Update the product instance
#     for key, value in data.items():
#         setattr(product, key, value)
#     product.save()
#
#     # Return success response
#     resp['status'] = 'Success'
#     resp['status_code'] = '200'
#     resp['data'] = {
#         'id': product.id,
#         'product_id': product.product_id,
#         'product_category': product.product_category,
#         'product_name': product.product_name,
#         'availability': product.availability,
#         'price': product.price
#     }
#     return HttpResponse(json.dumps(resp), content_type='application/json')
#
#
# @csrf_exempt
# def delete_product_data(request, product_id):
#     try:
#         product = product_details.objects.get(product_id=product_id)
#         product.delete()
#         resp = {
#             'status': 'Success',
#             'status_code': '200',
#             'message': 'Product deleted successfully.'
#         }
#     except product_details.DoesNotExist:
#         resp = {
#             'status': 'Failed',
#             'status_code': '404',
#             'message': 'Product not found.'
#         }
#     return HttpResponse(json.dumps(resp), content_type='application/json')


