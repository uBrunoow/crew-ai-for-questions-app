from django import forms


class AdminPasswordChangeForm(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Nova senha"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirme a nova senha"
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and new_password != confirm_password:
            self.add_error('confirm_password', "As senhas não coincidem.")

        return cleaned_data
