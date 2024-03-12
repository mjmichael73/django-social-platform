from django import forms
from images.models import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["title", "image_file", "description"]

    def clean_image_file(self):
        uploaded_image_file = self.cleaned_data["image_file"]
        uploaded_image_file_name = uploaded_image_file.name
        valid_extensions = ["jpg", "jpeg", "png"]
        extension = uploaded_image_file_name.rsplit(".", 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError("The given Image file extension not match valid image extensions.")
        return uploaded_image_file

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        uploaded_image_file = self.cleaned_data["image_file"]
        uploaded_image_name = uploaded_image_file.name
        name = slugify(self.cleaned_data["title"])
        extension = uploaded_image_name.rsplit(".", 1)[1].lower()
        new_file_name = f"{name}.{extension}"
        image.image_file.save(
            new_file_name,
            ContentFile(uploaded_image_file.read()),
            save=False
        )
        if commit:
            image.save()
        return image
