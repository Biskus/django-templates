from django import forms
from app.models import Tag
from pprint import pprint
class ColoredRadioSelect(forms.RadioSelect):
    pass
    def render(self,**kw):
        ret = super().render(**kw)
        
        pprint(ret)
        return ret

class TagForm(forms.ModelForm):
    """
    choices = [
            ('primary','Primary'),
            ('secondary','Secondary'),
            ('success','Success'),
            ('danger','Danger'),
            ('warning','Warning'),
            ('info','Info'),
            ('light','Light'),
            ('dark','Dark'),
        ]
    """
    def __init__(self, *a,**kw):
        super(TagForm,self).__init__(*a,**kw)
        #self.fields['label'].empty_label = None
        #self.fields['label'].choices = [('2',[('asd','asdf2')])]
        #self.fields['label'].attr['class'] = 'hidden'
        #self.fields['label'].widget.attrs['class'] = 'hidden'
        #self.fields['label'].label_classes = ("hidden asdf","iosdafusdo")
        pprint(self.fields['label'].__dict__)
        #self.fields['label'].initial = "primary"
    #label = forms.ChoiceField(choices=choices, widget=ColoredRadioSelect)
    class Meta():
        model = Tag
        fields = ['name','label']
        widgets = {
            'label':forms.RadioSelect, 
            }
        
    
    