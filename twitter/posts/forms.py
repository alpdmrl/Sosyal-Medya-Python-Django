from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'resim']
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})