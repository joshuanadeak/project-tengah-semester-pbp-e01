from django import forms
from suggestionbox.models import UserFeedback

class FeedbackForm(forms.Form):
    feedback = forms.CharField(label="Feedback", max_length=1000, widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))
    reply = forms.CharField(label="Reply", max_length=1000, widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))

class ReplyFeedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ['reply']