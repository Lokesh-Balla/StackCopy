
function bold(){
    document.getElementById('editor').focus();
    document.execCommand('bold', false, '');
}

function italic(){
    document.getElementById('editor').focus();
    document.execCommand('italic', false, '');
}

function link(){
    let url=prompt("enter the url");
    document.getElementById('editor').focus();
    document.execCommand('createLink', false, url);
}

function code(){
    document.execCommand("insertHTML", false, "<hr><code>"+document.getSelection()+"</code><hr>");
    document.getElementById('editor').focus();
}

function lalign(){
    document.getElementById('editor').focus();
    document.execCommand('justifyLeft', false, '');
}

function ralign(){
    document.getElementById('editor').focus();
    document.execCommand('justifyRight', false, '');
}

function calign(){
    document.getElementById('editor').focus();
    document.execCommand('justifyCenter', false, '');
}

function strike(){
    document.getElementById('editor').focus();
    document.execCommand('strikeThrough', false, '');
}
