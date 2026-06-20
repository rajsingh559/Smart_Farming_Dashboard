from django import forms
from .models import Feedback, Rating
from accounts.forms import BootstrapFormMixin

class FeedbackRatingForm(BootstrapFormMixin, forms.Form):
    feedback_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Tell us about your experience using the dashboard...',
            'rows': 4
        }),
        required=True,
        label="Feedback Comments"
    )
    score = forms.ChoiceField(
        choices=[(i, f"{i} Stars") for i in range(1, 6)],
        initial=5,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Overall Rating"
    )
