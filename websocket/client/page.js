var ADDR = 'ws://localhost:9001/websockets/open/?token=238e0375db25ccd3524e5023e0d5fb2d0'

function main() {
    console.log('main');
    var btn_start = document.getElementById('button_start');
    var btn_close = document.getElementById('button_close');
    var form_msg = document.getElementById('form_msg');
    var start_end_auto = document.getElementById('button_auto_start_end');
    start_end_auto.onclick = function() {
        auto=!auto;
        refreshAuto();
    }
    btn_start.onclick = function() {
	console.log('started');
	openWebSocket();
    };
    btn_close.onclick = function() {
    if (ws) {
    ws.close();
    console.log('closed');
    } else {
        console.log('no websocket open');
    }
    }
    form_msg.onsubmit = function() {
	if (!ws) {
	    alert('Start socket first');
	    return false;
	}
	var text = document.getElementById('input_text').value;
	//console.log('onsubmit text = ' + text);
	ws.send(text);
	return false;
    }
    refreshAuto();
}

var ws = null;

var auto = false;
var timer = null;
var index = 1;

function refreshAuto() {
    document.getElementById('span_auto_status').innerHTML=(auto?"ON":"OFF");
    document.getElementById('button_auto_start_end').innerHTML=(auto?"STOP AUTO":"START AUTO");
    if (auto) {
        index = 1;
        timer = window.setInterval(function() {
            ws.send('message ' + index);
            index++;
        },1000);
    } else {
        if (timer) {
            window.clearInterval(timer);
        }
    }
}

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
    ws = new WebSocket('ws://' + ADDR  + '/open/?uid='+uid);
    ws.onopen = function() {
	console.log('onopen');
    }
    ws.onclose = function(ev) {
	console.log('onclose: ' + ev.reason);
	ws = null;
    }
    ws.onerror = function(err) {
    console.log('onerror: ' + JSON.stringify(err));
	alert('onerror: ' + err.reason);
    }
    ws.onmessage = function(event) {
	msg = event.data;
	console.log('onmessage ' + msg);
	var div = document.getElementById('div_msgs')
	div.innerHTML = msg + '<hr/>' + div.innerHTML;
    }
}
window.onload = main;
