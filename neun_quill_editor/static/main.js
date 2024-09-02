
let quill;
let flat = false;

document.addEventListener('DOMContentLoaded', function() {
  const contenido = document.getElementById('dj_editor_neun')
  const textarea = document.getElementById('id_content')
  const formConten = textarea.parentNode
  formConten.style.display = 'block';
  textarea.style.display = 'none';
  textarea.style.width = '95%';
  contenido.style.width = '100%'

  let optionsToolBar = neunQuillOptions ? neunQuillOptions : {theme: 'snow', modules: {toolbar: true}}
  quill = new Quill('#dj_editor_neun', optionsToolBar);
  
  quill.on('text-change', (delta, oldDelta, source) => {
    let html = quill.getSemanticHTML();
    const dj_textarea = document.getElementById('id_content')
    dj_textarea.value = html
  });
  
});


function switchEditorAndTextArea() {
  const contenido = document.getElementById('neun_editor_content')
  const textarea = document.getElementById('id_content')
  if (flat) {
    contenido.style.display = 'block';
    textarea.style.display = 'none';
    flat = !flat
  } else {
    contenido.style.display = 'none';
    textarea.style.display = 'block';
    flat = !flat
  }
}





