# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from comment.models import comment_details
from django.http import JsonResponse
import json


@csrf_exempt
def add_comment_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        comment = comment_details.objects.create(
            user_id=data['user_id'],
            description=data['description'],
            created_date=data['created_date']
        )

        resp = {}
        if comment:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = {
                'id': comment.id,
                'user_id': comment.user_id,
                'description': comment.description,
                'created_date': comment.created_date
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



