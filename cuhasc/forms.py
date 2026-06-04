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
        for item_data in items:
            labels = scales[item_data['scale']]
            choices = [(str(i + 1), label or str(i + 1)) for i, label in enumerate(labels)]
            self.fields[item_data['item']] = forms.ChoiceField(
                choices=choices,
                widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                label=f"{item_data['item']}: {item_data['content']}",
            )

    def save_results(self, member):
        for item_data in self._items:
            value = int(self.cleaned_data[item_data['item']])
            QResult.objects.update_or_create(
                member=member,
                item=item_data['item'],
                defaults={'scale': item_data['scale'], 'value': value},
            )
