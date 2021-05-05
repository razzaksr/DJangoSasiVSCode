from django import forms
from crudl.models import Candidates, Companies
class CandidatesForm(forms.ModelForm):
    class Meta:
        model=Candidates
        fields="__all__"

class CompaniesForm(forms.ModelForm):
    class Meta:
        model=Companies
        fields="__all__"