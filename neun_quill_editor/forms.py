from django import forms
from django.utils.safestring import mark_safe
from django.conf import settings

toolbar_options = {
    'theme': 'snow',
    'modules': {
    }
}
if settings.NEUN_TOOLBAR_OPTIONS:
    toolbar_options = settings.NEUN_TOOLBAR_OPTIONS

neunQuillOptions = toolbar_options

class WidgetNeunQuillEditor(forms.Textarea):
    
    class Media:
        css = {
            'all': (settings.NEUN_QUILL_EDITOR_CSS,),
        }

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        if not value:
            value = ''
        #
        custom_html = f"""
            <div style="display: block; width: 100%;" id="neun_editor_{name}">
                <div id="#toolbar"></div>
                <div id="dj_editor_{name}" style="display: block; width: 100%;">
                    {value}
                </div>
                <br />
            </div>
            <div style="display: block; width: 100%;">
                <button 
                    type="button" 
                    onclick="switchEditor{name}(true)" 
                    style="background-color: #2d3436; color: white; border: 1px solid white; padding: 3px;">
                    Editor / Form(HTML)
                </button>
            </div>
            <script src={settings.NEUN_QUILL_EDITOR_JS}></script>
            <script src="/static/main.js"></script>
            <script>
                (function() {{
                    let flat = false;
                    let neunQuillOptions = {neunQuillOptions}
                    let fieldElement = {attrs['id']}
                    
                    let quill;
                    const contenido = document.getElementById('dj_editor_{name}')
                    const textarea = document.getElementById('id_{name}')

                    const formConten = textarea.parentNode
                    formConten.style.display = 'block';
                    textarea.style.display = 'none';
                    textarea.style.width = '95%';
                    contenido.style.width = '100%'
                    let optionsToolBar = neunQuillOptions ? neunQuillOptions : {{theme: 'snow', modules: {{toolbar: true}}}}
                    quill = new Quill('#dj_editor_{name}', optionsToolBar);
                    
                    quill.on('text-change', (delta, oldDelta, source) => {{
                        let html = quill.getSemanticHTML();
                        const dj_textarea = fieldElement
                        dj_textarea.value = html
                    }});
                    
                    
                    function switchEditor{name}() {{
                        const contenido = document.getElementById('neun_editor_{name}')
                        const textarea = fieldElement
                        if (flat) {{
                            contenido.style.display = 'block';
                            textarea.style.display = 'none';
                            flat = !flat
                        }} else {{
                            contenido.style.display = 'none';
                            textarea.style.display = 'block';
                            flat = !flat
                        }}
                    }}
                    window.switchEditor{name} = switchEditor{name};
                }})();
                
            </script>
            
        """

        return mark_safe(f"{html}<div style='display: block; width: 100%;'>{custom_html}</div>")