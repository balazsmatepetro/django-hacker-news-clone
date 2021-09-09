from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Comment, NewsItem


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': _('Your comment goes here...'),
            'rows': 4,
        }),
    )

    class Meta:
        model = Comment
        fields = ('content',)


class SubmitForm(forms.ModelForm):
    title = forms.CharField(
        label=_('Title'),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    url = forms.URLField(
        label=_('URL'),
        widget=forms.URLInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = NewsItem
        fields = ('title', 'url')
