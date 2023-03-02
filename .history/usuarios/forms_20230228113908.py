from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex: João Souza"})
    )
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Digite sua senha"})
    )
    
class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex: João Souza"})
    )