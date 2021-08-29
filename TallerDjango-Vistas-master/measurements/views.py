from .logic.logic_measurements import *
from django.http import HttpResponse
from django.core import serializers
import json
from django.forms.models import model_to_dict


def get_measurements(request):
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type='application/json')


def get_measurement_by_id(request, pk_p):
    measurements = get_measurements_by_pk(pk_p)
    measurement_by_pk = serializers.serialize('json', [measurements, ])
    return HttpResponse(measurement_by_pk, content_type='application/json')


def delete_measurement_by_id(request, pk_p):
    delete_measurements_by_pk(pk_p)
    return HttpResponse("Se borró el item con id "+str(pk_p))


def update_measurement_by_id(request, pk_p, name_value_p, new_value_p):
    measurement = update_measurements_by_pk(pk_p, name_value_p, new_value_p)
    measurement_by_pk = serializers.serialize('json', [measurement, ])
    return HttpResponse(measurement_by_pk, content_type='application/json')
