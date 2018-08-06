from django import forms
from app.models import Student

# class student_form(forms.ModelForm):
#     name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
#     # emailid = forms.EmailField(widget=forms.EmailField( is_hidden=False ), required=True, max_length=100)
#     contact_no = forms.CharField(widget=forms.NumberInput(), required=True, max_length=10)
#     # city = forms.CharField(widget=forms.TextInput(),required=False, max_length=100)
#     # marks = forms.CharField(widget=forms.NumberInput(),required=True, max_length=10)

# BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
# FAVORITE_COLORS_CHOICES = (
#     ('blue', 'Blue'),
#     ('green', 'Green'),
#     ('black', 'Black'),
# )
class LoginForm(forms.ModelForm):
    BRANCH_CHOICES=(('cse','CSE'),('me','ME'),('ec','EC'))
    YEAR_CHOICES=(('1','1st year'),('2','2nd year'),('3','3rd year'),('4','4th year'))
    name = forms.CharField(widget=forms.TextInput(), required=True ,max_length = 20)
    emailid = forms.CharField(widget=forms.TextInput(), required=True ,max_length = 30)
    rollno = forms.CharField(widget=forms.NumberInput(), required=True , max_length=12)
    # branch = forms.MultipleChoiceField(
    #     required=True,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=BRANCH_CHOICES,
    # ) # forms.CharField(widget=forms.TextInput(), required=True ,max_length=5)
    # year = forms.MultipleChoiceField(
    #     required=True,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=YEAR_CHOICES,
    # )
    branch = forms.ChoiceField(widget=forms.RadioSelect(),choices=BRANCH_CHOICES,required=True)
    year = forms.ChoiceField(widget=forms.RadioSelect(),choices=YEAR_CHOICES,required=True)
     #forms.CharField(widget=forms.NumberInput(), required=True , max_length=2)
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    # favorite_colors = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=FAVORITE_COLORS_CHOICES,
    #     )
    class Meta():
        model=Student
        fields=['name','emailid','rollno','branch','year']
