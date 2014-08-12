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
    if (ws != null) {
	alert('Already opened');
	return;
    }
    ws = new WebSocket("ws://localhost:8003/open/");
    ws.onopen = function() {
	console.log('onopen');
    }
    ws.onclose = function() {
	console.log('onclose');
	ws = null;
    }
    ws.onerror = function(err) { 
	console.log('onerror: ' + err)
    }
    ws.onmessage = function(event) {
	msg = event.data;
	console.log('onmessage ' + msg);
	var div = document.getElementById('div_msgs')
	div.innerHTML = msg + '<hr/>' + div.innerHTML;
    }
}
window.onload = main;