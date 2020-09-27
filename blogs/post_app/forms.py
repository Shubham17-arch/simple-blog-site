from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'snippet')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'authorid', 'type':'hidden'}),
            # 'author' : forms.Select(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ( 'title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            # 'author' : forms.Select(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')