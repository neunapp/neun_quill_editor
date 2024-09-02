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
        # js = ('main.js',)

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        if not value:
            value = ''
        custom_html = f"""
            <div style="display: block; width: 100%;" id="neun_editor_content">
                <div id="#toolbar"></div>
                <div id="dj_editor_neun" style="display: block; width: 100%;">
                    {value}
                </div>
                <br />
            </div>
            <div style="display: block; width: 100%;">
                <button 
                    type="button" 
                    onclick="switchEditorAndTextArea(true)" 
                    style="background-color: #2d3436; color: white; border: 1px solid white; padding: 3px;">
                    Editor / Form(HTML)
                </button>
            </div>
            <script>
                var neunQuillOptions = {neunQuillOptions}
            </script>
            <script src={settings.NEUN_QUILL_EDITOR_JS}></script>
            <script src="/static/main.js"></script>
        """

        return mark_safe(f"{html}<div style='display: block; width: 100%;'>{custom_html}</div>")