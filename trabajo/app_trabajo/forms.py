from django import forms


class ReclamoForm(forms.Form):

    nombre = forms.CharField(
        label="Nombre completo",
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Ingresá tu nombre completo"
        })
    )

    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            "placeholder": "Ingresá tu correo electrónico"
        })
    )

    tipo = forms.ChoiceField(
        label="Tipo de solicitud",
        choices=[
            ("reclamo", "Reclamo"),
            ("objeto_perdido", "Objeto perdido"),
            ("sugerencia", "Sugerencia"),
            ("otro", "Otro"),
        ]
    )

    estacion = forms.CharField(
        label="Estación",
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "¿En qué estación ocurrió?"
        })
    )

    fecha = forms.DateField(
        label="Fecha del incidente",
        widget=forms.DateInput(attrs={
            "type": "date"
        })
    )

    descripcion = forms.CharField(
        label="Descripción",
        widget=forms.Textarea(attrs={
            "placeholder": "Contanos qué sucedió...",
            "rows": 6
        })
    )


class LoginForm(forms.Form):

    usuario = forms.CharField(
        label="Usuario",
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Ingresá tu usuario"
        })
    )

    clave = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Ingresá tu contraseña"
        })
    )