from django import forms
from django.conf import settings
from qa.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description', 'tags']
        help_texts={
            'title':'见名思议',
            'tags':'',
        }
        labels ={
            'title':'标题',
            'description':'描述',
            'tags':'标签'
        }
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        try:
            settings.QA_SETTINGS['qa_description_optional']
            self.fields['description'].required = not settings.QA_SETTINGS[
                'qa_description_optional']

        except KeyError:
            pass