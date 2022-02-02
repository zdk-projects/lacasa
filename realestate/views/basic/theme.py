import re

from django.forms import model_to_dict

from realestate.models import AboutUs, HouseListing


def get_about_us():
    data_model = AboutUs.objects.all()
    # @TODO: News need to be update

    d_news = HouseListing.objects.all().order_by('list_date')[:3]
    news = []
    # image, date, title, description, slug
    for item in d_news:
        image = item.photo_main
        title = item.title
        description = item.description
        description = str(description).replace("  ", " ").strip().rstrip()
        description = re.sub(r'[^A-Za-z0-9 ]+', '', description)

        data_title = title
        if len(title) > 18:
            title = title[:16] + ".."
        if len(description) > 35:
            description = description[:32] + "..."

        date = item.list_date.strftime("%d-%m-%Y")
        slug = item.slug
        news.append(
            {
                'image': image,
                'title': title,
                'data_title': data_title,
                'description': description,
                'date': date,
                'slug': slug,

            }
        )

    about_us = {

    }
    if not data_model:
        return about_us

    about_us = model_to_dict(data_model[0])
    about_us['news'] = news

    return about_us
