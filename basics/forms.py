from django import forms
from basics.models import Candidates
class CandidatesForm(forms.ModelForm):
    class Meta:
        model=Candidates
        fields="__all__"