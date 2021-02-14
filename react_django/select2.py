"""
Django-Select2 URL configuration.

Add `django_select` to your ``urlconf`` **if** you use any 'Model' fields::

    from django.urls import path


    path('select2/', include('django_select2.urls')),

"""
from django.urls import path

from django.http import JsonResponse
from django_select2.views import AutoResponseView


class ProducutAutoResponseView(AutoResponseView):

    def get(self, request, *args, **kwargs):
        """
        Return a :class:`.django.http.JsonResponse`.

        Example::

            {
                'results': [
                    {
                        'text': "foo",
                        'id': 123
                    }
                ],
                'more': true
            }

        """
        self.widget = self.get_widget_or_404()
        self.term = kwargs.get("term", request.GET.get("term", ""))
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return JsonResponse(
            {
                "results": [
                    {"text": self.widget.label_from_instance(obj),
                     "id": obj.pk,
                     "price": obj.price if hasattr(obj, "price") else None,
                     "density": obj.density if
                     hasattr(obj, "density") else None,
                     "width": obj.width if hasattr(obj, "width") else None}
                    for obj in context["object_list"]
                ],
                "more": context["page_obj"].has_next(),
            }
        )


app_name = "django_select2"

urlpatterns = [
    path("fields/auto.json", ProducutAutoResponseView.as_view(),
         name="auto-json"),
]
