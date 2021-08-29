from ..models import Measurement


def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements


def get_measurements_by_pk(pk_p):
    measurements = Measurement.objects.get(pk=pk_p)
    return measurements


def delete_measurements_by_pk(pk_p):
    get_measurements_by_pk(pk_p).delete()


def update_measurements_by_pk(pk_p, name_value_p, new_value_p):
    measurement = get_measurements_by_pk(pk_p)
    if name_value_p == 'value':
        measurement.value = int(new_value_p)
    elif name_value_p == 'unit':
        measurement.unit = new_value_p
    elif name_value_p == 'place':
        measurement.place = new_value_p

    measurement.save()
    return measurement

