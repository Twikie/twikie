$(document).ready(function(){
    var settings = {
		source_element: '#source',
		annotation_xoff: -25,
		annotation_yoff: 10,
		add_control: '.add.control',
		toggle_control: '.toggle.control',
	};
	var save_annotations_to = new Object();
	var saved_annotations = {% autoescape off %} {{annotations}}; {% endautoescape %}

	annotate_js(settings, save_annotations_to, saved_annotations);
	
	$('.save.control').click(function(){
	    var json = JSON.stringify(save_annotations_to.json);
	    console.log(json);
	    $.post('annotations/new/', {annotations: json, revision:'{{revision.pk}}'}, function(data){
	        console.log(data);
	    });
	});
	
});

$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});
