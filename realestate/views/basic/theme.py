from django.forms import model_to_dict

from realestate.models import AboutUs


def get_about_us():
    data_model = AboutUs.objects.all()
    about_us = {

    }
    if not data_model:
        return about_us

    about_us = model_to_dict(data_model[0])
    return about_us
