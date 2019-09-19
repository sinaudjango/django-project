from django import forms

class ContactForm(forms.Form):
    nama            = forms.CharField(
        label       ='Nama Lengkap',
        max_length  =100,
        widget      = forms.TextInput(
            attrs={
                'class':'form-control col-sm-2',
                'placeholder':'Isi Nama Lengkap yaa',
                'id':'inputSuccess',
            }
        )

    )
    email           = forms.EmailField(
        label='Email',
        max_length=100,
        widget= forms.TextInput(
            attrs={
                'class': 'form-control col-sm-2',
                'placeholder': 'Isi Nama Lengkap yaa',
                'id': 'inputSuccess',

            }
        )

    )
    pesan           = forms.CharField(
        label='Pesan',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'rows':'4',
            }
        )

        )
    tanggal_lahir   = forms.DateField(
        label='Tanggal Lahir',
        widget=forms.SelectDateWidget(
            years=range(1980,2010,1),
            attrs={
                'class': 'form-control',
            }
        )

    )
    jenis_kelamin = forms.ChoiceField(
        label='Jenis kelamin',
        widget=forms.RadioSelect(),
        choices=[
            ('p', 'pria'),
            ('w', 'wanita')
        ]
    )

    agree           = forms.BooleanField()