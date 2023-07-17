from django import forms
from .models import Post, Category
from django.contrib.auth import get_user_model


# choices = [
#    ("coding", "coding"),
#    ("sports", "sports"),
#    ("entertainment", "entertainment"),
# ]

User = get_user_model()

choices = Category.objects.all().values_list("name", "name")

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "author", "category", "body")

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Add Your Title ..."}
            ),
            "title_tag": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Add The Title Tag ..."}
            ),
            "category": forms.Select(
                choices=choice_list,
                attrs={
                    "class": "form-control",
                },
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Add The Blog Post Body ...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["author"] = forms.ModelChoiceField(
            queryset=User.objects.filter(pk=user.pk),
            initial=user.pk,
            widget=forms.Select(attrs={"class": "form-control"}),
        )


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "body")

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Add Your Title ..."}
            ),
            "title_tag": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Add The Title Tag ..."}
            ),
            # "author": forms.Select(
            # attrs={
            # "class": "form-control",
            # }
            # ),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Add The Blog Post Body ...",
                }
            ),
        }
