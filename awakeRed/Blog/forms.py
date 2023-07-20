from django import forms
from .models import Tweet, Publicacion

# asociado a un modelo
class TweetForm(forms.ModelForm):
    cuerpo = forms.CharField(required = True,
                widget= forms.widgets.Textarea(
                    attrs={
                        "placeholder": "Escribe tu tweet aca",
                        "class": "textarea is-success is-medium",
                    }
                ))
    class Meta:
        model = Tweet
        fields = ["cuerpo"]


# formulario no ligado a un modelo
class ContactoForm(forms.Form):
    texto = forms.CharField(label = 'Contactanos')
    check = forms.BooleanField(label='acepta las politicas', required=False)
