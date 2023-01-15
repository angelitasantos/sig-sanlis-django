from django import forms
from .models import Estoque, EstoqueItens
from plataform.models import Item


class EstoqueForm(forms.ModelForm):

    class Meta:
        model = Estoque
        fields = '__all__'


class EstoqueItensEntradaForm(forms.ModelForm):

    class Meta:
        model = EstoqueItens
        fields = '__all__'


class EstoqueItensSaidaForm(forms.ModelForm):

    class Meta:
        model = EstoqueItens
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(EstoqueItensSaidaForm, self).__init__(*args, **kwargs)
        # Retorna somente produtos com estoque maior do que zero.
        self.fields['produto'].queryset = Item.objects.filter(stock_qtd__gt=0)
