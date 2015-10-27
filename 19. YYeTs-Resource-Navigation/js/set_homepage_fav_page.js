/*  
    这个文件存放2个函数.
    分别是 "设为首页" 和 "收藏本页"
    火狐和IE下有效.
    Chrome 无效
*/



//url：要收藏的链接；title：收藏项的名称 
function AddFavorite(url,title) 
{ 
    //如果url或者title为空，默认为当前页面url和title。 
    if(!(url&&title)) 
    { 
        url=document.URL; 
        title=document.title;  
    } 

    if (document.all)//IE 
    { 
        window.external.addFavorite(url,title); 
    } 
    else if (window.sidebar)//火狐 
    { 
        window.sidebar.addPanel(title, url, ""); 
    } 
} 

//url：要设置为首页的链接 
function SetHomepage(url) 
{ 
    //如果url为空，默认为当前页面url。 
    if(!url) 
    { 
        url=document.URL; 
    } 

    if (document.all)//IE  
    { 
        document.body.style.behavior = 'url(#default#homepage)'; 
        document.body.setHomePage(url); 
    } 
    else if (window.sidebar)//火狐 
    { 
        if (window.netscape) { 
            try 
            { 
                window.netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect"); 
            } 
            catch (e) 
            { 
                alert("此操作被浏览器拒绝！请在浏览器地址栏输入“about:config”并回车然后将[signed.applets.codebase_principal_support]的值设置为'true',双击即可。"); 
            } 
        } 
        var prefs = Components.classes['@mozilla.org/preferences-service;1'].getService(Components.interfaces.nsIPrefBranch); 
        prefs.setCharPref('browser.startup.homepage', url); 
    } 
}  