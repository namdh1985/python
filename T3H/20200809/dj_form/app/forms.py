from django import forms
class CustomerForm(forms.Form):
    fullname = forms.CharField(max_length=50, label='Họ tên')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=20, label='Số điện thoại')
    address = forms.CharField(max_length=200, label='Địa chỉ'
                , required=False
                , widget=forms.Textarea(attrs={'row':2, 'cols':23}))
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        if not phone.isdigit() or phone[0] != '0':
            raise forms.ValidationError('Số điện thoại không hợp lệ')
        return phone