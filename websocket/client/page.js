function main() {
    console.log('main');
    var btn_start = document.getElementById('button_start');
    var btn_close = document.getElementById('button_close');
    var form_msg = document.getElementById('form_msg');
    btn_start.onclick = function() {
	console.log('started');
	openWebSocket();
    };
    btn_close.onclick = function() {
	console.log('closed');
    }
    form_msg.onsubmit = function() {
	if (!ws) {
	    alert('Start socket first');
	}
	var text = document.getElementById('input_text').value;
	console.log('onsubmit text = ' + text);
	ws.send(text);
	return false;
    }
    
}

var ws = null;

function openWebSocket() {
    var uid_input = document.getElementById('uid_input')
    if (ws != null) {
	alert('Already opened');
	return;
    }
    uid = uid_input.value
    if (!uid) {
	alert('must specify uid input')
	return;
    }
    ws = new WebSocket("ws://54.208.172.48:9000/open/?uid="+uid);
    ws.onopen = function() {
	console.log('onopen');
    }
    ws.onclose = function() {
	console.log('onclose');
	ws = null;
    }
    ws.onerror = function(err) {
    console.log('onerror: ' + JSON.stringify(err));
	alert('onerror: ' + JSON.stringify(err));
    }
    ws.onmessage = function(event) {
	msg = event.data;
	console.log('onmessage ' + msg);
	var div = document.getElementById('div_msgs')
	div.innerHTML = msg + '<hr/>' + div.innerHTML;
    }
}
window.onload = main;
