function Popup() {
	
	var open = false;
	var ignoreClick = false;
	var confirmCancel = false;
	
	var popupDiv = $("#popup");
	var overlayDiv = $("#popup_overlay");
	
	var closeCallback = null;
	var self = this;
	
	self.open = function(instant) {
		ignoreClick = true;
		if(!open) {
			open = true;
			if(instant) {
				popupDiv.show();
				overlayDiv.show();
			} else {
				popupDiv.fadeIn(250);
				overlayDiv.fadeIn(500, function() { ignoreClick = false });
			}
			self.center();
		}
	}
	
	$( window ).resize(function() {
		if(open) self.center();
	});
	
	$(document).click(function(event) {
		if(open && !ignoreClick) {
			if(!($(event.target).attr('id') == "popup" || $(event.target).parents('div#popup').length > 0)) {
				if(confirmCancel) {
					if(confirm(confirmCancel)) {
						self.close();
					}
				} else {
					self.close();
				}
			}
		}
		ignoreClick = false;
	});
	
	self.close = function() {
		open = false;
		popupDiv.fadeOut(250);
		overlayDiv.fadeOut(500);
		if (typeof closeCallback == 'function') { 
			closeCallback();
		}
	}
	
	self.center = function() {
		var height = popupDiv.height();
		var width = popupDiv.width();
		popupDiv.css('margin-top','-'+((height/2)+6)+'px');
		popupDiv.css('margin-left','-'+((width/2)+11)+'px');
	}
	
	self.setHeader = function(html) {
		$("#popup_header").html(html);
		$("#popup_header").show();
		self.center();
	}
	
	self.setContents = function(html) {
		$("#popup_content").html(html);
		$("#popup_content").show();
		setTimeout(function() {
			$("#popup_loading").hide();
		},15);
		self.center();
	}
	
	self.addContents = function(html) {
		setTimeout(function() {
			$("#popup_loading").hide();
		},15);
		$("#popup_content").append(html);
		$("#popup_content").show();
		self.center();
	}
	
	self.setFooter = function(html) {
		$("#popup_footer").html(html);
		$("#popup").css( { paddingBottom : $("#popup_footer").outerHeight() + "px" } );
		$("#popup_footer").show();
		self.center();
	}
	
	self.loading = function(text) {
		if(!text) text = "Loading...";
		$("#popup_loading_message").html(text);
		$("#popup_loading").show();
		self.open();
	}
	
	self.loadURL = function(url, text) {
		alert(url);
		self.loading(text);
		var page = new Ajax(url);
		page.setCallback(self.addContents);
		page.start();
	}
	
	self.reset = function()
	{
		$("#popup_header").html("");
		$("#popup_content").html("");
		$("#popup_footer").html("");
	}

	self.onClose = function(c) {
		closeCallback = c;
	}
	
	self.closeConfirmText = function(t) {
		confirmCancel = t;
	}
}