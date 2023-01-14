from django import forms
from plataform.models import Partner, Item
from .models import Transaction, TransactionItems


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = (
                    'company',
                    'partner', 
                    'type_register', 
                    'status', 
                    'document', 
                    )


class TransactionItemsForm(forms.ModelForm):

    class Meta:
        model = TransactionItems
        fields = ('item', 'qtd', 'price_term', 'balance',)

