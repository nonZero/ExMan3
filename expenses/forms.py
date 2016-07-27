from django import forms

from expenses.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'body_markdown',
        )
