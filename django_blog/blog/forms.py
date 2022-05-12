from django import forms 
from .models import Comment, Post

class CreateTitle(forms.ModelForm):
 class Meta:
        model = Post
        fields = ("title",)
        labels = {"title": "タイトル",}
        widgets = {
            "title" : forms.TextInput(
                attrs = {
                    "type" : "text",
                    "class" : "form-control", 
                    "placeholder" : "タイトルを入力して下さい",
                    "name" : "title",
                }

            )
        }

class CreatePost(forms.ModelForm):
 class Meta:
        model = Post
        fields = ("text",)
        labels = {"text": "内容",}
        widgets = {
            "text" : forms.Textarea(
                attrs = {
                    "class" : "form-control",
                    "placeholder" : "内容",
                    "rows" : "5",
                }

            )
        }

class CreateImage(forms.ModelForm): #Postのところで記述増やすのが正しいかも
    class Meta:
        model = Post
        fields = ('title', 'link','image')


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("text",)
        labels = {"text": "コメント",}
        widgets = {
            "text" : forms.Textarea(
                attrs = {
                    "class" : "form-control",
                    "placeholder" : "内容",
                    "rows" : "5",
                    # "name" : "body", 元のHTMLでnameがbodyになっているがいるがどこで指定・・・？
                    # フィールドにbodyはないのでbodyの指定はできない？
                }

            )
        }