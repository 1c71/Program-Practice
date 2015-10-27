// ==UserScript==
// @name         Download WSJ Video & Subtitle
// @namespace    http://your.homepage/
// @version      0.2
// @description  Download wall street journal video and subtitle 
// @author       Github 1c7
// @match        http://www.wsj.com/video/*
// @grant        none
// ==/UserScript==



//--------------------------------------------------------------------------
// 工具函数
//--------------------------------------------------------------------------

// 插入新元素到某元素的后面
function insertAfter(newNode, referenceNode) {
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}


// 把字符串下载为文件
// 下面这个函数不是我写的。搜了下找到这个解决方案就直接复制过来用了。
// 复制自： http://www.alloyteam.com/2014/01/use-js-file-download/
function downloadFile(fileName, content){
    var aLink = document.createElement('a');
    var blob = new Blob([content]);
    var evt = document.createEvent("HTMLEvents");
    evt.initEvent("click", false, false);
    aLink.download = fileName;
    aLink.href = URL.createObjectURL(blob);
    aLink.dispatchEvent(evt);
}

// 处理时间轴的函数
function process_time(s){
    
    s = parseFloat(s).toFixed(3);
    // 超棒的函数, 可以把不论是整数还是小数它都给你弄成3位小数形式的数字.
    // 举个柚子: 
    // 671.33 -> 671.330
    // 671 -> 671.000
    // 注意, 这个函数会四舍五入. 具体可以去读文档
    
    
    var array = s.split('.');
    // 把开始时间根据句号分割
    // 671.330 会分割成数组: [671, 330]
    
    
    var Hour = 0;
    var Minute = 0;
    var Second = array[0];   // 671
    var MilliSecond = array[1];  // 330
    // 先声明一下变量, 待会把这几个拼好就行了。
    
    
    
    // 我们来处理秒数.  把"分钟"和"小时"除出来。
    if(Second >= 60){
        
        Minute = Math.floor(Second / 60);
        Second = Second - Minute * 60;
        // 我们把 秒 拆成 分钟和秒, 比如121秒, 拆成2分钟1秒    
        
        Hour = Math.floor(Minute / 60);
        Minute = Minute - Hour * 60;
        // 我们把 分钟 拆成 小时和分钟, 比如700分钟, 拆成11小时40分钟    
        
    } 
    
    
    // 处理分钟，如果位数不够两位就变成两位，下面两个if语句的作用也是一样。
    if (Minute < 10){
        Minute = '0' + Minute;
    }       
    
    // 处理小时
    if (Hour < 10){
        Hour = '0' + Hour;
    }
    
    // 处理秒
    if (Second < 10){
        Second = '0' + Second;
    }
    
    return Hour + ':' + Minute + ':' + Second + ',' + MilliSecond;
}

// 拿到视频的链接
// <meta name="twitter:player:stream" content="https://video-api-secure.wsj.com/api-video/redir_video_asset.asp?guid=174A5AB7-075A-4759-937A-3B76848ED801&type=video&format=v2_ec664k.mp4&site=twittercard" />
function getVideoContent() { 
   var metas = document.getElementsByTagName('meta'); 
   for (i=0; i<metas.length; i++) { 
      if (metas[i].getAttribute("name") == "twitter:player:stream") { 
         return metas[i].getAttribute("content"); 
      } 
   } 
   return "";
} 


// 拿到视频的标题
// <meta property="og:title" content="ISIS Captives Get Publicly Shamed on Iraqi Reality Show" />
function getVideoTitle() { 
   var metas = document.getElementsByTagName('meta'); 
   for (i=0; i<metas.length; i++) { 
      if (metas[i].getAttribute("property") == "og:title") { 
         return metas[i].getAttribute("content"); 
      } 
   } 
   return "";
} 


//--------------------------------------------------------------------------
// 代码开始
//--------------------------------------------------------------------------

var header = document.getElementsByTagName("header")[0];




// -------------------------------------------
// 字幕下载
// -------------------------------------------

// <br>
var newbr = document.createElement("br");

// <textarea>
var new_textarea  = document.createElement("textarea");    
new_textarea.setAttribute('id', 'wsj987');  // 设个不太容易重复的id

// <button>
var new_button = document.createElement("button"); 
new_button.innerHTML = '下载字幕';

new_button.onclick = function(){
    
    // 拿到 textarea 的值
    var ta = document.getElementById("wsj987");
    var ta_v = ta.value;
    
    // xml -> srt
    var xxx = new DOMParser().parseFromString(ta_v, "text/xml").getElementsByTagName('Item');
    var srtString = ""; // 把srt字幕都放这个变量里，到时候下载下来
    for (var i = 0, il = xxx.length; i < il; i++) {
        /*

            srt 的字幕格式都是类似这样的:

				1
				00:00:00,060 --> 00:00:01,240
				Hi, I'm John Green.

				2
				00:00:01,240 --> 00:00:03,060
				Welcome to Crash Course Big History

				3
				00:00:03,060 --> 00:00:04,390
				where today we're going to talk

			
			序号一行, 时间轴一行, 字幕一行或多行
			
			我们现在要转成这种格式

            */       
        
        // 	构造出序号
        var index = i+1;
        var from = xxx[i].getAttribute('from');
        var duration = xxx[i].getAttribute('duration');
        var text = xxx[i].childNodes[0].nodeValue;
        
        
        
        // 插入序号
        srtString = srtString + index;
        srtString = srtString + "\n";
        
        // 插入时间轴
        srtString = srtString + process_time(from);
        srtString = srtString + ' --> ';
        srtString = srtString + process_time(parseFloat(from)+parseFloat(duration));
        srtString = srtString + "\n";
        
        // 插入字幕
        srtString = srtString + text.toString().replace("\n", ' ');
        srtString = srtString + "\n \n";
    }
    
    
    // 下载文件
    //console.log(srtString);
    srt_filename = getVideoTitle() + ".srt";
    downloadFile(srt_filename, srtString);
};
  
insertAfter(new_button, header);
insertAfter(new_textarea, header);
insertAfter(newbr, header);




// -------------------------------------------
// 视频下载
// -------------------------------------------


// 往页面上添加元素
if(getVideoContent()!=""){
    var new_a = document.createElement("a");      
    var textnode = document.createTextNode("点击此链接下载视频: " + getVideoContent() + "")
    new_a.setAttribute('href', getVideoContent());
    new_a.setAttribute('target', "_blank");
    new_a.setAttribute('download', getVideoTitle()+".mp4");
    new_a.setAttribute('style', "font-size:12px; color: white;");
    new_a.appendChild(textnode); 
    insertAfter(new_a, header);
}
else{
	var new_a = document.createElement("a");   
    var textnode = document.createTextNode("拿不到视频地址，抱歉"); 
    new_a.setAttribute('target', "_blank");
    new_a.setAttribute('style', "font-size:12px; color: white; align:center; ");
    new_a.appendChild(textnode); 
    insertAfter(new_a, header);
}