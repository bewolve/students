from django.forms.models import ModelForm
from .models import Student, Bus


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = ['manager',]
        
    
class BusForm(ModelForm):
    class Meta:
        model = Bus
        fields = "__all__"
