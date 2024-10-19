from django import forms

class EmployeeForm(forms.Form):
    employeeid=forms.IntegerField()
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
    designation=forms.CharField(max_length=50)
    phonenumber=forms.IntegerField()


class FormClass(forms.Form):
    name=forms.CharField(min_length=3,max_length=2,required=True,initial="Enter the name",label="Full name",disabled=True)
    password=forms.CharField(min_length=4,max_length=16,widget=forms.PasswordInput())
    age=forms.IntegerField(min_value=18,max_value=40,initial=18)
    salary=forms.DecimalField(max_digits=6,decimal_places=2)
    email=forms.EmailField()
    is_active=forms.BooleanField()
    date=forms.DateField()
    day=forms.ChoiceField(choices=[('Mon','MONDAY'),('Tue','TUESDAY'),('Wed','WEDNESDAY'),('Thu','THURSDAY'),('Fri','FRIDAY'),('sat','SATURDAY')])
    hobbies=forms.MultipleChoiceField(choices=[('carrom','CARROM'),('books','BOOKS'),('football','FOOTBALL'),('cricket','CRICKET')])
    gender=forms.ChoiceField(choices=[('M','MALE'),('F','FEMALE')],widget=forms.RadioSelect())
    time=forms.TimeField()
    fileupload=forms.FileField()
    imageupload=forms.ImageField
    url=forms.URLField()
    address=forms.CharField(max_length=200,widget=forms.Textarea())
    txtarea=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"textareaforthisbox"}))
























