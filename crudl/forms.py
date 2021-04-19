from django import forms
from crudl.models import Candidates
class CandidatesForm(forms.ModelForm):
    class Meta:
        model=Candidates
        fields="__all__"