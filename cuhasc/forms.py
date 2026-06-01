from django import forms

from cuhasc.models import Member, Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name']
