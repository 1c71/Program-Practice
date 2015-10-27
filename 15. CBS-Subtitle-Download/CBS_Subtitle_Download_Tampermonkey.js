// ==UserScript==
// @name         CBS NEWS Subtitle Download
// @namespace    http://your.homepage/
// @version      1.0
// @description  lalalala
// @author       github 1c7
// @match        http://www.cbs.com/shows/cbs_evening_news/video/*
// @require      http://code.jquery.com/jquery-latest.js
// ==/UserScript==




// add element into page
var ta = document.createElement("textarea");     
ta.setAttribute('id', "textarea_CBS_1c7");        
ta.style.cssText = "height: 50px; width: 700px; margin:8px;";
var container = document.getElementById("cbs-show-content");
container.insertBefore(ta, container.firstChild);



// store srt content
var srt = '';



//if textarea content change.
$(document).on('change', '#textarea_CBS_1c7', function() {
    var content = $(this).val();
    if (content === '' || content === ' '){return;}
    
   	// string -> html, but actually, we are processing xml format.
	xml = $.parseHTML( content );
    

        $(xml).find("p").each(function(index){
            var index = index + 1;
            var begin = $(this).attr('begin');
            var end = $(this).attr('end');
            var text = $(this).text();
            
            if(index == 1){
                begin = "00:00:00,000";
            }else{
                begin = three_digit(begin);
            }
            
            end = three_digit(end);
            text = text.toLowerCase();
            
            srt = srt + index;
            srt = srt + '\n';
            srt = srt + begin;
            srt = srt + ' --> ';
            srt = srt + end;
            srt = srt + text;
            srt = srt + '\n';
            srt = srt + '\n';  
            
        });    
        downloadFile("result.srt",srt);

    
});



// 下载到文件
function downloadFile(fileName, content){
    var aLink = document.createElement('a');
    var blob = new Blob([content]);
    var evt = document.createEvent("HTMLEvents");
    evt.initEvent("click", false, false);
    aLink.download = fileName;
    aLink.href = URL.createObjectURL(blob);
    aLink.dispatchEvent(evt);
}


// process SRT time

//     input: 0:20:10.3
//     output: 0:20:10,300

//     input: 0:20:10.39999999999
//     output: 0:20:10,400
function three_digit(timeNumber){
    var list = timeNumber.split('.');
	var s = '0.' + list[1];
    s = parseFloat(s).toFixed(3);
    var l = s.split('.');
    list[1] = l[1];
    return list.join(',');
}