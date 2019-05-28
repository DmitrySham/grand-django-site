from django import forms
from .models import ApplyRequest


class ApplyRequestForm(forms.ModelForm):
    class Meta:
        model = ApplyRequest
        fields = ('name', 'email', 'education', 'phone', 'message', 'course')

    def __init__(self, *args, **kwargs):
        super(ApplyRequestForm, self).__init__(*args, **kwargs)

        self.fields['message'].required = False

        self.fields['course'].widget = forms.HiddenInput(attrs={
            'value': self.initial['course'].id if self.initial['course'] else ''
        })
