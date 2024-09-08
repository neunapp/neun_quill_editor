# Documentación Neun Quill Editor

Este es un WidgetForm de Django muy **simple y sencillo** para poder tener Quill.js, un Editor WYSIWYG de contenido open source muy popular en JS.

La idea es que se pueda integrar cualquier versión de Quill.js y cualquier tema CSS que provee este editor.

## ¿Cómo usar WidgetNeunQuillEditor?

Es muy sencillo, primero necesitamos indicar la versión de Neun Quill desde el CDN en los settings:

```python
NEUN_QUILL_EDITOR_JS = 'https://cdn.jsdelivr.net/npm/quill@2.0.2/dist/quill.js'


Ahora también puedes indicar el template o tema CSS en los settings con la constante:

```python
NEUN_QUILL_EDITOR_CSS = 'https://cdn.jsdelivr.net/npm/quill@2.0.2/dist/quill.snow.css'


También puedes configurar las opciones de la barra de herramientas que trae Quill.

Por defecto es:

```python
toolbar_options = {
    'theme': 'snow',
    'modules': {
    }
}


Las opciones completas soportadas son:

```python
NEUN_TOOLBAR_OPTIONS = {
    'modules': {
        'toolbar': [
            ['bold', 'italic', 'underline', 'strike'],        
            ['blockquote', 'code-block'],
            ['link', 'video', 'formula'],  # no image
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
    'placeholder': 'Inicia Aquí',
    'theme': 'snow'
}


Una vez declaradas estas variables necesarias para el funcionamiento, se requiere importar el widget en el archivo admin.py o donde se haya declarado la personalización del admin de algún modelo. Por ejemplo:

### En el models.py
Es importante declarar el campo donde quieres ver el editor como: models.TextField().
```python
class Home(models.Model):
    """Model definition for Home."""

    title = models.CharField('título', max_length=50)
    content = models.TextField('contenido')
    blog = models.TextField()



#### En el admin.py
```python
class EditorForm(forms.ModelForm):
    content = forms.CharField(widget=WidgetNeunQuillEditor(), required=False)  # aquí usamos el Widget

    class Meta:
        model = Home
        fields = '__all__'

Puedes usar el Form en tu clase que personaliza tu Admin:

```python    
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    form = EditorForm
