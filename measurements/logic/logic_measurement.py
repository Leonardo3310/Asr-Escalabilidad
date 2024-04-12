from ..models import Measurement

def get_measurements():
    queryset = Measurement.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_measurement(form):
    last_measurement = Measurement.objects.last()
    new_value = 1  # valor predeterminado si no existen mediciones
    if last_measurement:
        new_value = last_measurement.value + 1

    new_measurement = form.save()
    new_measurement.value = new_value
    new_measurement.save()
    return ()