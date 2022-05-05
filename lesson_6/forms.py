from django import forms
from durationwidget.widgets import TimeDurationWidget
from lesson_5.models import Client


class MyForm(forms.Form):
    name = forms.CharField(label='User Name', initial='User name')#, disabled=True, required=False)
    profile_picture = forms.ImageField(widget=forms.FileInput)
    additional_file = forms.FileField(widget=forms.FileInput)
    email = forms.EmailField(initial='admin@admin.admin', error_messages={'required': 'Please enter your email'})
    password = forms.CharField(max_length=20, min_length=6,
                               widget=forms.PasswordInput())
    age = forms.IntegerField(required=False, help_text='Enter your current age')
    agreement = forms.BooleanField(required=False)
    average_score = forms.FloatField(initial=10.1)
    birthday = forms.DateField(widget=forms.SelectDateWidget, required=False)
    work_experience = forms.DurationField(required=False)#widget=TimeDurationWidget)
    sex = forms.ChoiceField(choices=[("1", "Yes, pls"), ("2", "No, thx")], required=False)


class FormFromModel(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        # fields = ['user', 'second_email']
