from django import forms



class DateInput(forms.DateInput):
    input_type = 'date'    


class CreateNewTask(forms.Form):
    
    name = forms.CharField(label = "nombre de dueño", max_length = 200)    
    type_agend = forms.ChoiceField( label="tipo de agenda", widget=forms.RadioSelect, choices=[("familiar", "familiar"), ("trabajo", "trabajo")])
    date = forms.DateField(widget=DateInput, label="fecha de registro")
    description = forms.CharField(widget=forms.Textarea, label="descripción")
    

        