from django import forms
from django.contrib.auth.models import User


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        qs = User.objects.exclude(
            id=self.instance.id
        ).filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is already in use.")
        return email
