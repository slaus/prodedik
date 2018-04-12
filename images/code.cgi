//scgi 
//cached 
 
		
var SITEHELP_FUNC = {
	get_cookie: function ( check_name ) {
		var a_all_cookies = document.cookie.split( ';' );
		var a_temp_cookie = '';
		var cookie_name = '';
		var cookie_value = '';
		var b_cookie_found = false;
	
		for ( i = 0; i < a_all_cookies.length; i++ )	{
			a_temp_cookie = a_all_cookies[i].split( '=' );
			cookie_name = a_temp_cookie[0].replace(/^\s+|\s+$/g, '');
			if ( cookie_name == check_name ){
				b_cookie_found = true;
				if ( a_temp_cookie.length > 1 ){
					cookie_value = unescape( a_temp_cookie[1].replace(/^\s+|\s+$/g, '') );
				};
				return cookie_value;
				break;
			};
			a_temp_cookie = null;
			cookie_name = '';
		}
		if ( !b_cookie_found )	{
			return null;
		}
	},

	set_cookie: function ( name, value, expires_min, path, domain, secure ) {
		var today = new Date();
		today.setTime( today.getTime() );
		
		if ( expires_min ) {
			expires_min = expires_min * 1000 * 60;
		};
		var expires_date = new Date( today.getTime() + (expires_min) );
		
		document.cookie = name + "=" + escape( value ) +
		( ( expires_min ) ? ";expires=" + expires_date.toGMTString() : "" ) +
		( ( path ) ? ";path=" + path : "" ) +
		( ( domain ) ? ";domain=" + domain : "" ) +
		( ( secure ) ? ";secure" : "" );
	},
	
	delete_cookie: function ( name, path, domain ) {
		if ( SITEHELP_FUNC.get_cookie( name ) ) {
			document.cookie = name + "=" + ( ( path ) ? ";path=" + path : "") + 
			( ( domain ) ? ";domain=" + domain : "" ) + 
			";expires=Thu, 01-Jan-1970 00:00:01 GMT";
		};
	},
	
	object_to_string: function (obj) {
		var has_NL = false;
		var NL_SPL = '<NL>';
		
		for (var v in obj) {
			if (obj[v] == null) {
				obj[v] = '';
			};
		};
		
		for (var v in obj) {
			if (obj[v].toString().indexOf("\n") >= 0) {
				has_NL = true;
				break;
			};
		};
		
		if (has_NL) {
			while (1) {
				NL_SPL += Math.floor(Math.random() * 10);
				var NL_found = false;
				
				for (var v in obj) {
					if (obj[v].toString().indexOf(NL_SPL) >= 0) {
						NL_found = true;
						break;
					};
				};
				
				if (NL_found) {
					continue;
				} else {
					break;
				};
			};
			
			
			for (var v in obj) {
				obj[v] = obj[v].toString().replace(/\n/g, NL_SPL);
			};
			obj._NL = NL_SPL;
		};
		
		
		var s = '';
		for (var v in obj) {
			s += v + ':' + obj[v].toString() + "\n";
		};
		
		return s;
	},
	
	string_to_object: function (str) {
		var obj = new Object;
		
		var lines = str.split("\n");
		
		for (var i=0; i < lines.length; i++) {
			var line = lines[i];
			
			if (line.match(/^(.*?):((.|\r)*)$/)) {
				obj[RegExp.$1] = RegExp.$2;
			};
		};
		
		if (typeof obj._NL != 'undefined') {
			var rx = new RegExp(obj._NL, 'g');
			for (var v in obj) {
				obj[v] = obj[v].toString().replace(rx, "\n");
			};
		};
		
		delete obj._NL;
		return obj;
	},

	find_object_position: function (obj) {
	  var curleft = 0;
	  var curtop = 0;
	   
	  if (obj.offsetParent) {
	    while(1)  {
	      curleft += obj.offsetLeft;
	      curtop += obj.offsetTop;
	      obj = obj.offsetParent;
	      if (! obj) { break; };
	    };
	  } else  {
	  	if(obj.x) curleft += obj.x;
	    if(obj.y) curtop += obj.y;
	  };
	  
	  return [curleft, curtop];
	}


};

		
		var SITEHELP_1218 = {
			client_id: '',
			iframe: '',
			chat_window_open: 0,
			
			curr_operator_status: '',
			CODE_CONTAINER: '',
			
			SYSTEM: {
				INITIALIZED: false,
				ACC_TYPE: 'p'
			},
			
			TEMPLATE: {
				HTML_CODE: '',
				OPINIONS: [
{
 id: 1,
text: 'Super',
want_comment: 0
},
{
 id: 2,
text: 'Good',
want_comment: 0
},
{
 id: 3,
text: 'Normal',
want_comment: 0
},
{
 id: 4,
text: 'Bad',
want_comment: 1
},
{
 id: 5,
text: 'Worst',
want_comment: 1
}
]
			},
			
			OPERATOR_STATUS: {
				current_status: 'online'
			},
			
			AUTO_CMD_POLLER: {
				active: false,
				timer: '',
				last_id : 0,
				poll_time: 30000, //default = each 30 seconds
				
				_MSG_DATA: '',
				
				start: function () {
					if (SITEHELP_1218.AUTO_CMD_POLLER.active) return;
			
					SITEHELP_1218.AUTO_CMD_POLLER.active = true;
					SITEHELP_1218.AUTO_CMD_POLLER.timer = setTimeout('SITEHELP_1218.AUTO_CMD_POLLER.poll()', 100);
				},
				
				stop: function () {
					SITEHELP_1218.AUTO_CMD_POLLER.active = false;
					clearTimeout(SITEHELP_1218.AUTO_CMD_POLLER.timer);
					SITEHELP_1218.AUTO_CMD_POLLER.timer = '';
				},
				
				poll: function () {
					if (! SITEHELP_1218.AUTO_CMD_POLLER.active) return;
					
					var s = document.createElement('script');
					s.type = 'text/javascript';
					s.charset = 'utf-8';
					s.src = 'https://c.sitehelp.im/outchat_cmd.cgi?c=1218&cid=' + SITEHELP_1218.client_id + '&aid=' + SITEHELP_1218.AUTO_CMD_POLLER.last_id + '&v=2&u=' + escape(window.location.href.slice(7)) + '&r=' + Math.random();
					SITEHELP_1218.CODE_CONTAINER.appendChild(s);
				},
				
				
				on_message: function (msg_id, msg_data) {
					if (! SITEHELP_1218.AUTO_CMD_POLLER.active) return;	//this can happen, coz script loading can be initiated before chat window opened

					SITEHELP_1218.AUTO_CMD_POLLER.last_id = msg_id;
					
					//we should NOT call 'notify_received' here. (it will be called by 'outchat_cmd' script if needed)
					
					//display msg in HINT box
					if ((typeof SITEHELP_HINT_1218 == 'object') && (typeof SITEHELP_HINT_1218.show == 'function')) {
						var coords_descr = SITEHELP_STATUS_1218.get_hint_box_coords();
						
						if (coords_descr) {
							SITEHELP_HINT_1218.show(msg_data, coords_descr);
						};
					};
				},
				
				notify_received: function (msg_id, options) {
					options.force = typeof options.force == 'undefined' ? false : options.force;
					options.is_auto = typeof options.is_auto == 'undefined' ? true : options.is_auto;
					
					if (! options.force) {
						if (! SITEHELP_1218.AUTO_CMD_POLLER.active) return;
					};
					
					var s = document.createElement('script');
					s.type = 'text/javascript';
					s.charset = 'utf-8';
					s.src = 'https://channel1218.sitehelp.im/send/c=1218&id=' + SITEHELP_1218.client_id + '&cmd=offchat_msg_received/' + (options.is_auto ? 1 : 0) + ',' + msg_id + '/' + Math.random();
					
					SITEHELP_1218.CODE_CONTAINER.appendChild(s);
				}
			},
		
			AUTO_DIE: {
				active: false,
				timer: '',
				died: false,
				
				start: function () {
					if (SITEHELP_1218.AUTO_DIE.active) return;
					
					SITEHELP_1218.AUTO_DIE.timer = setTimeout('SITEHELP_1218.AUTO_DIE.die()', 1000*300);
					SITEHELP_1218.AUTO_DIE.active = true;
				},
				
				stop: function () {
					SITEHELP_1218.AUTO_DIE.active = false;
					
					clearTimeout(SITEHELP_1218.AUTO_DIE.timer);
					SITEHELP_1218.AUTO_DIE.timer = null;
					
					
					//if 'stop' called after we 'died' - do UN-die
					if (SITEHELP_1218.AUTO_DIE.died) {
						SITEHELP_1218.AUTO_DIE.died = false;
						SITEHELP_1218.iframe.contentWindow.postMessage('init_wait:' + "\n", '*'); //un-qq!
					};
				},
				
				die: function () {
					//stop communication channel
					SITEHELP_1218.iframe.contentWindow.postMessage('de_init_wait:' + "\n", '*'); //un-qq!
					SITEHELP_1218.AUTO_DIE.stop();
					
					SITEHELP_1218.AUTO_DIE.died = true;
				}
			},
			
			COBROWSE: {
				script_loaded: false,
				queue: [],
				
				load_script: function () {
					var s = document.createElement('script');
					s.type = 'text/javascript';
					s.charset = 'utf-8';
					s.src = 'https://c.sitehelp.im/cobrowse.cgi?c=1218&v=2&cid=' + SITEHELP_1218.client_id + '&r=' + Math.random();
					SITEHELP_1218.CODE_CONTAINER.appendChild(s);
					
					SITEHELP_1218.COBROWSE.script_loaded = true;
				},
				
				add_command_to_queue: function (data) {
					if (! SITEHELP_1218.COBROWSE.script_loaded) SITEHELP_1218.COBROWSE.load_script();
					
					if (typeof SITEHELP_1218.COBROWSE.process_command == 'function') {
						SITEHELP_1218.COBROWSE.process_command(data);
					} else {
						SITEHELP_1218.COBROWSE.queue.push(data);
					};
				}
			},
		
			generate_client_id: function (in_len) {
				var len = (in_len ? in_len : 30);
				var chars = '_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890';
				var res = '';
				
				for (i=0; i <= len; i++) {
					var st = Math.floor(Math.random() * chars.length);
					res += chars.substr(st,1);
				};
				
				return res;
			},
			
			check_SITEHELP_list_init_allowed: function () {
				var ks = Object.keys(window);
				
				for (var i=0; i < ks.length; i++) {
					if (ks[i] == 'SITEHELP_1218') continue;
					
					if (ks[i].match(/^SITEHELP_(\d+)$/)) {
						var other_ch = RegExp.$1;
						
						if (typeof window[ks[i]].SYSTEM == 'undefined') continue;
						if (! window[ks[i]].SYSTEM.INITIALIZED) continue;
						
						if (SITEHELP_1218.SYSTEM.ACC_TYPE == 'f') {
							return false;
						} else {
							if (window[ks[i]].SYSTEM.ACC_TYPE == 'f') {
								if (window['SITEHELP_' + other_ch.toString()].CODE_CONTAINER) {
									window['SITEHELP_' + other_ch.toString()].CODE_CONTAINER.innerHTML = '';
								};
							};
						};
					};
					
				};
				
				return true;
			},
		
			init: function () {
				if (SITEHELP_1218.SYSTEM.INITIALIZED) return;
				if (! SITEHELP_1218.check_SITEHELP_list_init_allowed()) return;
				
				if (typeof SITEHELP_1218.check_allowed_domains == 'function') {
					if (! SITEHELP_1218.check_allowed_domains()) {
						return;
					};
				};
				
				// make CODE_CONTAINER
				if (! document.getElementById('SITEHELP_CONTAINER_1218')) {	//create new if not pasted to code 'inplace'
					var container = document.createElement('div');
					container.setAttribute("id", "SITEHELP_CONTAINER_1218");
					document.body.appendChild(container);
				};
				
				SITEHELP_1218.CODE_CONTAINER = document.getElementById('SITEHELP_CONTAINER_1218');
				
				//install OnMessage handler
				SITEHELP_1218.add_listener(window, "message", SITEHELP_1218.on_message_handler);
				
								
				//get||generate client_id
				if ((typeof SITEHELP_POPUP == 'undefined') || (typeof SITEHELP_POPUP.client_id == 'undefined')) {
					SITEHELP_1218.client_id = SITEHELP_FUNC.get_cookie("sitechat_ID_1218");
					if (! SITEHELP_1218.client_id) {
						SITEHELP_1218.client_id = SITEHELP_1218.generate_client_id();
					};
					SITEHELP_FUNC.set_cookie("sitechat_ID_1218", SITEHELP_1218.client_id, 525948, '/');	//1 year
				} else {
					SITEHELP_1218.client_id = SITEHELP_POPUP.client_id;
				};
				
				//append form HTML
				var form_container = document.createElement('div');
				form_container.innerHTML = SITEHELP_1218.TEMPLATE.HTML_CODE;
				document.body.appendChild(form_container);
								
				try {
					SITEHELP_STATUS_1218.init({'operator_status': SITEHELP_1218.OPERATOR_STATUS.current_status});
				} catch (e) {};
					
				try {
					SITEHELP_HINT_1218.init();
				} catch (e) {};
				
				try {
					SITEHELP_TEMPLATE_1218.init({
						'operator_status': SITEHELP_1218.OPERATOR_STATUS.current_status,						
						'opinions': SITEHELP_1218.TEMPLATE.OPINIONS,
						'partial_msg_tracking_enabled': 1,
						'partial_msg_tracking_update_time_sec': 5
					});
				} catch (e) {};
				
				
				//create communication iframe
				SITEHELP_1218.iframe = document.createElement('iframe');
				SITEHELP_1218.iframe.style.display = 'none';
				SITEHELP_1218.iframe.setAttribute('style', 'display:none;');
				SITEHELP_1218.iframe.src = "https://channel1218.sitehelp.im/iframe.cgi?c=1218&v=2&clientid=" + SITEHELP_1218.client_id + '&ssl=' + 1;// + "&r=" + Math.random(1);
				document.body.appendChild(SITEHELP_1218.iframe);
				
				SITEHELP_1218.SYSTEM.INITIALIZED = true;
			},
		
		
	    add_listener: function (element, event, listener, bubble) {
	      if(element.addEventListener) {
	        if(typeof(bubble) == "undefined") bubble = false;
	        element.addEventListener(event, listener, bubble);
	        return true;
	      } else if (element.attachEvent) {
	        element.attachEvent("on" + event, listener);
	        return true;
	      };
	      
	      return false;
	    },
		
		
			on_message_handler: function (evt) {				
				if (evt.origin != 'https://channel1218.sitehelp.im') return;
				
				if (evt.data == 'iframe_ready') {					
					var state_obj = {
						title: document.title,
						curr_url: decodeURIComponent(window.location.href.slice(7)),
						chat_window_open: 0	//start with 0 always
					};
					
					if (document.referrer) {
						state_obj.referrer = decodeURIComponent(document.referrer.slice(7));
					};
					
					//send client_state (if we are NOT in popup)
					if (typeof SITEHELP_POPUP == 'undefined') {
						evt.source.postMessage('client_state_data:' + "\n" + JSON.stringify(state_obj), evt.origin);
					};
					
					evt.source.postMessage("init_wait:\n", evt.origin);	//init_wait
					
					
					if (typeof SITEHELP_POPUP == 'undefined') {
						var WindowOpenStatus = SITEHELP_FUNC.get_cookie("SITEHELP.window_open_1218");
						if (WindowOpenStatus && (WindowOpenStatus == 1)) {	//reopen window
							SITEHELP_TEMPLATE_1218.open_chat_window();
						} else {
							SITEHELP_1218.AUTO_CMD_POLLER.start();
							SITEHELP_1218.AUTO_DIE.start();
						};
					} else {
						SITEHELP_TEMPLATE_1218.open_chat_window();
					};
								
					return;
				};
				
				
				if (evt.data.match(/get_form_data_reply:\n((.|[\n\r])*)/)) {
					var data = JSON.parse(RegExp.$1);
					if (SITEHELP_TEMPLATE_1218.form_data) SITEHELP_TEMPLATE_1218.form_data(data);
					
					return;
				};
				
				
				if (evt.data.match(/send_form_data_result:\n((.|[\n\r])*)/)) {
					var result = JSON.parse(RegExp.$1);
					if (SITEHELP_TEMPLATE_1218.send_form_data_result) SITEHELP_TEMPLATE_1218.send_form_data_result(result);
					
					return;
				};
				
				
				if (evt.data.match(/operator_message:\n((.|[\n\r])*)/)) {
					var msg_obj = JSON.parse(RegExp.$1);
					
					SITEHELP_TEMPLATE_1218.on_chat_message(msg_obj);
						
					if (SITEHELP_1218.chat_window_open == '0') {	//closed chat window
						if ((msg_obj.to == 'client') && (msg_obj.by_human == '1')) {
							SITEHELP_1218.AUTO_CMD_POLLER.notify_received(msg_obj.id, {is_auto: false});
							
							//display msg in HINT box
							if ((typeof SITEHELP_HINT_1218 == 'object') && (typeof SITEHELP_HINT_1218.show == 'function')) {
								var coords_descr = SITEHELP_STATUS_1218.get_hint_box_coords();
								
								if (coords_descr) {
									SITEHELP_HINT_1218.show(msg_obj.text, coords_descr);
								};
							};
						};
					};
					
					return;
				};
				
				
				if (evt.data.match(/full_chat_history:\n((.|[\n\r])*)/)) {	
					var msgs_arr = JSON.parse(RegExp.$1);
					SITEHELP_TEMPLATE_1218.full_chat_log_data({'msgs': msgs_arr});
					return;
				};
				
				
				if (evt.data.match(/operator_status:\n((.|[\n\r])*)/)) {
					var event_obj = JSON.parse(RegExp.$1);

					SITEHELP_1218.curr_operator_status = event_obj.status;

					var status_object = {
						'operator_status': event_obj.status
					};
											
					if (event_obj.status == 'offline') {
						status_object.actions = event_obj.actions;
					};

					if (event_obj.status == 'error') {
						status_object.error_message = event_obj.error_message;
					};

					//notify template(s)
					SITEHELP_STATUS_1218.operator_status_changed(status_object);
					SITEHELP_TEMPLATE_1218.operator_status_changed(status_object);

					//call api
					if (typeof SITEHELP_API_1218 == 'object') {
						
						if ( (event_obj.status == 'online') && (typeof SITEHELP_API_1218.onReady_func == 'function') ) {	//this will be true only once per page load
							SITEHELP_API_1218.onReady_func();
							SITEHELP_API_1218.onReady(undefined);	//reset to undef
						};
						
						if ( (event_obj.status == 'offline') && (typeof SITEHELP_API_1218.onReadyOffline_func == 'function') ) {	//this will be true only once per page load
							SITEHELP_API_1218.onReadyOffline_func();
							SITEHELP_API_1218.onReadyOffline(undefined);	//reset to undef
						};
						
					};
					
					return;
				};
				
				if (evt.data.match(/operator_data:\n((.|[\n\r])*)/)) {
					var event_obj = JSON.parse(RegExp.$1);
					SITEHELP_TEMPLATE_1218.operator_data_changed(event_obj);
					return;
				};
				
				if (evt.data.match(/operator_typing:\n((.|[\n\r])*)/)) {
					var event_obj = JSON.parse(RegExp.$1);
					SITEHELP_TEMPLATE_1218.operator_activity(event_obj);
					return;
				};
				
				if (evt.data.match(/operator_command:\n((.|[\n\r])*)/)) {
					var event_obj = JSON.parse(RegExp.$1);
				
					if (event_obj.command == 'goto') {
						if (typeof SITEHELP_POPUP == 'undefined') {
							window.location.href = event_obj.url;
						} else {
							try {
								window.opener.location.href = event_obj.url;
							} catch (e) {};
						};
					};
					
					if (typeof SITEHELP_POPUP != 'undefined') {
						return;	//do not process NEXT commands in popup state
					};
					
					if (event_obj.command == 'openchat') {
						SITEHELP_TEMPLATE_1218.open_chat_window();
					};
					
					if (event_obj.command == 'closechat') {
						SITEHELP_TEMPLATE_1218.close_chat_window();
					};
											
					if (event_obj.command == 'cobrowse_cmd') {
						SITEHELP_1218.COBROWSE.add_command_to_queue(event_obj.data);
					};
					
					return;
				};
				
				
				if (evt.data.match(/jseval:\n((.|[\n\r])*)/)) {
					var event_obj = JSON.parse(RegExp.$1);
					try { eval(event_obj.code); } catch (e) {};
					return;
				};
				
			},
			
			
			
			
			//callbacks from TEMPATE
			notify_window_state_changed: function (params) {
				//params.state: 'open' || 'closed' ( window would not KNOW it is in 'popup' state)

				var this_state = params.state;
				
				if ((this_state == 'open') && (typeof SITEHELP_POPUP != 'undefined')) {
					this_state = 'popup';
				};
				
				if (this_state == 'open') {
					SITEHELP_1218.chat_window_open = 1;
				};
				
				if (this_state == 'popup') {
					SITEHELP_1218.chat_window_open = 2;
				};
				
				if (this_state == 'open' || this_state == 'popup') {
					SITEHELP_FUNC.set_cookie("SITEHELP.window_open_1218", 1, 30, '/');
					SITEHELP_1218.AUTO_CMD_POLLER.stop();
					SITEHELP_1218.AUTO_DIE.stop();
					
					//call api
					if ((typeof SITEHELP_API_1218 == 'object') && (typeof SITEHELP_API_1218.onChatWindowOpen_func == 'function')) {
						SITEHELP_API_1218.onChatWindowOpen_func();
					};
				};
				
				
				if (this_state == 'closed') {
					SITEHELP_1218.chat_window_open = 0;
					SITEHELP_FUNC.delete_cookie("SITEHELP.window_open_1218", '/');
					SITEHELP_1218.AUTO_CMD_POLLER.start();
					SITEHELP_1218.AUTO_DIE.start();
					
					//call api
					if ((typeof SITEHELP_API_1218 == 'object') && (typeof SITEHELP_API_1218.onChatWindowClose_func == 'function')) {
						SITEHELP_API_1218.onChatWindowClose_func();
					};
				};
				
				SITEHELP_STATUS_1218.window_state_changed({'state': this_state});
				SITEHELP_HINT_1218.window_state_changed({'state': this_state});	//will hide hint box on chat window open
				SITEHELP_1218.iframe.contentWindow.postMessage('client_state_data:' + "\n" + JSON.stringify({'chat_window_open': SITEHELP_1218.chat_window_open}), '*');	//un-qq!
			},
			
			notify_client_activity: function (params) {
				var obj;
				
				if (params.type == 'client_typing') {
					obj = {
						'type': 'client_typing',
						'status': params.status
					};
				};
				
				if (params.type == 'client_partial_msg') {
					obj = {
						'type': 'client_partial_msg',
						'status': params.status
					};
				};
				
				if (obj) SITEHELP_1218.iframe.contentWindow.postMessage('client_activity:' + "\n" + JSON.stringify(obj), '*');
			},
			
			send_message: function (msg_obj) {
				SITEHELP_1218.iframe.contentWindow.postMessage('send_message:' + "\n" + JSON.stringify(msg_obj), '*');
			},
			
			play_sound: function (type) {
				SITEHELP_1218.iframe.contentWindow.postMessage('play_sound:' + "\n" + JSON.stringify({'type': type}), '*');
			},
			
			send_opinion: function (id, comment) {
				SITEHELP_1218.iframe.contentWindow.postMessage('send_opinion:' + "\n" + JSON.stringify({'id': id, 'comment': comment}), '*');
			},
			
			send_chat_log_to_email: function (email) {
				SITEHELP_1218.iframe.contentWindow.postMessage('send_chat_log_to_email:' + "\n" + JSON.stringify({'email': email}), '*');
			},
			
			//user want open chat in new (external) window
			// 2 parameters is REQUIRED:
			//params.height - height of new window
			//params.width - width of new window
			open_in_new_window: function (params) {
				
				var New_win =
				  window.open("https://c.sitehelp.im/ext_win_chat.cgi?c=1218&clientid=" + SITEHELP_1218.client_id + "&rnd=" + Math.random(), 
				   "SITEHELP_PopupWindow_1218",
				   "menubar=no,location=no,resizable=no,scrollbars=no,status=no,directories=no,height=" + params.height + ",width=" + params.width
				 );
				 
			},			
			
			
			get_form_data: function (form_id, msg_id) {
				var params = {
					"form_id": form_id, 
					"msg_id": msg_id
				};
				
				SITEHELP_1218.iframe.contentWindow.postMessage('get_form_data:' + "\n" + JSON.stringify(params), '*');
			},
			
			
			send_form_data: function (form_id, msg_id, form_data) {
				var params = {
					"form_id": form_id, 
					"msg_id": msg_id,
					"form_data": form_data,
					"url": window.location.href
				};
				
				SITEHELP_1218.iframe.contentWindow.postMessage('send_form_data:' + "\n" + JSON.stringify(params), '*');
			},
			
			notify_form_completed: function (form_id, msg_id, secret) {
				var params = {
					"form_id": form_id, 
					"msg_id": msg_id,
					"secret": secret
				};
				SITEHELP_1218.iframe.contentWindow.postMessage('notify_form_completed:' + "\n" + JSON.stringify(params), '*');
			},
			
			reload_history: function () {
				SITEHELP_1218.iframe.contentWindow.postMessage('reload_history:' + "\n", '*');
			}
		};
		
		//status JS
		
var SITEHELP_STATUS_1218 = {
	TEMPLATE_HTML_CODE: '',	// will hold HTML code for this hint template
	
	TEXT_ONLINE: 'Support Online!',
	TEXT_OFFLINE: 'Support Offline!',
	
	hide_on_offline: 1,
	hide_on_chat_open: 1,
	
	animated_appearance: 1,
	animation_effect: 'fade_in',
	animation_effect_duration: 200,
	
	animation_effect_step: 0,
	animation_effect_total_steps: 50,
	
	
	curr_op_status: '',
	window_open: false,
	
	first_time_appearance: true,
	i_am_visible: '', //not set
				
	init: function (params) {
		//params.operator_status = 'online' || 'ofline' || ''
		
		var s = document.createElement('div');
		s.innerHTML = SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE;
		SITEHELP_1218.CODE_CONTAINER.appendChild(s);
		
		SITEHELP_STATUS_1218.operator_status_changed(params);
	},
	
	operator_status_changed: function (params) {
		//params.operator_status: 'online' || 'offline' || 'connecting' || 'error' || '' = unknown
		
		//ignore all statuses except 'online' and 'offline'
		if (! ((params.operator_status == 'online') || (params.operator_status == 'offline'))) return;
		
		if (SITEHELP_STATUS_1218.curr_op_status == params.operator_status) return;
		
		SITEHELP_STATUS_1218.curr_op_status = params.operator_status;
		SITEHELP_STATUS_1218.__INT_change_image();
		SITEHELP_STATUS_1218.__INT_show_OR_hide_status();
	},
	
	window_state_changed: function (params) {
		//params.state: 'closed' || 'open' | 'popup'
		SITEHELP_STATUS_1218.window_open = params.state == 'open';
		SITEHELP_STATUS_1218.__INT_show_OR_hide_status();
	},
	
	
	
	//this function is used to retrieve coordinates (POINT with margins) where 'hint box' will be displayed
	// should return object:
	// {
	//  top:					]
	//  left:					] [top || bottom] && [left || right] SHOULD BE DEFINED.
	//  right:				] should end with 'px' or '%'.  Ex: '10px',  '50%'
	//  bottom:				]
	//  position: 'absoulte' || 'fixed'
	//
	//	optional:
	//	margin_top, margin_left, margin_right, margin_bottom   - ONLY IN PIXELS!
	// }
	
	get_hint_box_coords: function () {
		var hint_over_object_container = document.getElementById('SITEHELP_STATUS_CONTAINER_WRAP_1218');
		var hint_over_object = document.getElementById('SITEHELP_STATUS_CONTAINER_1218');
		
		var res = {};
		
		res.position = 'fixed';
		
		if (hint_over_object_container.style.right) {
			if (hint_over_object_container.style.right.match(/px/)) {
				res.right = parseInt(hint_over_object_container.style.right) + parseInt(hint_over_object_container.offsetWidth/2) + 'px';
			} else {
				res.right = hint_over_object_container.style.right;
				res.margin_right = parseInt(hint_over_object_container.offsetWidth/2);
			};
		};

		if (hint_over_object_container.style.left) {
			if (hint_over_object_container.style.left.match(/px/)) {
				res.left = parseInt(hint_over_object_container.style.left) + parseInt(hint_over_object_container.offsetWidth/2) + 'px';
			} else {
				res.left = hint_over_object_container.style.left;
				res.margin_left = parseInt(hint_over_object_container.offsetWidth/2);
			};
		};

		if (hint_over_object_container.style.top) {
			if (hint_over_object_container.style.top.match(/px/)) {
				res.top = parseInt(hint_over_object_container.style.top) + parseInt(hint_over_object_container.offsetHeight/2) + 'px';
			} else {
				res.top = hint_over_object_container.style.top;
				res.margin_top = parseInt(hint_over_object_container.offsetHeight/2);
			};
		};
		
		if (hint_over_object_container.style.bottom) {
			if (hint_over_object_container.style.bottom.match(/px/)) {
				res.bottom = parseInt(hint_over_object_container.style.bottom) + parseInt(hint_over_object_container.offsetHeight/2) + 'px';
			} else {
				res.bottom = hint_over_object_container.style.bottom;
				res.margin_bottom = parseInt(hint_over_object_container.offsetHeight/2);
			};
		};
		
			
		if (hint_over_object_container.style.marginRight) {
			if (res.margin_right) {
				res.margin_right = parseInt(res.margin_right) + parseInt(hint_over_object_container.style.marginRight) + 'px';
			} else {
				res.margin_right = hint_over_object_container.style.marginRight;
			};
		};

		if (hint_over_object_container.style.marginLeft) {
			if (res.margin_left) {
				res.margin_left = parseInt(res.margin_left) + parseInt(hint_over_object_container.style.marginLeft) + 'px';
			} else {
				res.margin_left = hint_over_object_container.style.marginLeft;
			};
		};
		
		if (hint_over_object_container.style.marginTop) {
			if (res.margin_top) {
				res.margin_top = parseInt(res.margin_top) + parseInt(hint_over_object_container.style.marginTop) + 'px';
			} else {
				res.margin_top = hint_over_object_container.style.marginTop;
			};
		};
		
		if (hint_over_object_container.style.marginBottom) {
			if (res.margin_bottom) {
				res.margin_bottom = parseInt(res.margin_bottom) + parseInt(hint_over_object_container.style.marginBottom) + 'px';
			} else {
				res.margin_bottom = hint_over_object_container.style.marginBottom;
			};
		};
		
		return res;
	},
	
	
	
	
	
	/////////////////////////// INTERNAL FUNCITONS /////////////////////////////////
	
	__INT_change_image: function () {
		var c = document.getElementById('SITEHELP_STATUS_CONTAINER_1218');
		var t = document.getElementById('SITEHELP_STATUS_TEXT_CONTAINER_1218');
		if (!c) return;
		if (!t) return;
		
		c.style.display = 'none';
		
		if (SITEHELP_STATUS_1218.curr_op_status == 'online') {
			c.className = "SITEHELP_STATUS_CONTAINER_1218 SITEHELP_STATUS_CONTAINER_ONLINE_1218 SITEHELP_STATUS_CONTAINER_ONLINE_CUSTOM_1218";
			t.className = "SITEHELP_STATUS_TEXT_CONTAINER_ONLINE_1218 SITEHELP_STATUS_TEXT_CONTAINER_ONLINE_CUSTOM_1218";
			t.innerHTML = SITEHELP_STATUS_1218.TEXT_ONLINE;
		} else {
			c.className = "SITEHELP_STATUS_CONTAINER_1218 SITEHELP_STATUS_CONTAINER_OFFLINE_1218 SITEHELP_STATUS_CONTAINER_OFFLINE_CUSTOM_1218";
			t.className = "SITEHELP_STATUS_TEXT_CONTAINER_OFFLINE_1218 SITEHELP_STATUS_TEXT_CONTAINER_OFFLINE_CUSTOM_1218";
			t.innerHTML = SITEHELP_STATUS_1218.TEXT_OFFLINE;
		};

	},
	
	
	
	__INT_show_OR_hide_status: function () {
		var img_visible = true;
		
		if (SITEHELP_STATUS_1218.curr_op_status == 'online') {
			
			if (SITEHELP_STATUS_1218.window_open) {
				img_visible = ! SITEHELP_STATUS_1218.hide_on_chat_open;
			} else {
				img_visible = true;
			};
			
		} else {		//op OFFLINE
			
			if (SITEHELP_STATUS_1218.window_open) {
				img_visible = ! SITEHELP_STATUS_1218.hide_on_chat_open;
			} else {
				img_visible = ! SITEHELP_STATUS_1218.hide_on_offline;
			};
		};
		
		
		if (img_visible) {
			
			if (SITEHELP_STATUS_1218.i_am_visible != '1') {
				SITEHELP_STATUS_1218.i_am_visible = '1';
				
				
				
				if (SITEHELP_STATUS_1218.first_time_appearance && (SITEHELP_STATUS_1218.animated_appearance == 1)) {
					SITEHELP_STATUS_1218.first_time_appearance = false;
					SITEHELP_STATUS_1218.__INT_appear_animated();
				} else {
					document.getElementById('SITEHELP_STATUS_CONTAINER_1218').style.display = '';
				};
				
				
				
			};
			
		} else {
			
			if (SITEHELP_STATUS_1218.i_am_visible != '0') {
				SITEHELP_STATUS_1218.i_am_visible = '0';
				document.getElementById('SITEHELP_STATUS_CONTAINER_1218').style.display = 'none';
			};
			
		};

		
	},
	
	

	__INT_appear_animated: function () {
		
		if (SITEHELP_STATUS_1218.animation_effect == 'fade_in') return SITEHELP_STATUS_1218.__INT_appear_animated_FADE_IN();
		
		
		
		//unknown animation effect
		document.getElementById('SITEHELP_STATUS_CONTAINER_1218').style.display = '';
	},
	
	
	__INT_appear_animated_FADE_IN: function () {
		document.getElementById('SITEHELP_STATUS_CONTAINER_1218').style.opacity = 0;
		document.getElementById('SITEHELP_STATUS_CONTAINER_1218').style.display = '';
		
		if (typeof jQuery == 'undefined') {
			SITEHELP_STATUS_1218.animation_effect_step = 0;
			SITEHELP_STATUS_1218.__INT_appear_animated_FADE_IN_STEP();
		} else {
			jQuery('#SITEHELP_STATUS_CONTAINER_1218').css({'opacity': 0}).animate({'opacity': 1}, {'duration': SITEHELP_STATUS_1218.animation_effect_duration});
		};
	},
	
	__INT_appear_animated_FADE_IN_STEP: function () {
		SITEHELP_STATUS_1218.animation_effect_step++;
		
		if (SITEHELP_STATUS_1218.animation_effect_step >= SITEHELP_STATUS_1218.animation_effect_total_steps) {
			document.getElementById('SITEHELP_STATUS_CONTAINER_1218').style.opacity = 1;
			return;
		};
		
		var opc = SITEHELP_STATUS_1218.animation_effect_step / SITEHELP_STATUS_1218.animation_effect_total_steps;
		document.getElementById('SITEHELP_STATUS_CONTAINER_1218').style.opacity = opc;
		
		setTimeout(SITEHELP_STATUS_1218.__INT_appear_animated_FADE_IN_STEP, Math.round(SITEHELP_STATUS_1218.animation_effect_duration / SITEHELP_STATUS_1218.animation_effect_total_steps));
	},
	



	
	
	
	
	
	last_element_for_IE: ''
};

		SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '<style type="text/css">';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	#SITEHELP_STATUS_CONTAINER_1218, #SITEHELP_STATUS_TEXT_CONTAINER_1218, #SITEHELP_STATUS_CONTAINER_TBL_1218 {';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		display: block;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		box-sizing: border-box;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		outline: none;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		width: auto;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		min-width: 0;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		max-width: none;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		height: auto;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		min-height: 0;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		max-height: none;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		text-indent: 0;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		line-height: normal;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		text-decoration: none;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		padding: 0;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		border: none;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	#SITEHELP_STATUS_CONTAINER_TBL_1218 * {';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		outline: none;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		width: auto;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		min-width: 0;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		max-width: none;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		height: auto;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		min-height: 0;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		max-height: none;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		border: none;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		background: none;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		padding: 0;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		margin: 0;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	#SITEHELP_STATUS_CONTAINER_WRAP_1218 {';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		z-index:2100000000; ';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	#SITEHELP_STATUS_CONTAINER_1218 {';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		position: relative;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		right:0; ';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		 ';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		margin-right:0px; ';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		 ';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		 ';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '			border-top-left-radius: 5px;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '			border-top-right-radius: 5px;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		cursor: pointer;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		text-align: center;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '				';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '			';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		    transform: translateY(-100%) rotate(270deg) translateX(50%);';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		    transform-origin: right bottom 0;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '			';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '				';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	#SITEHELP_STATUS_TEXT_CONTAINER_1218 {';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		font-size: 16px;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		font-weight: normal;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		font-family: sans-serif;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		white-space: nowrap;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	#SITEHELP_STATUS_CONTAINER_TBL_1218 {';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		padding: 5px 15px 5px 15px;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		border: 0;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	.SITEHELP_STATUS_CONTAINER_ONLINE_1218 {';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		background: #000000;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		border: 1px solid #000000;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	.SITEHELP_STATUS_TEXT_CONTAINER_ONLINE_1218 {';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		color: #FFFFFF;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	.SITEHELP_STATUS_CONTAINER_OFFLINE_1218 {';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		background: #000000;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		border: 1px solid #000000;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	.SITEHELP_STATUS_TEXT_CONTAINER_OFFLINE_1218 {';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		color: #FFFFFF;';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	/* online class,  use "!important" to override styles */';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '.SITEHELP_STATUS_CONTAINER_ONLINE_CUSTOM_1218 {';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '}';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '.SITEHELP_STATUS_TEXT_CONTAINER_ONLINE_CUSTOM_1218 {';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '}';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '/* offline class, use "!important" to override styles */';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '.SITEHELP_STATUS_CONTAINER_OFFLINE_CUSTOM_1218 {';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '}';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '.SITEHELP_STATUS_TEXT_CONTAINER_OFFLINE_CUSTOM_1218 {';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '}';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '</style>';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '<div id="SITEHELP_STATUS_CONTAINER_WRAP_1218" style="position: fixed; right:0; top:50%; ">';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	<div id="SITEHELP_STATUS_CONTAINER_1218" class="SITEHELP_STATUS_CONTAINER_1218" onclick="SITEHELP_TEMPLATE_1218.open_chat_window()" style="">';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		<table cellpadding=0 cellspacing=0 id="SITEHELP_STATUS_CONTAINER_TBL_1218">';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '			<tr>';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '				<td style="vertical-align: bottom; padding-right: 4px;  display: none;  " id="SITEHELP_STATUS_CONTAINER_ICON_IMG_1218">';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '					<img style="border: 0; margin:0 padding: 0;" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyZpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTExIDc5LjE1ODMyNSwgMjAxNS8wOS8xMC0wMToxMDoyMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTUgKFdpbmRvd3MpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjgxQzhFRDJGMEM2NDExRTZCNjQzQ0FCNTJENjFCOUJFIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjgxQzhFRDMwMEM2NDExRTZCNjQzQ0FCNTJENjFCOUJFIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6ODFDOEVEMkQwQzY0MTFFNkI2NDNDQUI1MkQ2MUI5QkUiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6ODFDOEVEMkUwQzY0MTFFNkI2NDNDQUI1MkQ2MUI5QkUiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7QI2JLAAABeklEQVR42mJkwA9UgVgLiCWh/JdAfB2IbzCQCIKAeCMQ/wLi/2j4LxBvA+JIYgwyAeKzaAbcBOJdQLwT6jpkuWtAbIvLsGgkhSCNSUAsikWdEBDHAvF5JPXp6IqckCRbSAiaciR9gTBBJiD+BhUsYyAdpEH1/gFiHpBALlRgLwP5YDPUjFYQ5xyU44ikwABNgwIUM+BQYwo14z4DUhgIQCUnQPkJUD5I/AMQP0BSUwBVMwHJ0N8gMSYkga9Q+gMWF4AMk0cy8AOSZTDwB8Z4AbVNBUkyAIv30IPBAclAKagZn0Cc2VBOIwWRUgs1Yy0sv8LC0YAMwySA+Ae6/n7kWCIBSAPxE6jeucgShlDBs0QaxALEWUD8D6rvALIELOvBXAoL8Hog/gnEJ6Cu+Af1HshbPkDMCVU7H5rvUcBhpHS1F0uRhQ3vA2I3dIMYoaXHWzTxU0DcDnWVEdRloDT7BlpkHcUX3mugNh6GRr8uA4UgEYhtGKgEAAIMAN8UdsDgdn3qAAAAAElFTkSuQmCC">';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '				</td>';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '				';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '				<td id="SITEHELP_STATUS_TEXT_CONTAINER_1218">';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '					';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '				</td>';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '			</tr>';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		</table>';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '	</div>';
SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_STATUS_1218.TEMPLATE_HTML_CODE += '</div>';


		//hint template
		
var SITEHELP_HINT_1218 = {
	TEMPLATE_HTML_CODE: '',	// will hold HTML code for this hint template
	
	hint_container: '',
	hint_text_container: '',
	
	init: function () {		
		var d = document.createElement('div');
		d.setAttribute("style", "position: absolute;");
		d.style.position = 'absolute';
		d.style.top = '0px';
		d.style.left = '0px';
		d.innerHTML = SITEHELP_HINT_1218.TEMPLATE_HTML_CODE;
		document.body.appendChild(d);
		
		SITEHELP_HINT_1218.hint_container = document.getElementById('SITEHELP_HINT_CONTAINER_1218');
		SITEHELP_HINT_1218.hint_text_container = document.getElementById('SITEHELP_HINT_TEXT_CONTAINER_1218');
	},
	
	window_state_changed: function (params) {
		//params.state: 'closed' || 'open' | 'popup'
		
		//process only 'open' state
		if (params.state == 'open') {
			SITEHELP_HINT_1218.hide();
		};
		
	},
	
	show: function (msg_text, show_point) {
		if (! SITEHELP_HINT_1218.hint_container) return;
		if (! SITEHELP_HINT_1218.hint_text_container) return;
		
		SITEHELP_HINT_1218.hint_text_container.innerHTML = msg_text;
		
		var hint_container = SITEHELP_HINT_1218.hint_container;
		 
		var positionClass_1;
		var positionClass_2;
		var hint_container_Width = 248;
		var hint_container_Height = 207;
		
		hint_container.style.position = show_point.position;
		
		
		hint_container.style.display = 'none';	
		hint_container.style.top = null;
		hint_container.style.bottom = null;
		hint_container.style.right = null;
		hint_container.style.left = null;
		
		hint_container.style.marginTop = null;
		hint_container.style.marginBottom = null;
		hint_container.style.marginLeft = null;
		hint_container.style.marginRight = null;
		
		
		if (show_point.position == 'absoulte') {

			
			/*
			var trueBody = (document.compatMode && document.compatMode!="BackCompat")? document.documentElement : document.body;
			
      if ( parseInt(trueBody.clientWidth + trueBody.scrollLeft) < parseInt(hint_container_Width + Pos[0])) {
        positionClass = "SITEHELP_Right";
        Pos[0] -= hint_container_Width;
      } else {
	      positionClass = "SITEHELP_Left";
      };
      
      if ( parseInt(trueBody.clientHeight + trueBody.scrollTop) < parseInt(hint_container_Height + Pos[1])) {
        positionClass += "Bottom";
        Pos[1] -= hint_container_Height;
      } else {
        positionClass += "Top";
      };
      
      */
		};
		
	
		var browser_size = SITEHELP_HINT_1218.__get_browser_size();
		
		var corner_left_right = '';
		var corner_top_bottom = '';
		
		if (show_point.left) {
			hint_container.style.left = show_point.left;
			
			if (show_point.left.match(/px/)) {
				corner_left_right = (parseInt(show_point.left) <= (browser_size.width/2)) ? 'left' : 'right';
			} else {
				corner_left_right = (parseInt(show_point.left) <= 50) ? 'left' : 'right';
			};
		};
		
		if (show_point.right) {
			hint_container.style.right = show_point.right;
			
			if (show_point.right.match(/px/)) {
				corner_left_right = (parseInt(show_point.right) <= (browser_size.width/2)) ? 'right' : 'left';
			} else {
				corner_left_right = (parseInt(show_point.right) <= 50) ? 'right' : 'left';
			};
		};
		
		if (show_point.top) {
			hint_container.style.top = show_point.top;
			
			if (show_point.top.match(/px/)) {
				corner_top_bottom = (parseInt(show_point.top) <= (browser_size.height/2)) ? 'top' : 'bottom';
			} else {
				corner_top_bottom = (parseInt(show_point.top) <= 50) ? 'top' : 'bottom';
			};
		};
		
		if (show_point.bottom) {
			hint_container.style.bottom = show_point.bottom;
			
			if (show_point.bottom.match(/px/)) {
				corner_top_bottom = (parseInt(show_point.bottom) <= (browser_size.height/2)) ? 'bottom' : 'top';
			} else {
				corner_top_bottom = (parseInt(show_point.bottom) <= 50) ? 'bottom' : 'top';
			};
		};
		
		
		
		show_point.margin_left = parseInt(typeof show_point.margin_left != 'undefined' ? show_point.margin_left : 0);
		show_point.margin_right = parseInt(typeof show_point.margin_right != 'undefined' ? show_point.margin_right : 0);
		show_point.margin_top = parseInt(typeof show_point.margin_top != 'undefined' ? show_point.margin_top : 0);
		show_point.margin_bottom = parseInt(typeof show_point.margin_bottom != 'undefined' ? show_point.margin_bottom : 0);
		
		
		if (corner_left_right == 'left') {
			positionClass_1 = "SITEHELP_Left";
			
			if (show_point.left) {
				hint_container.style.marginLeft = show_point.margin_left + 'px';
			} else {
				hint_container.style.marginRight = -(hint_container_Width - show_point.margin_right) + 'px';
			};
			
		} else {
			positionClass_1 = "SITEHELP_Right";
			
			if (show_point.left) {
				hint_container.style.marginLeft = -(hint_container_Width - show_point.margin_left) + 'px';
			} else {
				hint_container.style.marginRight = show_point.margin_right + 'px';
			};

		};
		
		
		if (corner_top_bottom == 'top') {
			positionClass_2 = "Top";
			
			if (show_point.top) {
				hint_container.style.marginTop = show_point.margin_top + 'px';
			} else {
				hint_container.style.marginBottom = -(hint_container_Height - show_point.margin_bottom) + 'px';
			};
			
		} else {
			positionClass_2 = "Bottom";
			
			if (show_point.top) {
				hint_container.style.marginTop = -(hint_container_Height - show_point.margin_top) + 'px';
			} else {
				hint_container.style.marginBottom = show_point.margin_bottom + 'px';
			};

		};
						
		
		hint_container.className = positionClass_1 + positionClass_2 + '_1218';
		hint_container.style.display = '';
	},
	
	
	hide: function (event) {
		if (! SITEHELP_HINT_1218.hint_container) return;
		SITEHELP_HINT_1218.hint_container.style.display = 'none';
		
		try { event.stopPropagation(); event.cancelBubble = true; } catch (r) {};
	},
	
	
	
	
	
	
	
	
	/////////////// INTERNAL FUNC ///////////////
	
	__my_open_chat: function () {
		SITEHELP_HINT_1218.hide(); 
		SITEHELP_TEMPLATE_1218.open_chat_window();
	},
	
	__get_browser_size: function () {
		var e = window, a = 'inner';
		if ( !( 'innerWidth' in window ) ) {
			a = 'client';
			e = document.documentElement || document.body;
		};
		return { width : e[ a+'Width' ] , height : e[ a+'Height' ] }
	}
};
		SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '<style type="text/css">';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	div.SITEHELP_RightBottom_1218 {';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		background: url(https://c.sitehelp.im/img/hint_template/0/rb.png) no-repeat;';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	div.SITEHELP_RightTop_1218 {';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		background: url(https://c.sitehelp.im/img/hint_template/0/rt.png) no-repeat;';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	div.SITEHELP_LeftBottom_1218 {';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		background: url(https://c.sitehelp.im/img/hint_template/0/lb.png) no-repeat;';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	div.SITEHELP_LeftTop_1218 {';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		background: url(https://c.sitehelp.im/img/hint_template/0/lt.png) no-repeat;';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	div.SITEHELP_HINT_BTN_1218 {';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		border: 1px solid lightgray; ';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	  color: gray; ';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	  cursor: pointer;';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	  padding: 3px 5px;';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	  float: left;';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	  font-size: 12px;';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	#SITEHELP_HINT_CONTAINER_1218 {';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		border: 0; ';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		margin: 0; ';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		padding: 0; ';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		text-align: left;';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		z-index: 2100000100;';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	}';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '</style>';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '<div id="SITEHELP_HINT_CONTAINER_1218" style="display: none; position: absolute;">';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	<div style="width: 248px; height: 207px; margin: 0; padding: 0; text-align: left;">';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		<div onclick="SITEHELP_HINT_1218.__my_open_chat();" style="cursor: pointer; position: relative; width: 200px; height: 148px; overflow: auto; text-align: left; margin: 0; padding: 5px; top: 23px; left: 18px;">';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '		  ';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '			<div style="float: right; border: 1px solid lightgray; padding: 0px 3px; color: lightgray; cursor: pointer; margin-left: 1px; margin-bottom: 5px; display: none;" id="SITEHELP_HINT_CLOSE_BTN_X_1218" onclick="SITEHELP_HINT_1218.hide(event);" title="&#1047;&#1072;&#1082;&#1088;&#1099;&#1090;&#1100;">X</div>';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '			';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '			<span id="SITEHELP_HINT_TEXT_CONTAINER_1218" style=" color: black; font-size: 14px;"></span>';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '			';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '			<div style="position: absolute; bottom:0; width: 190px;">';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '       <table style="margin: 0 auto;">';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '        <tr>';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '          <td>';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '      			<div style="" class="SITEHELP_HINT_BTN_1218" id="SITEHELP_HINT_START_CHAT_BTN_1218" onclick="SITEHELP_HINT_1218.__my_open_chat();">&#1053;&#1072;&#1095;&#1072;&#1090;&#1100;&#32;&#1095;&#1072;&#1090;</div>';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '					  <div style="margin-left: 5px; " class="SITEHELP_HINT_BTN_1218" id="SITEHELP_HINT_CLOSE_BTN_1218" onclick="SITEHELP_HINT_1218.hide(event);">&#1047;&#1072;&#1082;&#1088;&#1099;&#1090;&#1100;</div>';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '          </td>';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '          ';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '        </tr>';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '       </table>';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '			</div>';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '	</div>';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += '</div>';
SITEHELP_HINT_1218.TEMPLATE_HTML_CODE += "\n";
		
		//form JS
		var SITEHELP_NEED_JQUERY_1218 = 0;
var SITEHELP_NEED_JQUERY_UI_1218 = 0;


<!-- we need this for form show/hide animation -->
	SITEHELP_NEED_JQUERY_1218 = 1;






if ((typeof jQuery == 'undefined') && (SITEHELP_NEED_JQUERY_1218 == 1)) {
	var s = document.createElement('script');
	s.type = 'text/javascript';
	s.charset = 'utf-8';
	s.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js';

	if (SITEHELP_NEED_JQUERY_UI_1218 == 1) {
		s.onload = function () {
			var s_ui = document.createElement('script');
			s_ui.type = 'text/javascript';
			s_ui.charset = 'utf-8';
			s_ui.src = 'https://code.jquery.com/ui/1.11.2/jquery-ui.min.js';
			document.body.appendChild(s_ui);
		};
	};

	document.body.appendChild(s);
};




var SITEHELP_TEMPLATE_1218 = {
	//mandatory functions
	curr_operator_status: '',
	partial_msg_tracking_enabled: true,
	partial_msg_tracking_update_time_MSEC: 5000,
	__offline_actions: [],
	
	init: function (params) {
		//params.operator_status = 'online' || 'offline'
		
		//params.partial_msg_tracking_enabled = 1 | 0
		//params.partial_msg_tracking_update_time_sec = INT
		
		//params.opinions :  array of objects:
		// {
		//  id: id of opinion
		//  text: text to diaply
		//	want_comment: 1|0  whether or not ask user for comments when choosing this variant
		// }, ... {}, {} ...


		SITEHELP_TEMPLATE_1218.partial_msg_tracking_enabled = params.partial_msg_tracking_enabled;
		SITEHELP_TEMPLATE_1218.partial_msg_tracking_update_time_MSEC = 1000 * params.partial_msg_tracking_update_time_sec;

		
		//init 'messages' iframe
		var MSGS_style = '';
		if (navigator.userAgent.match(/(iPod|iPhone|iPad)/) && navigator.userAgent.match(/WebKit/)) {                                                                                            
			MSGS_style = 'height:1px; min-height:100%; overflow: scroll;';                                                                                             
		};
		
		var fr = window.frames.SITEHELP_MSGS_IFR_1218;
		var d = fr.document;
		d.open();
		d.write('<html><head><META HTTP-EQUIV="Pragma" CONTENT="No-Cache"><META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE"><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><base target="_Blank"></head>');
		d.write('<body leftmargin="0" topmargin="0" rightmargin="0" bottommargin="0" marginwidth="0" marginheight="0">');
		
		d.write('	\
		<style type="text/css"> \
      body * { \
		  	font-family: Arial, Verdana; \
		  	font-size: 12px; \
      } \
			\
			table { \
				padding: 0; \
				margin: 0; \
				border-collapse: collapse; \
				border-spacing: 0; \
			} \
			\
			td.op_dt { \
			    text-align: right; \
			    width: 28px; \
			    padding-right: 5px; \
			    color: #d6d5d5; \
			    font-size: 9px; \
			    vertical-align: middle; \
			} \
			td.my_dt { \
			    text-align: left; \
			    width: 35px; \
			    padding-left: 5px; \
			    color: #2d2d2d; \
			    font-size: 9px; \
			    vertical-align: middle; \
			} \
			td.msg_from_op_triangle, td.msg_from_cli_triangle { \
			    height: 6px; \
			    width: 10px; \
			} \
			td.empty_spacer { \
			    width: 10px; \
			}\
			div.dv1 { \
			    float: right; \
			    clear: both; \
			    width: 10px; \
			    height: 6px; \
			    background: linear-gradient(15deg, rgba(255, 255, 255, 0), rgba(0, 0, 0, 0) 35%, rgba(70, 123, 173, 0.7) 35%, rgba(70, 123, 173, 1) 100%); \
			} \
			\
			div.dv4 { \
			    float: left; \
			    clear: both; \
			    width: 10px; \
			    height: 6px; \
			    background: linear-gradient(335deg, rgba(255, 255, 255, 0), rgba(0, 0, 0, 0) 35%, rgba(187, 186, 187, 0.7) 35%, rgba(187, 186, 187, 1) 100%); \
			} \
			\
			div.msg_from_op { \
			    background: #467bad; \
			    border-radius: 3px; \
			    padding: 5px 0 5px 5px; \
			    width: 100%; \
			    float: left; \
			    box-sizing: border-box; \
			} \
			td.msg_from_op_msg { \
			    padding: 3px; \
			    color: white; \
			    word-wrap: break-word; \
			    word-break: break-all; \
			} \
			\
			div.msg_from_cli { \
			    background: #bbbabb; \
			    border-radius: 3px; \
			    padding: 5px 5px 5px 0px; \
			    width: 100%; \
			    float: right; \
			    box-sizing: border-box; \
			} \
			td.msg_from_cli_msg { \
			    padding: 3px; \
			    color: #3b3b3b; \
			    text-align: right; \
			    word-wrap: break-word; \
			    word-break: break-all; \
			} \
			div.msg_line { \
			 padding-top: 7px; \
			}\
			div.msg_line_form { \
			 padding: 7px 10px 7px 10px; \
			}\
			#MSGS_CONTAINER { \
				padding: 0 2px 7px 2px; \
			} \
			</style>	\
		');
		
		d.write('<div id="MSGS_CONTAINER" style="' + MSGS_style + '"></div>');
		d.write('<div id="OPERATOR_TYPING_CONTAINER" style="display: none; opacity: 0.5; padding: 0 0 7px 3px;">	\
			<table width=100% cellpadding=0 cellspacing=0> \
			<tr> \
				<td class="msg_from_op_triangle"><div class="dv1"></div></td> \
				<td class="msg_from_op"> \
					<div class="msg_from_op"> \
						<table cellpadding=0 cellspasing=0 width=100%> \
							<tr> \
								<td class="msg_from_op_msg" id="OPERATOR_TYPING_MSG"></td> \
								<td class="op_dt"></td> \
							</tr> \
						</table> \
					</div> \
				</td> \
				<td class="empty_spacer"></td> \
			</tr>\
			</table> \
			</div>');
		d.write('</bo' + 'dy></ht' + 'ml>');
		d.close();

		
		
		SITEHELP_TEMPLATE_1218.msgs_ifr = fr;
		SITEHELP_TEMPLATE_1218.msgs_container = d.getElementById('MSGS_CONTAINER');
		
		//here NOT d. , but DOCUMENT 
		SITEHELP_TEMPLATE_1218.top_form_container_tr = document.getElementById('TOP_FORM_CONTAINER_TR');
		SITEHELP_TEMPLATE_1218.top_form_container = document.getElementById('TOP_FORM_CONTAINER');
		SITEHELP_TEMPLATE_1218.bottom_form_container_tr = document.getElementById('BOTTOM_FORM_CONTAINER_TR');
		SITEHELP_TEMPLATE_1218.bottom_form_container = document.getElementById('BOTTOM_FORM_CONTAINER');
		
		SITEHELP_TEMPLATE_1218.operator_typing_container = d.getElementById('OPERATOR_TYPING_CONTAINER');
		SITEHELP_TEMPLATE_1218.operator_typing_msg_container = d.getElementById('OPERATOR_TYPING_MSG');
		
		SITEHELP_TEMPLATE_1218.__iframe_import_CSS();
		
		//init 'leave opinion dialog'
		var opinions_html_code = '<table cellpadding=0 cellspacing=0 style="margin: 0; padding: 0;">';
		opinions_html_code += '<tr id="SITEHELP_OPINION_HEADER_1218"><td>Оставить отзыв</td><td width=10 style="padding: 0 1px 0 5px !important;" align=center><a style="text-decoration: none;" href="#" onclick="SITEHELP_TEMPLATE_1218.local_hide_opinion_dialog(); return false;" title="закрыть">x</a></td></tr>';

		for (var i=0; i < params.opinions.length; i++) {
			opinions_html_code += '<tr>';
			opinions_html_code += '<td colspan=2 class="SITEHELP_OPINION_LIST_1218" onclick="SITEHELP_TEMPLATE_1218.local_opinion_set(' + params.opinions[i].id + ',' + params.opinions[i].want_comment + ')">' + params.opinions[i].text + '</td>';
			opinions_html_code += '</tr>';
		};

		opinions_html_code += '</table>';

		var dv = document.createElement('div');
		dv.setAttribute('id', 'SITEHELP_OPINION_BOX_1218');
		dv.setAttribute('style', 'z-index: 100000000000;');
		dv.style.zIndex = 100000000000;
		dv.innerHTML = opinions_html_code;
		dv.style.display = 'none';
		document.body.appendChild(dv);
		
		SITEHELP_TEMPLATE_1218.original_form_height = document.getElementById('SITEHELP_SET_HEIGHT_TD_1218').style.height;
	},
	
	
	//	
	__iframe_import_CSS: function () {
		var fr = SITEHELP_TEMPLATE_1218.msgs_ifr;
		var css = document.getElementById('SITEHELP_CSS_1218');
		if (! css) return;
		
    var st = fr.document.createElement("style");
    st.type = "text/css";
    try {
     st.innerHTML = css.innerText;
    } catch (ex) {
     st.styleSheet.cssText = css.innerText;  // IE8 and earlier
    };
    
    fr.document.getElementsByTagName("head")[0].appendChild(st);
	},
	

	operator_status_changed: function (params) {
		//params.operator_status = 'online' || 'offline' || 'connecting' || 'error' | 'no_empty_accounts'
		
		//--- params.operator_status == 'online' || 'offline'
		//>>>no additional params		
		
		//--- params.operator_status == 'offline'
		//>>> params.actions = [			// list of actions to do
		//>>>   {
		//>>>   	action: 'form' | 'message'
		//>>>   	param: 'form_ID' | 'message_text'
		//>>>   }
		//>>> ]
		
		//--- params.operator_status == 'connecting' || 'no_empty_accounts'
		//>>> no additional params
		
		//--- params.operator_status == 'error'
		//>>> params.error_message => text error
		
		var circle_el = document.getElementById('SITEHELP_OP_STATUS_CIRCLE_1218');
		var text_el = document.getElementById('SITEHELP_OP_STATUS_TEXT_1218');
		text_el.style.color = '#4da92a';
		circle_el.className = 'SITEHELP_OP_STATUS_CIRCLE_ONLINE_1218';
	
		if (params.operator_status == 'connecting') {
			text_el.style.color = 'gray';
			circle_el.className = 'SITEHELP_OP_STATUS_CIRCLE_UNKNOWN_1218';
			text_el.innerHTML = 'подключение';
		};
	

		if (params.operator_status == 'online') {
			text_el.style.color = '#4da92a';
			circle_el.className = 'SITEHELP_OP_STATUS_CIRCLE_ONLINE_1218';
			text_el.innerHTML = 'онлайн';
		};
		
		if (params.operator_status == 'offline') {
			circle_el.className = 'SITEHELP_OP_STATUS_CIRCLE_OFFLINE_1218';
			text_el.style.color = 'red';
			text_el.innerHTML = 'оффлайн';
		};
		
		if (params.operator_status == 'no_empty_accounts') {
			circle_el.className = 'SITEHELP_OP_STATUS_CIRCLE_OFFLINE_1218';
			text_el.innerHTML = 'нет свободных каналов';
		};
		
		if (params.operator_status == 'error') {
			circle_el.className = 'SITEHELP_OP_STATUS_CIRCLE_OFFLINE_1218';
			text_el.innerHTML = 'ошибка соединения с оператором';
		};
		
		
		//////////
		var online_offline_op_status;
		
		if (! ((params.operator_status == 'online') || (params.operator_status == 'offline')) ) {
			return; // NO FUTHER procrssing of statuses. only online and offline
		};
		
		if (SITEHELP_TEMPLATE_1218.curr_operator_status == params.operator_status) return;
		SITEHELP_TEMPLATE_1218.curr_operator_status = params.operator_status;
		
		if (params.operator_status == 'online') {
			SITEHELP_TEMPLATE_1218.__show_layer('online');
		}; 

		if (params.operator_status == 'offline') {
			SITEHELP_TEMPLATE_1218.__offline_actions = params.actions;
			SITEHELP_TEMPLATE_1218.__show_layer('offline');
		}; 
	},
	
	
	__show_layer: function (layer) {
		
		if (layer == 'default') {
			if (SITEHELP_TEMPLATE_1218.curr_operator_status == 'online') {
				layer = 'online';
			};
			
			if (SITEHELP_TEMPLATE_1218.curr_operator_status == 'offline') {
				layer = 'offline';
			};
		};
		
		//for state 'connecting', etc, .
		if (layer == 'default') {
			layer = 'loading';
		};
				
		
		var loading_layer_visible = false;
		var modal_layer_visible = false;
		var online_layer_visible = false;
		var footer_visible = false;
		var send_btn_visible = false;
		
		var reset_from_height = false;
		var set_original_from_height = true;
		
		if (layer == 'online') {
			online_layer_visible = true;
			footer_visible = true;
			send_btn_visible = true;
		};
	
		if (layer == 'loading') {
			loading_layer_visible = true;
		};
		
		if (layer == 'modal_form') {
			modal_layer_visible = true;
			reset_from_height = true;
		};
	
	
		if (layer == 'offline') {
			
			for (var i=0; i < SITEHELP_TEMPLATE_1218.__offline_actions.length; i++) {
				var this_action = SITEHELP_TEMPLATE_1218.__offline_actions[i];
				
				if (this_action.action == 'form') {
					SITEHELP_TEMPLATE_1218.local_on_chat_message({
						"type": 'form',
						"text": this_action.param, 
						"to": "client", 
						"dt": "",
						"id": 0,
						"is_info": 1,
						"by_human": 0
					});
					continue;
				};
				
				
				if (this_action.action == 'message') {
					online_layer_visible = true;
					
					SITEHELP_TEMPLATE_1218.local_on_chat_message({
						"type": 'msg',
						"text": this_action.param, 
						"to": "client", 
						"dt": "", 
						"id": 0, 
						"is_info": 1,
						"by_human": 0
					});
					
					continue;
				};
			};
			
		};
	
	
		document.getElementById('LOADING_LAYER_1218').style.display = loading_layer_visible ? '' : 'none';
		document.getElementById('MODAL_FORM_LAYER_1218').style.display = modal_layer_visible ? '' : 'none';
		document.getElementById('ONLINE_LAYER_1218').style.display = online_layer_visible ? '' : 'none';
		
		document.getElementById('SITEHELP_SEND_BTN_CONTAINER_1218').style.display = send_btn_visible ? '' : 'none';
		//document.getElementById('SITEHELP_FOOTER_1218').style.display = footer_visible ? '' : 'none';
		
		if (reset_from_height) {
			document.getElementById('SITEHELP_SET_HEIGHT_TD_1218').style.height = null;
		};
		
		if (set_original_from_height && (! reset_from_height)) {
			document.getElementById('SITEHELP_SET_HEIGHT_TD_1218').style.height = SITEHELP_TEMPLATE_1218.original_form_height;
		};
	},
	
	
	
	operator_data_changed: function (params) {
		//params.name - name of currently assigned operator
		//params.photo - abs path to image
		
		if (typeof params.photo != 'undefined') {
			document.getElementById('SITEHELP_OPERATOR_PHOTO_1218').src = params.photo;
		};
	},
	
	
	operator_activity: function (params) {
		//params.type == 'operator_typing'			- operator keyboard activity
		//params.status = 'composing' || 'paused' || ''				('' = clear status)
		
		if (params.type == 'operator_typing') {
			
			if (params.status == '') {
				SITEHELP_TEMPLATE_1218.operator_typing_container.style.display = 'none';
				SITEHELP_TEMPLATE_1218.operator_typing_msg_container.innerHTML = '';
			};
			
			if (params.status == 'paused') {
				SITEHELP_TEMPLATE_1218.operator_typing_container.style.display = '';
				SITEHELP_TEMPLATE_1218.operator_typing_msg_container.innerHTML = 'оператор приостановил печать ...';
			};
			
			if (params.status == 'composing') {
				SITEHELP_TEMPLATE_1218.operator_typing_container.style.display = '';
				SITEHELP_TEMPLATE_1218.operator_typing_msg_container.innerHTML = '<img src="data:image/gif;base64,R0lGODlhEAAQAOZ8AIhVAO2rAP+6AJdoGMCFAYhVA+mnAJttH9ycAMCme9CSAPu3AJxzLqVyELR9CI5ZAK6ZeP/+/N7Ru7+jdqSFUMzJwPGuAKaLXcWLC49dCJZpHeqoAMqOBJ9oAJFcAL2DBJJiEbuAAP25Ar61p9mZAMbEwIhWA6J/RO3l2f/1255rD7F8DfPt5bF7DY5cB4dUANOUANLIq9fHrMbDv4xYALh/CpluJPKyC7GMTubbyrmtmbZ+B62Ydd6gB49aAIVSAJhiAJ12M8GmeKNxE93Eg7Z+CraVXax3DsjHxIpWAJtoDP+9DMnJyI5aAP24AMjGxP/yz4tXAIhWBPCvB/v697J8COPCa7iACdqbANTDpvS7I+akAMC4rNrLso1ZAKmBPZdlDf/AFf/BG/++D7yxoKeMYf/vw7uBB//tvc+RAN7Efs/It7WTWZ9sDIZTAKmNX72hcrORVopYBaaJWpdkC6l1D/ezAMmRDvCtAJRiCv///8rKygAAAAAAAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgB8ACwAAAAAEAAQAAAHaIB8fDSChYaGAA8hXoeNgh0CHo6NPgQIDHuZmpqGLk4NEnqio3p7hhRnAQOko6aFSFJ2VRebe6WGexMtG0Ost4W2Nj1atb+CtnpQYhGsrselezFrm8Z8yL6iztbQtbba19jf3bWT5XyBACH5BAkKAHwALAAAAAAQABAAAAdogHyCg4SFhoeIg01RAIh7j3szcnh0I5CEe3qaE1cGB5p6e5igBwZFCaCig5l7ZEoCBU+PoaN6RgQwOKC0q6EFC206kLyCmVkrAQO7xHysNxxzkKy1S2jLzJkVRNKzqsXXu97N3OSJiYEAIfkECRQAfAAsAAAAABAAEAAAB2uAfIKDhIWGh4huAEAAiIJ7ezw7WxqQlnuEe3ooYAImVHqhepiDmnoDAUcyoqOZoxQECieWraWhEg0BA6ykj6N7BQt5XJC1vqFfWDVCor18mpBldyIVxc6moSljvK6XarTXrOLGz5fmkI6OgQAh+QQFFAB8ACwAAAAAEAAQAAAHaYB8goOEhYaHiIYvSQ+Fe4+QexAOCAx7hHt6mptxCgRwl4OZm5oHBnVdoYKZkUw/AhksqnyjmzkqFiB6s6yQkyRBu5ikemxpHwnCoruQb1MYJcqrxHphZpq8zJBWj9K01BGbvJHkj4mJgQA7" style="padding-right:4px;">оператор печатает ...';
			};
			
			SITEHELP_TEMPLATE_1218.scrol_msg_list_to_bottom();
		};
		
	},
	
	open_chat_window: function (params) {
		SITEHELP_TEMPLATE_1218.tmpl_open_window();
		
		//notify 'core' that chat_window is open now 
		SITEHELP_1218.notify_window_state_changed({state: 'open'});
		SITEHELP_TEMPLATE_1218.chat_window_open = true;
		
		SITEHELP_TEMPLATE_1218.scrol_msg_list_to_bottom();
	},
	
	close_chat_window: function (params) {
		SITEHELP_TEMPLATE_1218.tmpl_close_window();
		
		//notify 'core' that chat_window is closed now 
		SITEHELP_1218.notify_window_state_changed({state: 'closed'});
		SITEHELP_TEMPLATE_1218.chat_window_open = false;
	},
	
	
	full_chat_log_data: function (params) {
		//params.msgs: array of 'msg_obj': (see operator_message function for description)
		
		SITEHELP_TEMPLATE_1218.msgs_container.innerHTML = '';
		SITEHELP_TEMPLATE_1218.msgs_count = 0;
		
		for (var i=0; i < params.msgs.length; i++) {
			SITEHELP_TEMPLATE_1218.local_on_chat_message(params.msgs[i], false);
		};
	},
	
	on_chat_message: function (msg_obj) {
		// msg_obj: {
		//	type: msg || form					(text = form_id for [type=form])
		//	completed: 0 | 1   (ONLY FOR FORM)
		//  text: text of message	(already processed for smiles/html chars, so it's ready to 'display') OR form_id
		//  dt: datetime of message in format 'YYYY-MM-DD HH:MM:SS'
		//	to: 'client' || 'operator'
		//  id: internal id of msg
		//  is_info: 1|0  (1 = server info msg)
		//  operator_name: name of opertor who wrote this msg
		//  show_operator_name: 1|0 display operator name or not (set to 0 for welcome msg)
		//  by_human: 0|1   (1= wrote by human, 0=generated automatically by autioinitiate rule or in other way)
		// }
		
		SITEHELP_TEMPLATE_1218.local_on_chat_message(msg_obj, true);
	},
	
	
	//
	__QF_cached_form_data: [],
	__QF_blink_field_error_count: 10,
		
	
	//form data callback by call to 'get_form_data'
	form_data: function (obj) {
		//obj.msg_id - id of message
		
		//obj.form_data::
		//form_data.ID - int
		
		//form_data.options = {}
		//form_data.options.display	 "modal", "top", "bottom", "inchat"
		
		
		//form_data.fields = []
		//form_data.fields ITEM: {
		//	ID: ...
		//	name: ...
		//	var_name: ...
		//	type: 'int', 'string', 'select', 'select-row', 'select-column', button   (+ SPECIAL:  'header' and 'title', 'hidden', 'img' )
		//	options: {
		//		required: 0|1
		//		lines: INT			(1 = input text,  >=2  - textarea)
		//		min_length: INT  (min input length)
		//		type: 		'submit', 'close_chat', 'close_form'  (for BUTTON)
		//	}
		//	default_value: 	'default value is here'
		//	values: [
		//		'value|display_value'    or only 'display_value'
		//		....
		//	]
		//}
		
		var CLASS_FOR_REPLACE = 'REPLACE_CLASS_1218';
		
		var js_call_prefix = (obj.form_data.options.display == 'inchat') ? 'parent.' : '';
		var rows = [];
		var cols = [];
		
		for (var i=0; i < obj.form_data.fields.length; i++) {
			var field = obj.form_data.fields[i];
			
			if (field.type == 'hidden') {
				rows.push(['<input id="FORM_INPUT_1218_' + obj.form_data.ID + '_' + field.ID + '" type="hidden" name="' + field.var_name + '" value="' + field.value + '" orig_value="">', '']);
				cols.push([]);
				continue;
			};
			
			if (field.type == 'img') {
				rows.push(['<tr class="FORM_IMG_1218 ' + CLASS_FOR_REPLACE + '">', '</tr>']);
				cols.push(['<td>', '<img style="display: block; margin: auto;" src="' + field.value + '" alt="' + field.name + '" />', '</td>']);
				continue;
			};
			
			if (field.type == 'header') {
				rows.push(['<tr class="FORM_HEADER_1218 ' + CLASS_FOR_REPLACE + '">', '</tr>']);
				cols.push(['<td>', '<h1>' + field.name + '</h1>', '</td>']);
				continue;
			};
			
			if (field.type == 'title') {
				rows.push(['<tr class="FORM_TITLE_1218 ' + CLASS_FOR_REPLACE + '">', '</tr>']);
				cols.push(['<td>', '<h3>' + field.name + '</h3>', '</td>']);
				continue;
			};
			
			if (field.type == 'int') {
				if (field.name.length > 0) {
					rows.push(['<tr class="FORM_FIELD_TITLE_1218">', '</tr>']);
					cols.push([
					'<td>', 
						field.name,
					'</td>',
					]);
				};
				
				rows.push(['<tr class="FORM_FIELD_1218 FORM_FIELD_INT_1218 ' + CLASS_FOR_REPLACE + '">', '</tr>']);
				cols.push([
				'<td>', 
				'<input id="FORM_INPUT_1218_' + obj.form_data.ID + '_' + field.ID + '" type="text" name="' + field.var_name + '" value="' + field.value + '" orig_value="' + field.value + '" onfocus="' + js_call_prefix + 'SITEHELP_TEMPLATE_1218.__form_el_focus(this, \'' + field.value + '\');" onblur="' + js_call_prefix + 'SITEHELP_TEMPLATE_1218.__form_el_blur(this, \'' + field.value + '\');"' + '>', 
				'</td>'
				]);
				
				continue;
			};
			
			
			if (field.type == 'string') {
				if (field.name.length > 0) {
					rows.push(['<tr class="FORM_FIELD_TITLE_1218">', '</tr>']);
					cols.push([
					'<td>', 
						field.name,
					'</td>',
					]);
				};
				
				
				
				rows.push( ['<tr class="FORM_FIELD_1218 FORM_FIELD_STRING_1218 ' + CLASS_FOR_REPLACE + '">', '</tr>'] );
				
				var arr = ['<td>', '', '</td>'];
				
				if (field.options.lines == 1) {
					arr[1] = '<input id="FORM_INPUT_1218_' + obj.form_data.ID + '_' + field.ID + '" type="text" name="' + field.var_name + '" value="' + field.value + '" orig_value="' + field.value + '" onfocus="' + js_call_prefix + 'SITEHELP_TEMPLATE_1218.__form_el_focus(this, \'' + field.value + '\');" onblur="' + js_call_prefix + 'SITEHELP_TEMPLATE_1218.__form_el_blur(this, \'' + field.value + '\');"' + '>';
				} else {
					arr[1] = '<textarea id="FORM_INPUT_1218_' + obj.form_data.ID + '_' + field.ID + '" rows="' + field.options.lines + '" name="' + field.var_name + '" orig_value="' + field.value + '" onfocus="' + js_call_prefix + 'SITEHELP_TEMPLATE_1218.__form_el_focus(this, \'' + field.value + '\');" onblur="' + js_call_prefix + 'SITEHELP_TEMPLATE_1218.__form_el_blur(this, \'' + field.value + '\');"' + '>' + field.value + '</textarea>';
				};
				
				cols.push(arr);
				continue;
			};
			
			
			if (field.type == 'select') {
				if (field.name.length > 0) {
					rows.push(['<tr class="FORM_FIELD_TITLE_1218">', '</tr>']);
					cols.push([
					'<td>', 
						field.name,
					'</td>',
					]);
				};
				
				rows.push( ['<tr class="FORM_FIELD_1218 FORM_FIELD_SELECT_1218 ' + CLASS_FOR_REPLACE + '">', '</tr>'] );
				
				
				var select_el_html = '<select id="FORM_INPUT_1218_' + obj.form_data.ID + '_' + field.ID + '" name="' + field.var_name + '">';
				
				for (var k=0; k < field.values.length; k++) {
					var sel = '';
					
					var val, display_value;
					
					if (field.values[k].match(/^(.*?)\|(.*)/)) {
						val = RegExp.$1;
						display_value = RegExp.$2;
					} else {
						val = field.values[k];
						display_value = field.values[k];
					};
					
					if (field.default_value == val) {
						sel = 'selected';
					};
					
					select_el_html += '<option value="' + val + '"' + sel + ' >' + display_value + '</option>';
				};
				
				select_el_html += '</select>';
				
				
				cols.push(['<td>', select_el_html, '</td>']);
				continue;
			};
			
			
			if (field.type == 'select-column') {
				for (var k=0; k < field.values.length; k++) {
					//html += '<tr class="FORM_FIELD_1218 FORM_FIELD_SELECT_COL_1218 ' + CLASS_FOR_REPLACE + '"><td>';
					//html += '<div onclick="SITEHELP_TEMPLATE_1218.__FormFieldSelectCol(' + obj.form_data.ID + ', ' + field.ID + ')" id="FORM_FIELD_SELECT_COL_1218_' + obj.form_data.ID + '_' + field.ID + '">' + field.values[k] + '</div>';
					//html += '</td></tr>';
				};
				continue;
			};
			
			
			if (field.type == 'button') {
				var this_btn_html = '<button id="FORM_BUTTON_1218_' + obj.form_data.ID + '_' + field.ID + '" name="' + field.var_name + '" value="' + field.value + '" onclick="' + js_call_prefix + 'SITEHELP_TEMPLATE_1218.__QF_button_click(' + obj.form_data.ID + ', ' + obj.msg_id + ', \'' + field.options.type + '\')">' + field.name + '</button>';
				
				if ((field.options.on_prev_line == 1) && (cols.length > 0)) {
					rows[rows.length-1][0] = rows[rows.length-1][0].replace(CLASS_FOR_REPLACE, 'FORM_BUTTON_CONTAINER_1218 ' + CLASS_FOR_REPLACE);
					
					var col_html = field.options.html_container;
					col_html = col_html.replace(field.options.line_1_var, cols[cols.length-1][1]);
					col_html = col_html.replace(field.options.line_2_var, this_btn_html);
					cols[cols.length-1][1] = col_html;
					
				} else {
					rows.push( ['<tr class="FORM_BUTTON_CONTAINER_1218 ' + CLASS_FOR_REPLACE + '">', '</tr>'] );
					cols.push( ['<td colspan=2>', this_btn_html, '</td>'] );
				};

				continue;
			};
			

		};
		
		var html = '<table id="FORM_1218" cellpadding=0 cellspacing=0 style="width: 100%;">';
		for (var i=0; i < rows.length; i++) {
			rows[i][0] = rows[i][0].replace(CLASS_FOR_REPLACE, '');
			
			html += rows[i][0];
			
			for (var k=0; k < cols[i].length; k++) {
				html += cols[i][k];
			};
			
			html += rows[i][1];
		};
		html += '</table>';
		
		
		//save for future use
		SITEHELP_TEMPLATE_1218.__QF_cached_form_data.push(obj);
		SITEHELP_TEMPLATE_1218.__QF_show_form(obj.form_data.options.display, html, obj.msg_id);
	},
	
	
	
	send_form_data_result: function (result) {
		
		var frm_obj = SITEHELP_TEMPLATE_1218.__QF_get_cached_form_data(result.form_id, result.msg_id);
		if (! frm_obj) return;
		
		var d = document;
		
		if (frm_obj.form_data.options.display == 'inchat') {
			d = SITEHELP_TEMPLATE_1218.msgs_ifr.document;
		};
		
		var form_closed = false;
		
		if (result.result == 1) {
			
			for (var i = 0; i < result.cmd.length; i++) {
				var cmd = result.cmd[i];
				
				if (cmd.action == 'CLOSE_FORM') {
					SITEHELP_TEMPLATE_1218.__QF_hide_form(frm_obj.form_data.options.display, result.form_id, result.msg_id);					
					SITEHELP_1218.notify_form_completed(result.form_id, result.msg_id, cmd.secret);
					form_closed = true;
					continue;
				};
				
				if (cmd.action == 'CLOSE_CHAT') {
					SITEHELP_TEMPLATE_1218.close_chat_window();
					SITEHELP_1218.notify_form_completed(result.form_id, result.msg_id, cmd.secret);
					form_closed = true;
					continue;
				};
				
				if (cmd.action == 'FORM_ERROR') {
					var err_processed = false;
					
					if (cmd.error_type == 'field') {
						var field_id;
						
						var fields = d.querySelectorAll('*[id^="FORM_INPUT_1218_' + result.form_id + '_"]');
						
						for (var i=0; i < fields.length; i++) {
							if (fields[i].name == cmd.field) {
								field_id = fields[i].id;
								break;
							};
						};
						
						if (field_id) {
							err_processed = true;
							SITEHELP_TEMPLATE_1218.__QF_blink_field_error(frm_obj.form_data.options.display == 'inchat' ? true : false, field_id, 'FORM_INPUT_ERROR_1218', true);
						};
					};
					
					if (! err_processed) alert(cmd.error_msg);
					
					
					//enable all buttons
					var btns = d.querySelectorAll('*[id^="FORM_BUTTON_1218_' + result.form_id + '_"]');
					
					for (var i=0; i < btns.length; i++) {
						var btn = btns[i];
						btn.className = '';
						btn.disabled = false;
					};
					
					continue;
				};
				
				
			};
			
		} else {
		};
		
		if (form_closed) {
			SITEHELP_1218.reload_history();
		};
	},
	

	
	__QF_get_cached_form_data: function (form_id, msg_id) {
		
		for (var i=0; i < SITEHELP_TEMPLATE_1218.__QF_cached_form_data.length; i++) {
			if (! (SITEHELP_TEMPLATE_1218.__QF_cached_form_data[i].msg_id == msg_id)) continue;
			if (! (SITEHELP_TEMPLATE_1218.__QF_cached_form_data[i].form_data.ID == form_id)) continue;
			return SITEHELP_TEMPLATE_1218.__QF_cached_form_data[i];
		};
		
	},
	
	__QF_button_click: function (form_id, msg_id, action) {
		var frm_obj = SITEHELP_TEMPLATE_1218.__QF_get_cached_form_data(form_id, msg_id);
		if (! frm_obj) return;
		
		var d = document;
		
		if (frm_obj.form_data.options.display == 'inchat') {
			d = SITEHELP_TEMPLATE_1218.msgs_ifr.document;
		};
		
		
		if ((action == 'submit') || (action == 'cancel')) {
			//disable all buttons
			var btns = d.querySelectorAll('*[id^="FORM_BUTTON_1218_' + form_id + '_"]');
			
			for (var i=0; i < btns.length; i++) {
				var btn = btns[i];
				btn.className = 'FORM_BUTTON_DISABLED_1218';
				btn.disabled = true;
			};
		};
		
		
		if (action == 'submit') {		//validatation of fields is NOT needed
			var data = 'action=submit';
			
			var fields = d.querySelectorAll('*[id^="FORM_INPUT_1218_' + form_id + '_"]');
			
			for (var i=0; i < fields.length; i++) {
				var field = fields[i];
				var orig_value = field.getAttribute('orig_value');
				
				if (orig_value && (orig_value == field.value)) {
					//do not send UNFILLED field
				} else {
					if (field.type == 'hidden') {
						data += '&' + field.name + '=' + escape(field.value);
					};
					
					if (field.type == 'text') {
						data += '&' + field.name + '=' + escape(field.value);
					};
					
					if (field.type == 'textarea') {
						data += '&' + field.name + '=' + escape(field.value);
					};
					
					if (field.type == 'select-one') {
						data += '&' + field.name + '=' + escape(field.value);
						data += '&' + field.name + '__TEXT=' + escape(field.options[field.selectedIndex].text);
					};
				};
			};
			
			SITEHELP_1218.send_form_data(form_id, msg_id, data);
			return;
		};
		
		if (action == 'cancel') {
			SITEHELP_1218.send_form_data(form_id, msg_id, 'action=cancel');
			return;
		};
		
		if (action == 'close_chat') {
			SITEHELP_TEMPLATE_1218.close_chat_window();
			return;
		};
		
	},
	
	__QF_blink_field_error: function (in_iframe, el_id, el_class, flag) {
		var el
		
		if (in_iframe) {
			el = SITEHELP_TEMPLATE_1218.msgs_ifr.document.getElementById(el_id);
		} else {
			el = document.getElementById(el_id);
		};
		
		if (! el) return;

		
		if (SITEHELP_TEMPLATE_1218.__QF_blink_field_error_count-- <= 0) {
			SITEHELP_TEMPLATE_1218.__QF_blink_field_error_count = 7; //reset
			el.className = el.className.replace(el_class, '');
			return;
		};
		
		if (flag) {
			el.className += ' ' + el_class;
		} else {
			el.className = el.className.replace(el_class, '');
		};
		
		var code = 'SITEHELP_TEMPLATE_1218.__QF_blink_field_error(' + (in_iframe ? 'true' : 'false') + ',\'' + el_id + '\',\'' + el_class + '\',' + (flag ? 'false' : 'true') + ')';
		setTimeout(code, 100);
	},
	
	
	__QF_show_form: function (display, html, msg_id) {
		if (display == 'modal') {
			document.getElementById('MODAL_FORM_LAYER_CONTAINER_1218').innerHTML = html;
			SITEHELP_TEMPLATE_1218.__show_layer('modal_form');
		};
		
		if (display == 'top') {
			SITEHELP_TEMPLATE_1218.top_form_container.innerHTML = html;
			SITEHELP_TEMPLATE_1218.top_form_container_tr.style.display = '';
		};
		
		if (display == 'bottom') {
			SITEHELP_TEMPLATE_1218.bottom_form_container.innerHTML = html;
			SITEHELP_TEMPLATE_1218.bottom_form_container_tr.style.display = '';
		};
		
		if (display == 'inchat') {
			var el = SITEHELP_TEMPLATE_1218.msgs_ifr.document.getElementById('msg_' + msg_id);
			if (el) {
				el.innerHTML = html;
				el.style.display = '';
			};
		};
		
		
		try {
			SITEHELP_TEMPLATE_1218.scrol_msg_list_to_bottom();
		} catch (e) {};
	},
	
	__QF_hide_form: function (display, form_id, msg_id) {
		if (display == 'modal') {
			SITEHELP_TEMPLATE_1218.__show_layer('default');
		};
		
		if (display == 'top') {
			SITEHELP_TEMPLATE_1218.top_form_container_tr.style.display = 'none';
		};
		
		if (display == 'bottom') {
			SITEHELP_TEMPLATE_1218.bottom_form_container_tr.style.display = 'none';
		};
		
		if (display == 'inchat') {
			var el = SITEHELP_TEMPLATE_1218.msgs_ifr.document.getElementById('msg_' + msg_id);
			if (el) el.style.display = 'none';
		};
		
		try {
			SITEHELP_TEMPLATE_1218.scrol_msg_list_to_bottom();
		} catch (e) {};
	},
	
	
	
	
	
	
	//--------------------------------------------------------------------------------
	//--------------------------------------------------------------------------------
	//--------------------------------------------------------------------------------
	
	//LOCAL template functions/variables
	
	original_form_height: '',
	msgs_ifr: '',	//iframe variable holder
	msgs_container: '',	//msgs_container in iframe
	top_form_container: '',
	top_form_container_tr: '',
	bottom_form_container: '',
	bottom_form_container_tr: '',
	msgs_count: 0,
	operator_typing_container : '',
	operator_typing_msg_container: '',
	sound_enabled: true,
	chat_window_open: false,
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	local_on_chat_message: function (msg_obj, play_sound) {
		var e = SITEHELP_TEMPLATE_1218.msgs_ifr.document.createElement('div');
		e.className = 'msg_line';
		e.id = 'msg_' + msg_obj.id;
		
		if (msg_obj.type == 'msg') {
			var tm = '';
			if (msg_obj.dt.match(/ (\d\d?:\d\d):\d\d/)) {
				tm = RegExp.$1;
			};

			var line = '';

			if (msg_obj.to == 'client') {
				var op_name = '';
				if (msg_obj.show_operator_name == '1') {
					op_name = msg_obj.operator_name;
				};

				line = ' \
	<table width=100% cellpadding=0 cellspacing=0> \
	<tr> \
		<td class="msg_from_op_triangle"> \
			<div class="dv1"></div> \
		</td> \
		<td class="msg_from_op"> \
			<div class="msg_from_op"> \
			<table cellpadding=0 cellspasing=0 width=100%> \
			<tr> \
				<td class="msg_from_op_msg">$$MSG$$</td> \
				<td class="op_dt">$$DT$$</td> \
			</tr> \
			</table> \
			</div> \
		</td> \
		<td class="empty_spacer"></td> \
	</tr> \
	</table> \
				';


				line = line.replace('$$DT$$', tm).replace('$$MSG$$', msg_obj.text);
			} else {
				
				line = ' \
	<table width=100% cellpadding=0 cellspacing=0 style="margin: 0;"> \
	<tr> \
	    <td class="empty_spacer"></td> \
	    <td class="msg_from_cli" align=right> \
	        <div class="msg_from_cli"> \
	        <table cellpadding=0 cellspasing=0 width=100%> \
	     		<tr> \
	     		<td class="my_dt">$$DT$$</td> \
	     		<td class="msg_from_cli_msg">$$MSG$$</td> \
	     		</tr> \
	        </table> \
	        </div> \
	    </td> \
	    <td class="msg_from_cli_triangle"> \
	        <div class="dv4"></div> \
	    </td> \
	</tr> \
	</table> \
				';


				line = line.replace('$$DT$$', tm).replace('$$MSG$$', msg_obj.text);

			};


			e.innerHTML = line;
		};
		
		
		if (msg_obj.type == 'form') {
			e.className += ' msg_line_form';
			e.style.display = 'none';
			if (msg_obj.completed == 1) {
				// do no show anything
			} else {
				SITEHELP_1218.get_form_data(msg_obj.text, msg_obj.id);		// form_data  will be called as result
			};
		};
		
		
		SITEHELP_TEMPLATE_1218.msgs_container.appendChild(e);
		SITEHELP_TEMPLATE_1218.msgs_count++
		SITEHELP_TEMPLATE_1218.scrol_msg_list_to_bottom();
		
		
		if (SITEHELP_TEMPLATE_1218.sound_enabled && SITEHELP_TEMPLATE_1218.chat_window_open && play_sound) {
			SITEHELP_1218.play_sound('new_message');
		};
	},
	
	scrol_msg_list_to_bottom: function () {
		var last_elem = SITEHELP_TEMPLATE_1218.msgs_container.lastChild;
		
		if (SITEHELP_TEMPLATE_1218.operator_typing_container.style.display != 'none') {
			last_elem = SITEHELP_TEMPLATE_1218.operator_typing_msg_container;
		};
		
		if (last_elem) {
			var pos = SITEHELP_FUNC.find_object_position(last_elem);
			SITEHELP_TEMPLATE_1218.msgs_ifr.scrollTo(0, pos[1]);
			
			if (navigator.userAgent.match(/(iPod|iPhone|iPad)/) && navigator.userAgent.match(/WebKit/)) {
				SITEHELP_TEMPLATE_1218.msgs_container.scrollTop = pos[1];
			};
		};
	},
	
	open_in_new_window: function () {
		var w = parseInt(document.getElementById('SITEHELP_FLOAT_FORM_DIV_1218').offsetWidth);
		var h = parseInt(document.getElementById('SITEHELP_FLOAT_FORM_DIV_1218').offsetHeight);
		
		SITEHELP_TEMPLATE_1218.close_chat_window();
		SITEHELP_1218.open_in_new_window({
			'width': w,
			'height': h
		});
	},
	

	draggable_initilized: false,	

	tmpl_open_window: function () {
		
		
		
		
		
		if (typeof SITEHELP_TEMPLATE_1218.animate_window_open == 'function') {
		 SITEHELP_TEMPLATE_1218.animate_window_open();
		} else {
			
		 		SITEHELP_TEMPLATE_1218.std_window_open();
		 	
		};
		
		
		//this is required for IE
		if (navigator.appName.indexOf("Internet Explorer") != -1) {
			var parent = document.getElementById('SITEHELP_MSGS_IFR_PARENT_1218');
			document.getElementById('SITEHELP_MSGS_IFR_1218').height = parent.offsetHeight + 'px';
			
			parent = document.getElementById('SITEHELP_TEXTAREA_ROW_1218');
			document.getElementById('SITEHELP_TEXTAREA_1218').style.height = parseInt(parent.offsetHeight) + 'px';
		};
	},
	
	
	tmpl_close_window: function () {
		if (typeof SITEHELP_TEMPLATE_1218.animate_window_close == 'function') {
		 SITEHELP_TEMPLATE_1218.animate_window_close();
		} else {
		 SITEHELP_TEMPLATE_1218.std_window_close();
		};
	},
	
	
	std_window_open: function (options) {
		var form_div = document.getElementById('SITEHELP_FLOAT_FORM_DIV_1218');
		var new_style_display = '';
		
		try {
			if (typeof options == 'object') {
				var units = 'px';
				
				if (options.left) { 	
					if (options.left.match(/(px|%|em)$/)) { units = RegExp.$1; } else { units = 'px'; };
					form_div.style.left = parseInt(options.left) + units;
				};
				if (options.right) {
					if (options.right.match(/(px|%|em)$/)) { units = RegExp.$1; } else { units = 'px'; };
					form_div.style.right = parseInt(options.right) + units;
				};
				if (options.top) {
					if (options.top.match(/(px|%|em)$/)) { units = RegExp.$1; } else { units = 'px'; };
					form_div.style.top = parseInt(options.top) + units;
				};
				if (options.bottom) {
					if (options.bottom.match(/(px|%|em)$/)) { units = RegExp.$1; } else { units = 'px'; };
					form_div.style.bottom = parseInt(options.bottom) + units;
				};
				if (options.height) {
					if (options.height.match(/(px|%|em)$/)) { units = RegExp.$1; } else { units = 'px'; };
					form_div.style.height = parseInt(options.height) + units;
				};
				if (options.width) {
					if (options.width.match(/(px|%|em)$/)) { units = RegExp.$1; } else { units = 'px'; };
					form_div.style.width = parseInt(options.width) + units;
				};
				if (typeof(options.display) != 'undefined') {
					new_style_display = options.display;
				};
			};
		} catch (e) {};
		
		form_div.style.display = new_style_display;
	},
	
	std_window_close: function () {
		document.getElementById('SITEHELP_FLOAT_FORM_DIV_1218').style.display = 'none';
	},
	

	
	
	
	
	animate_window_open: function () {
		if (typeof SITEHELP_TEMPLATE_1218.get_chat_form_width_height == 'function') {
		 SITEHELP_TEMPLATE_1218.get_chat_form_width_height();
		};
		
		
		
		
		  
			
			
		
		  
		     try {
		      SITEHELP_TEMPLATE_1218.std_window_open( { bottom: -1*SITEHELP_TEMPLATE_1218.form_height + 'px' } );
		      $("#SITEHELP_FLOAT_FORM_DIV_1218").stop(true).css({ 'bottom': -1*SITEHELP_TEMPLATE_1218.form_height + 'px' }).animate({ "bottom": "0px" }, 600 );
		     } catch (e) {
		      SITEHELP_TEMPLATE_1218.std_window_open( { bottom: '0px' } );
		     };
			
		
		  

		
		
	
	},

	animate_window_close: function () {
		try {
		 
		 
		  
			
			
		
		  
	       $("#SITEHELP_FLOAT_FORM_DIV_1218").stop(true).animate({ "bottom": -1*SITEHELP_TEMPLATE_1218.form_height + "px" }, 600, function(){
	          SITEHELP_TEMPLATE_1218.std_window_close();
	          $("#SITEHELP_FLOAT_FORM_DIV_1218").css({"bottom": "0px"});  //keep it back
	       });
			
		
		  
			
		
		 
		
		 } catch (e) {
		  SITEHELP_TEMPLATE_1218.std_window_close();
		 };
	},
	
	
	

	
	
	
	form_height: 0,
	form_width: 0,
	form_width_height_set: false,
	
	get_chat_form_width_height: function () {
		if (SITEHELP_TEMPLATE_1218.form_width_height_set) return;
		
		SITEHELP_TEMPLATE_1218.form_width_height_set = true;
		
		var float_form = document.getElementById('SITEHELP_FLOAT_FORM_DIV_1218');
		
	  if (float_form.style.display == '') {
			SITEHELP_TEMPLATE_1218.form_height = float_form.offsetHeight;
			SITEHELP_TEMPLATE_1218.form_width = float_form.offsetWidth;
	  } else {
	
	   var old_left = float_form.style.left;
	   var old_right = float_form.style.right;
	
	   if (old_left) {
	     float_form.style.left = '-10000px';
	     float_form.style.display = '';
	     SITEHELP_TEMPLATE_1218.form_height = float_form.offsetHeight;
	     SITEHELP_TEMPLATE_1218.form_width = float_form.offsetWidth;
	     float_form.style.display = 'none';
	     float_form.style.left = old_left;
	   };
	
	   if (old_right) {
	     float_form.style.right = '-10000px';
	     float_form.style.display = '';
	     SITEHELP_TEMPLATE_1218.form_height = float_form.offsetHeight;
	     SITEHELP_TEMPLATE_1218.form_width = float_form.offsetWidth;
	     float_form.style.display = 'none';
	     float_form.style.right = old_right;
	   };
	
	  };
	},
	
	
	
	
	__form_el_focus: function (el, def_text) {
		if (el.value == def_text) {
			el.value = '';
			el.style.color = 'black';
		};
	},
	
	__form_el_blur: function (el, def_text) {
		if (el.value == '') {
			el.value = def_text;
			el.style.color = 'gray';
		};
	},
	
	
	textarea_prev_color: '',
	
	textarea_focus: function () {
		var t = document.getElementById('SITEHELP_TEXTAREA_1218');
		
		if (t.value == 'Напишите ваше сообщение тут ...') {
			t.value = '';
			SITEHELP_TEMPLATE_1218.textarea_prev_color = t.style.color;
			t.style.color = 'black';
		};
	},
	
	textarea_blur: function () {
		var t = document.getElementById('SITEHELP_TEXTAREA_1218');
		
		if (t.value == '') {
			t.value = 'Напишите ваше сообщение тут ...';
			t.style.color = SITEHELP_TEMPLATE_1218.textarea_prev_color;
		};
	},
	
	textarea_onkeydown: function (e) {
		if ((e.ctrlKey || e.altKey) && e.keyCode == 13) {
			document.getElementById('SITEHELP_TEXTAREA_1218').value += "\n";
			try { if (e) e.preventDefault();} catch (er) {};
			return false;
		};
		
		if (e.keyCode == 13) {	// enter (w/o ctrl)
			SITEHELP_TEMPLATE_1218.local_send_message();
			try { if (e) e.preventDefault();} catch (er) {};
			return false;
		};
		
		return true;
	},
	
	textarea_onkeypress: function () {
		SITEHELP_TEMPLATE_1218.track_keyboard_activity();
		
		if (SITEHELP_TEMPLATE_1218.partial_msg_tracking_enabled) {
			SITEHELP_TEMPLATE_1218.track_partial_msg();
		};
	},
	
	
	//	partial_msg_sender_active: false,
	partial_msg_sender_timer: '',
	last_send_partial_msg: '',
	
	track_partial_msg: function () {
		var current_text = document.getElementById('SITEHELP_TEXTAREA_1218').value;
		
		if ((current_text == '') || (current_text == 'Напишите ваше сообщение тут ...')) {
			SITEHELP_TEMPLATE_1218.stop_track_partial_msg();
		} else {
			if (SITEHELP_TEMPLATE_1218.partial_msg_sender_active) return;
			
			//start timer
			SITEHELP_TEMPLATE_1218.partial_msg_sender_active = true;
			SITEHELP_1218.last_send_partial_msg = '';
			SITEHELP_TEMPLATE_1218.partial_msg_sender_timer = setTimeout(SITEHELP_TEMPLATE_1218.partial_msg_sender_timer_fired, SITEHELP_TEMPLATE_1218.partial_msg_tracking_update_time_MSEC);
		};
		
	},
	
	stop_track_partial_msg: function () {
		if (SITEHELP_TEMPLATE_1218.partial_msg_sender_active || (SITEHELP_1218.last_send_partial_msg != '')) {
			SITEHELP_1218.notify_client_activity({'type': 'client_partial_msg', 'status': ''});
			SITEHELP_1218.last_send_partial_msg = '';
			SITEHELP_TEMPLATE_1218.partial_msg_sender_active = false;
			
			clearTimeout(SITEHELP_TEMPLATE_1218.partial_msg_sender_timer);
			SITEHELP_TEMPLATE_1218.partial_msg_sender_timer = '';
		};
	},
	
	partial_msg_sender_timer_fired: function () {
		var current_text = document.getElementById('SITEHELP_TEXTAREA_1218').value;
		
		if ((current_text == '') || (current_text == 'Напишите ваше сообщение тут ...')) {
			return SITEHELP_TEMPLATE_1218.stop_track_partial_msg();
		};
		
		if (SITEHELP_1218.last_send_partial_msg != current_text) {
			SITEHELP_1218.last_send_partial_msg = current_text;
			SITEHELP_1218.notify_client_activity({'type': 'client_partial_msg', 'status': current_text});
		};
		
		//restart timer
		SITEHELP_TEMPLATE_1218.partial_msg_sender_timer = setTimeout(SITEHELP_TEMPLATE_1218.partial_msg_sender_timer_fired, SITEHELP_TEMPLATE_1218.partial_msg_tracking_update_time_MSEC);
	},
	
	
	local_send_message: function () {
		var t = document.getElementById('SITEHELP_TEXTAREA_1218');
		
		if (t.value == '') return; //do not send empty msg
		if (t.value == 'Напишите ваше сообщение тут ...') return;	//do not send def text by clicking 'send btn'
		
		SITEHELP_1218.send_message({'text': t.value});
		t.value = '';
		try { t.focus(); } catch (e) {};
	},
	
	
	//keyboard activity tracking
	keyboard_active: false,
	keyboard_activity_timeout_timer: '',
	last_send_keyboard_status: '',
	
	track_keyboard_activity: function () {
		var current_text = document.getElementById('SITEHELP_TEXTAREA_1218').value;
		
		//obj.type == 'client_typing'			- operator keyboard activity
		//obj.status = 'composing' || 'paused' || ''				('' = clear status)
		
		if ((current_text == '') || (current_text == 'Напишите ваше сообщение тут ...')) {
			
			if (SITEHELP_TEMPLATE_1218.keyboard_active || (SITEHELP_1218.last_send_keyboard_status != '')) {
				SITEHELP_1218.notify_client_activity({'type': 'client_typing', 'status': ''});
				SITEHELP_1218.last_send_keyboard_status = '';
				SITEHELP_TEMPLATE_1218.keyboard_active = false;
				
				clearTimeout(SITEHELP_TEMPLATE_1218.keyboard_activity_timeout_timer);
				SITEHELP_TEMPLATE_1218.keyboard_activity_timeout_timer = null;
			};
			
		} else {
			
			if (SITEHELP_TEMPLATE_1218.keyboard_active) {
				//restart 'pause timeout' timer
				clearTimeout(SITEHELP_TEMPLATE_1218.keyboard_activity_timeout_timer);
				SITEHELP_TEMPLATE_1218.keyboard_activity_timeout_timer = setTimeout(SITEHELP_TEMPLATE_1218.track_keyboard_activity_timeout, 5000);
			} else {
				//start
				SITEHELP_1218.notify_client_activity({'type': 'client_typing', 'status': 'composing'});
				SITEHELP_1218.last_send_keyboard_status = 'composing';
				SITEHELP_TEMPLATE_1218.keyboard_active = true;
				SITEHELP_TEMPLATE_1218.keyboard_activity_timeout_timer = setTimeout(SITEHELP_TEMPLATE_1218.track_keyboard_activity_timeout, 5000);
			};
			
		};
	},
	
	track_keyboard_activity_timeout: function () {
		var current_text = document.getElementById('SITEHELP_TEXTAREA_1218').value;
		
		clearTimeout(SITEHELP_TEMPLATE_1218.keyboard_activity_timeout_timer);
		SITEHELP_TEMPLATE_1218.keyboard_active = false;
		
		if ((current_text == '') || (current_text == 'Напишите ваше сообщение тут ...')) {
			SITEHELP_1218.notify_client_activity({'type': 'client_typing', 'status': ''});
			SITEHELP_1218.last_send_keyboard_status = '';
		} else {
			SITEHELP_1218.notify_client_activity({'type': 'client_typing', 'status': 'paused'});
			SITEHELP_1218.last_send_keyboard_status = 'paused';
		};
	}
	
};

		SITEHELP_1218.TEMPLATE.HTML_CODE += '<style type="text/css" id="SITEHELP_CSS_1218">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#SITEHELP_FLOAT_FORM_DIV_1218, #SITEHELP_FLOAT_FORM_DIV_1218 *, ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#SITEHELP_OPINION_BOX_1218, #SITEHELP_OPINION_BOX_1218 * {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  padding: 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  margin: 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	border-spacing: 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	border-collapse: collapse;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	border: 0 none;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  font-size: 11px;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  line-height: normal !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  vertical-align: top;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	text-align: left;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	text-indent: 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	text-decoration: none;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	outline: none;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	width: auto;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	min-width: 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	max-width: none;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	height: auto;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	min-height: 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	max-height: none;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	background: none;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	box-sizing: border-box;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	text-shadow: none;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	font-family: Verdana;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	color: black;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#SITEHELP_FLOAT_FORM_DIV_1218 table tr {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	display: table-row;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#SITEHELP_FLOAT_FORM_DIV_1218 table td {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	display: table-cell;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#SITEHELP_FLOAT_FORM_DIV_1218, #SITEHELP_FLOAT_FORM_DIV_1218 * {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	background-color: #2d3233;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#SITEHELP_FLOAT_FORM_DIV_1218 img {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	display: inline;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#SITEHELP_TEXTAREA_CONTAINER_1218 {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += ' width: 100%; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += ' height: 39px; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += ' border: 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += ' padding: 3px 0 0 4px !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += ' outline: 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += ' background-color: #d7d7d7;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += ' border-radius: 4px;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#SITEHELP_TEXTAREA_CONTAINER_1218 * {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	background-color: rgba(0,0,0,0);';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#SITEHELP_TEXTAREA_1218 {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	resize: none; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	overflow: auto; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	width: 100%  !important; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	height: 34px; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	border: 0; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	outline: 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	font-size: 11px !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	box-shadow: none !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	font-weight: normal;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  background-color: rgba(0,0,0,0);';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  color: #838383;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#CHAT_FORM_TITLE_1218, #FORM_1218 .FORM_HEADER_1218 h1  {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	font-size: 15px; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	font-weight: bold; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	color:white; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	font-family: Arial;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#FORM_1218 .FORM_TITLE_1218 h3 {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	padding: 10px 0; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	color: white; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	text-align: left; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	min-height: 50px;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	font-weight: normal;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#FORM_1218 .FORM_BUTTON_CONTAINER_1218 > td {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	padding: 2px 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	text-align: center;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#FORM_1218 .FORM_BUTTON_CONTAINER_1218 button {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	white-space: nowrap;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  border-radius: 3px;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  background-color: #B6B6B6;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	border: 0 none;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  margin: 0px; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  padding: 0 4px;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  vertical-align: middle;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  cursor: pointer; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  overflow: visible; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  height: 23px !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  outline: 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  text-align: center;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  color: black;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#FORM_1218 .FORM_BUTTON_CONTAINER_1218 button.FORM_BUTTON_DISABLED_1218 {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	background: #686868;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#FORM_1218 .FORM_FIELD_TITLE_1218 > td {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	color: white;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	padding: 3px 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#FORM_1218 .FORM_FIELD_1218 > td {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	padding: 2px 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	box-sizing: border-box;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#FORM_1218 .FORM_FIELD_1218 input {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	resize: none; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	border: 1px solid #B6B6B6;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	outline: 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	width: 100%;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	font-size: 11px !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	padding-left: 4px !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	box-shadow: none !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	font-weight: normal !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	height: 23px !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	color: #838383;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	background-color: #d7d7d7;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '  border-radius: 4px;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#FORM_1218 .FORM_FIELD_1218 input.FORM_INPUT_ERROR_1218 {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	background: #F7F7F7;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#FORM_1218 .FORM_FIELD_1218 textarea {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	resize: none; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	border: 1px solid #B6B6B6;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	color: #838383;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	outline: 0;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	width: 100%;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	font-size: 11px !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	padding-left: 4px !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	background-color: #d7d7d7;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	border-radius: 4px;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	box-shadow: none !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	font-weight: normal;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	height: auto !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#FORM_1218 .FORM_FIELD_1218 textarea.FORM_INPUT_ERROR_1218 {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	background: #F7F7F7;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#SITEHELP_MSGS_IFR_PARENT_1218 {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	height: 100%;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	width: 100%;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	border-radius: 4px;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	background-color: #d7d6d6;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#SITEHELP_MSGS_IFR_1218 {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	background: none;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#SITEHELP_OP_STATUS_CIRCLE_1218 {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += ' float: left;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += ' width: 4px;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += ' height: 4px;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += ' -moz-border-radius: 3px; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += ' -webkit-border-radius: 3px; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += ' border-radius: 3px;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '.SITEHELP_OP_STATUS_CIRCLE_ONLINE_1218 {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	background-color: #4da92a !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	border: 1px solid #4da92a !important; ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '.SITEHELP_OP_STATUS_CIRCLE_OFFLINE_1218 {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	background-color: red !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	border: 1px solid red !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '.SITEHELP_OP_STATUS_CIRCLE_UNKNOWN_1218 {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	background-color: gray !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	border: 1px solid gray !important;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '#SITEHELP_HEADER_TD_1218, #SITEHELP_HEADER_TD_1218 * {';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	background-color: #25292a;';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '}';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '</style>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '<table style="width:300px; display:none; z-index:2100000010; box-shadow: 0px 0px 7px 0px rgba(0, 0, 0, 0.5);   position: fixed; right:0; bottom:0;  margin-right:5px; margin-bottom:0px;      " id="SITEHELP_FLOAT_FORM_DIV_1218" valign=top>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	<tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '		<td style="height:380px;" id="SITEHELP_SET_HEIGHT_TD_1218">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '            ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '            <table style="height:100%; width:100%;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                <tr style="height: 63px;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    <td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                       <table style="width:100%; height: 100%;" >';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                           <tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                            <td colspan=2 style="height: 18px; padding: 5px 5px 0 0;" id="SITEHELP_HEADER_TD_1218">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                              <table align=right cellpadding=0 cellspacing=0 style="width: 20px;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                               <tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                               	';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                <td style="padding-top: 1px; text-align: right;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                       						<a href="#" onclick="SITEHELP_TEMPLATE_1218.close_chat_window(); return false;" title="Скрыть чат"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAHCAYAAADEUlfTAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAGZJREFUeNpijM/MLmdgYOgA4tVAHAZlg8RmMQGJTiA+C8ShQOwCxGlQfjpIEgTSofQqIBYE4goQByYJUrkHKgFjwyXToEaCgDHUTrCkIJTzHuqg91C+EhPUHiWow1ZDaZCGVQABBgDjzBUNdznLwgAAAABJRU5ErkJggg=="/></a>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                               </tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                              </table>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                            </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                           </tr>                               ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                           <tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                               <td colspan=2 style="width:100%; padding: 5px 10px;" valign=top>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                   <table style="height:100%; width:100%;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                       <tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                          <td style="width:80px; text-align: center;" align=center valign=top>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                            <!--template must define [VAR_OPERATOR_PHOTO_MAX_LONGEST_SIDE] variable to automatically resize photo-->';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                            ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                            <img style="" src="//c.sitehelp.im/img/templates/elegant_dark/man.png" id="SITEHELP_OPERATOR_PHOTO_1218">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                          </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                          <td valign=top style="padding-left: 10px;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                             <table style="width: 100%;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                              <tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                              	<td colspan=2 id="CHAT_FORM_TITLE_1218">&#1057;&#1083;&#1091;&#1078;&#1073;&#1072;&#32;&#1087;&#1086;&#1076;&#1076;&#1077;&#1088;&#1078;&#1082;&#1080;</td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                              </tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                              ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                               <tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                                 <td style="width: 10px; padding: 2px 0 0 2px; vertical-align: middle;" valign=middle align=center><div id="SITEHELP_OP_STATUS_CIRCLE_1218" class="SITEHELP_OP_STATUS_CIRCLE_ONLINE_1218"></div></td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                                 <td valign=top align=left style="color: #4da92a; font-size: 11px;" id="SITEHELP_OP_STATUS_TEXT_1218">онлайн</td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                               </tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                               <tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                                 <td colspan=2 style="padding: 10px 0;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                                  <div style="width: 100%; box-sizing: border-box; height: 2px; border-top: 1px solid #3d3d3c; border-bottom: 1px solid #262e1f;"></div>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                                 </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                               </tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '																								';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                              </table>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                          </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                       </tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                   </table>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                               </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                           </tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                       </table>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                </tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                <tr style="height:100%;" id="LOADING_LAYER_1218">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    <td valign=top style="padding: 0 10px;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	            				<table style="width: 100%; height: 100%;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	            					<tr style="height: 100%;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	            						<td style="text-align: center; vertical-align: middle;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	            							<img src="data:image/gif;base64,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fj5CSQhOuOHrz6///vz37///AAygAKkUEAA7AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==" />';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	            						</td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	            					</tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	            				</table>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                </tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	              ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                <tr style="height:100%; display: none;" id="MODAL_FORM_LAYER_1218">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                  <td valign=top style="height: 100%; padding: 0 10px;" id="MODAL_FORM_LAYER_CONTAINER_1218">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                  </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                </tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	            	';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                <tr style="height:100%; display: none;" id="ONLINE_LAYER_1218">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    <td valign=top style="padding: 0 10px;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    	<table style="height: 100%; width: 100%;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    		<tr id="TOP_FORM_CONTAINER_TR" style="display: none;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '				            			<td style="padding-bottom:2px;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '				            				<div id="TOP_FORM_CONTAINER" style=""></div>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '				            			</td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '				            		</tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '				            		';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    		<tr style="height:100%;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    			<td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '			                    	<div id="SITEHELP_MSGS_IFR_PARENT_1218">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '			                    		<iframe name="SITEHELP_MSGS_IFR_1218" id="SITEHELP_MSGS_IFR_1218" frameborder="0" border="0" scrolling="auto" style="border:0px; padding: 0; margin: 0; overflow: auto; width: 100%; height: 100%;"></iframe>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '			                    	</div>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '			                    </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    		</tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    		';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '				            		<tr id="BOTTOM_FORM_CONTAINER_TR" style="display: none;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '				            			<td style="padding-top:2px;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '				            				<div id="BOTTOM_FORM_CONTAINER" style=""></div>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '				            			</td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '				            		</tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    	</table>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                </tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                <tr style="height: 40px; display: none;" id="SITEHELP_SEND_BTN_CONTAINER_1218">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    <td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                        <table style="height: 100%; width:100%;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                            <tr style="height: 100%;" id="SITEHELP_TEXTAREA_ROW_1218"> ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                <td valign=top style="padding: 10px 10px 0px 10px;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                	<div id="SITEHELP_TEXTAREA_CONTAINER_1218">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                	  <table cellpadding=0 cellspacing=0 style="width: 100%;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                	    <tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                	      <td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                	         <textarea id="SITEHELP_TEXTAREA_1218" onfocus="SITEHELP_TEMPLATE_1218.textarea_focus();" onblur="SITEHELP_TEMPLATE_1218.textarea_blur();" onkeydown="return SITEHELP_TEMPLATE_1218.textarea_onkeydown(event);" onkeypress="SITEHELP_TEMPLATE_1218.textarea_onkeypress();">Напишите ваше сообщение тут ...</textarea>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                	      </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                	      <td style="width: 40px; text-align: center; vertical-align: middle;" align=center valign=middle id="SITEHELP_SEND_BTN_CONTAINER_1218">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                	         <img onclick="SITEHELP_TEMPLATE_1218.local_send_message();" style="cursor: pointer; opacity: 0.2;" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB0AAAAZCAYAAADNAiUZAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAU5JREFUeNpiNDY2ZiACJAFxJBAzMlAOTrMQqXAiEPMwUAc4MxGp8AMD9cA3Yi39TUVL/zIxDAAYtXTUUrpa+o8Msy8CcRwQXyDXUmYyLG0D4sVAPIMcS0GFszQe+QYgNgfiFWji7FD6P7oGUNnLB8SWaIU5SOFfqIX1QMyKw8JSIO6Bsi8DcQSSHA+uqAFZehyItcgIvnokCyuAuBVN/gCUVsBmKTkWlgBxL5TtC8TtQPwW6qs3QNwExNeh8hHYLP0MxLwkWFiBZCEIHIGmjf9Y1CYAsTI18ukn9KoKi4WaQDwViOdjM4CFDEunAfEvIJ4L5bsB8WogfgTE36EJSAmfASxkFipzoNGyCoi3AfFuIPahRzG4EohToFkLlpjoUvbOBuJYKJubFEsptXgREN8E4jwi1TMykeJCPECNBLU8LNAC2ZpKbVpiwE2AAAMAvvM4iLznIRQAAAAASUVORK5CYII="/>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                	      </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                	    </tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                	  </table>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                	</div>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                                </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                            </tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                        </table>      ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                </tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                <tr style="height: 24px; ">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                   <td style="vertical-align: middle; padding: 0 10px 0 10px;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                   ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '										<table style="width: 100%;">';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    	<tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                        <td style="text-align: left; padding-top: 2px;" valign=top>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                         ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                        </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '									      ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '												';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '												';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '												';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '												';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '												';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '									';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '											</tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    </table>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                    ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                   </td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '                </tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '            </table>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '            ';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '		</td>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '	</tr>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";SITEHELP_1218.TEMPLATE.HTML_CODE += '</table>';
SITEHELP_1218.TEMPLATE.HTML_CODE += "\n";
		
		
		
		SITEHELP_1218.init();
	