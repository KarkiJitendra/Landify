from mainapp.models import ContactMessage
from django import forms    

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Name', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Email', 'required': 'required'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Subject', 'required': 'required'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Message', 'rows': '5', 'required': 'required'})
        
        