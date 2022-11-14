from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Customers, OrderItems, Orders , CustomerCompanies, Deliveries
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.db.models import F, Func, Value, CharField


# Create your views here.

@csrf_exempt
def orderApi(request,id=1):
    if request.method == "GET" or request.environ['HTTP_ACCESS_CONTROL_REQUEST_METHOD']:
        data = OrderItems.objects.all().select_related('order_id','order_id__customer_id').prefetch_related('deliveries_set').annotate(date=Func(F('order_id__created_at')
                                     ,Value('DD-MM-YYYY HH:MM:SS'),function='to_char',output_field=CharField())).values('order_id__order_name', 'order_id__customer_id__company_id__company_name',
                                     'order_id__customer_id__user_id','date','deliveries__delivered_quantity',
                                     'quantity'
                                    )
        json_data = json.dumps(list(data),cls=DjangoJSONEncoder)
        #json_data = serializers.serialize('json',data)
        return JsonResponse(json_data,safe=False)
