from django import forms

class CryptoForm(forms.Form):
    kode_crypto = forms.CharField(label="Kode Crypto", max_length=4)
    nama_crypto = forms.CharField(label="Nama Crypto", max_length=255)
    harga_crypto = forms.IntegerField(label="Harga Crypto")
    risk = forms.CharField(label="Risk")
    
class NotesForm(forms.Form):
    note = forms.CharField(label="Notes", max_length=255)