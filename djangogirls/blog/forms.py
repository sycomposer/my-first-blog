#장고 form 양식을 사용하기 위해 forms calling
from django import forms
#
from .models import Post
#The name is PostForm because it is about Post.
#Form is able to create when formsModelForm is located between parenthesis.
class PostForm(forms.ModelForm):

#If you are written as a name, Meta inside the PostForm.
#Target model is "model=모델이름형식으로
#사용자에게 입력받을 부분은 fields=('1st column','2nd column', etc.)
#you can write as a form.
    class Meta:
        model = Post
        fields = ('title', 'text',)