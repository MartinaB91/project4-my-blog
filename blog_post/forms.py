from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "category",
            "content",
            "post_img",
            "meta_description"
            )


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "category",
            "content",
            "post_img",
            "meta_description"
            )
