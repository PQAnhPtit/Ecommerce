# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from img.models import img_details
from django.http import JsonResponse
import json


@csrf_exempt
def add_img_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        img = img_details.objects.create(
            link=data['link'],
            description=data['description'],
        )

        resp = {}
        if img:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = {
                'id': img.id,
                'link': img.link,
                'description': img.description
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



