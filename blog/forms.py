from django import forms
from .models import Post, Comment

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = ['text',]
        exclude = ('user_id','time','replay','post_id')
