from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = [
            "owners_name",
            "Address",
            "contact_number",
            "location",
            "amount",
            "length",
            "Area",
            "frontview",
            "leftsideview",
            "backsideview",
            "rightsideview",
            "payment_verification_slip",
            "citizenship_photo",
            "land_ownership_document_photo",
            "land_map_photo",
        ]
