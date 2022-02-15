from django.forms import CharField, Form


class CharFieldDisabled(CharField):
    def __init__(self, *args, **kwargs):
        kwargs["disabled"] = True
        kwargs["required"] = False
        super().__init__(*args, **kwargs)


class DeleteObjectForm(Form):

    class Media:
        js = ('js/delete_object_form.js',)
