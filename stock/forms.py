from cProfile import label
from logging import PlaceHolder
from django import forms

class StockForm(forms.Form):
    kode_saham = forms.CharField(label="Kode Saham", max_length=4)
    nama_perusahaan = forms.CharField(label="Nama Perusahaan", max_length=255)
    harga_saham = forms.IntegerField(label="Harga",max_value=9999,min_value=0)
    risk = forms.CharField(label="Risk", max_length=4)
    
class NoteForm(forms.Form):
    catatan = forms.CharField(label="Catatan", max_length=255)
