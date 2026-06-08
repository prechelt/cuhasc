from django import forms

from cuhasc.models import Member, QResult, Team


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name']


class QuestionnaireForm(forms.Form):
    def __init__(self, items, scales, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._items = items
        for item in items:
            labels = scales[item.scale]
            choices = [(str(i + 1), label) for i, label in enumerate(labels)]
            self.fields[item.item] = forms.ChoiceField(
                choices=choices,
                widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                label=item.content,
            )

    def save_results(self, member):
        for item in self._items:
            value = int(self.cleaned_data[item.item])
            QResult.objects.update_or_create(
                member=member,
                item=item.item,
                defaults={'scale': item.scale, 'value': value},
            )
