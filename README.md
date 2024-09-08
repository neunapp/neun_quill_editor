# Documentacion Neun Quill Editor

Este es un WidgetForm de Django muy **simple y sencillo** para poder tener Quill.js un Editor WYSIWYG de contenido open source muy porpular en JS. 

La idea es que se pueda integrar cualquier version de Quill.js y cualquier Tema css que provee este editor.

## ¿Como usar WidgetNeunQuillEditor?
Es muy senicllo, primero necesitamos indicar la version de Neun Quill desde el CDN en los settings

```
NEUN_QUILL_EDITOR_JS = 'https://cdn.jsdelivr.net/npm/quill@2.0.2/dist/quill.js'


Ahora Tambien puedes indicar el template o tema css en en los settings con la constante:

```
NEUN_QUILL_EDITOR_CSS = 'https://cdn.jsdelivr.net/npm/quill@2.0.2/dist/quill.snow.css'


Tambien puedes configurar las opciones de la barra de herramientas de que trae Quill

por defecto es:
```
toolbar_options = {
    'theme': 'snow',
    'modules': {
    }
}

Las opciones completas soportadas son:
```
NEUN_TOOLBAR_OPTIONS = {
    'modules': {
        'toolbar': [
            ['bold', 'italic', 'underline', 'strike'],        
            ['blockquote', 'code-block'],
            ['link', 'video', 'formula'],# no image
            [{'header': 1}, {'header': 2}],                   
            [{'list': 'ordered'}, {'list': 'bullet'}, {'list': 'check'}],
            [{'script': 'sub'}, {'script': 'super'}],        
            [{'indent': '-1'}, {'indent': '+1'}],             
            [{'direction': 'rtl'}],                           
            [{'size': ['small', 'false', 'large', 'huge']}],    
            [{'header': [1, 2, 3, 4, 5, 6, 'false']}],
            [{'color': []}, {'background': []}],              
            [{'font': []}],
            [{'align': []}],
            ['clean']                                         
        ],
    },
    'placeholder': 'Inicia Aqui',
    'theme': 'snow'
}

una vez declarado estas variables necesarias para el funcionamiento, se requiere
importar el widget en el archivo admin.py o donde se haya declaro la personalizacion
del admin de algun modelo, por ejemplo:

#### en el models.py
Es **importante** declarar el campo donde quieres ver el editor como: models.TextField()
```
class Home(models.Model):
    """Model definition for Home."""

    title = models.CharField('titulo', max_length=50)
    content = models.TextField('contenido')
    blog = models.TextField()



#### en el admin.py
```
class EditorForm(forms.ModelForm):
    content = forms.CharField(widget=WidgetNeunQuillEditor(), required=False) # aqui usamos el Widget 

    class Meta:
        model = Home
        fields = '__all__'


Puedes usar el Form en tu class que personaliza tu Admin

 ```      
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    form = EditorForm
