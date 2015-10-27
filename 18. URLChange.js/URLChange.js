/*  
	@ URLChange.js 
	@ Github:  https://github.com/1c7/URLChange.js
	@ Version: 1.0
	@ Author:  Cheng Zheng
	@ license  MIT
*/


function addORchangeURLParameter(paramName, paramValue, URL){

	var url_list = URL.split('?');


	var GET = getParameterFromURL(paramName, URL);
	if(GET){
		return changeURLParameter(paramName, paramValue, URL);
	}else{
		return addURLParameter(paramName, paramValue, URL);
    }

}
/*  
	//__________________________
	//
	//	Some example:
	//___________________________


	if parameter not exist, add it. 
	example:
		addORchangeURLParameter('name', 'obama', 'http://localhost/newteamwork/')
		http://localhost/newteamwork/?name=obama


	if parameter exist, change it.
	example:
		addORchangeURLParameter('name', 'obama', 'http://localhost/newteamwork/?name=handsomejack')
		http://localhost/newteamwork/?name=obama

		addORchangeURLParameter('name', 'obama', 'http://localhost/newteamwork/?name=handsomejack&age=19')
		http://localhost/newteamwork/?name=obama&age=19
	
		addORchangeURLParameter('name', 'obama', 'http://localhost/newteamwork/?Category=2,4,6,1')
		http://localhost/newteamwork/?Category=2,4,6,1&name=obama



*/





function addURLParameter(paramName, paramValue, URL){

	var url_list = URL.split('?');
	var haveParameter = false;

    // if there no parameter, return false;
    if(url_list[1]){
    	haveParameter = true;
    }

    if(haveParameter){
    	var parameter_list = url_list[1].split('&');
    	parameter_list.push(paramName + '=' + paramValue);
	    return url_list[0] + '?' + parameter_list.join('&');
    }else{
    	return url_list[0] + '?' + paramName + '=' + paramValue;
    }

}

/*  
	//__________________________
	//
	//		Some example:
	//___________________________


	addURLParameter('name', 'obama', 'http://localhost/newteamwork/')
	http://localhost/newteamwork/?name=obama


	addURLParameter('City', 'London', 'http://localhost/newteamwork/')
	http://localhost/newteamwork/?City=London


	addURLParameter('City', 'London', 'http://localhost/newteamwork/?BarName=haha')
	http://localhost/newteamwork/?BarName=haha&City=London


	addURLParameter('City', 'London', 'http://localhost/newteamwork/?BarName=haha&you=beatuiful')
	http://localhost/newteamwork/?BarName=haha&you=beatuiful&City=London


	addURLParameter('City', 'London', 'http://localhost/newteamwork/?City=London&you=beatuiful')
	http://localhost/newteamwork/?City=London&you=beatuiful&City=London

*/







function changeURLParameter(paramName, paramValue, URL){
	var url_list = URL.split('?');

    // if there no parameter, return false;
    if(!url_list[1]){
    	return false;
    }

    var that_parameter_name_exist = false;

    var parameter_list = url_list[1].split('&');
    for (var i = 0; i < parameter_list.length; i++) 
    {
        var one_parameter = parameter_list[i].split('=');
        if (one_parameter[0] == paramName) 
        {
        	that_parameter_name_exist = true;
            one_parameter[1] = paramValue;
            parameter_list[i] = one_parameter.join('=')
            var newURL = url_list[0] + '?' + parameter_list.join('&');
            return newURL;
        }
    }
    if(that_parameter_name_exist == false){
    	return false;
    }
}

/*  
	//__________________________
	//
	//		Some example:
	//___________________________


	if there are no parameter:
		changeURLParameter('a', 'b', 'http://localhost/newteamwork/')
		false
	

	if parameter not exist:
		changeURLParameter('lalala', 'Amsterdam', 'http://localhost/newteamwork/?City=London&Category=1')
		false

		changeURLParameter('dasdafeaf', 'auahusauh', 'http://localhost/newteamwork/?City=London')
		false


	changeURLParameter('City', 'Amsterdam', 'http://localhost/newteamwork/?City=London')
	http://localhost/newteamwork/?City=Amsterdam


	changeURLParameter('City', 'Amsterdam', 'http://localhost/newteamwork/?City=London&Category=1')
	http://localhost/newteamwork/?City=Amsterdam&Category=1

	changeURLParameter('Category', '1,3,4', 'http://localhost/newteamwork/?City=London&Category=1')
	http://localhost/newteamwork/?City=London&Category=1,3,4

*/







function getParameterFromURL(parameter_name, URL)
{
    var url_list = URL.split('?');

    // if there no parameter, return false;
    if(!url_list[1]){
    	return false;
    }

    var that_parameter_name_exist = false;

    var parameter_list = url_list[1].split('&');
    for (var i = 0; i < parameter_list.length; i++) 
    {
        var one_parameter = parameter_list[i].split('=');
        if (one_parameter[0] == parameter_name) 
        {
            return one_parameter[1];
            that_parameter_name_exist = true;
        }
    }

    if(that_parameter_name_exist == false){
    	return false;
    }
}        
/*  
	//__________________________
	//
	//		Some example:
	//___________________________

	getParameterFromURL('aa', 'http://localhost/newteamwork/?aa=bb');
	bb

	getParameterFromURL('haha', 'http://localhost/newteamwork/?aa=bb&haha=lol');
	lol

	if there are no parameter:
		getParameterFromURL('aa', 'http://localhost/newteamwork/');
		false

	if parameter not exist:
		getParameterFromURL('jj', 'http://localhost/newteamwork/?aa=bb');
		false

*/




function removeParameterFromURL(parameter_name, URL) {
    var url_list = URL.split('?');

    // if there no parameter, return false;
    if(!url_list[1]){
    	return false;
    }

    var parameter_list = url_list[1].split('&');
    // ["aa=bb", "cc=dd"]

    for (var i = 0; i < parameter_list.length; i++) 
    {
        var one_parameter = parameter_list[i].split('=');
        // ['aa', 'bb']
        if (one_parameter[0] == parameter_name) 
        {
        	var index = parameter_list.indexOf(parameter_list[i]);
        	if (index > -1) {
			    parameter_list.splice(index, 1);
			}
        }
    }

    if(parameter_list.length == 0){
    	return url_list[0];
    }else{
    	return url_list[0] + '?' + parameter_list.join('&');
    }


}

/* 
	//__________________________
	//
	//		Some example:
	//___________________________

		removeParameterFromURL('aa', 'http://localhost/newteamwork/');
		false	

		removeParameterFromURL('aa', 'http://localhost/newteamwork/?aa=bb');
		http://localhost/newteamwork/

		removeParameterFromURL('aa', 'http://localhost/newteamwork/?aa=bb&cc=dd&ee=ff');
		http://localhost/newteamwork/?cc=dd&ee=ff

		removeParameterFromURL('cc', 'http://localhost/newteamwork/?aa=bb&cc=dd&ee=ff');
		http://localhost/newteamwork/?aa=bb&ee=ff

		removeParameterFromURL('ee', 'http://localhost/newteamwork/?aa=bb&cc=dd&ee=ff');
		http://localhost/newteamwork/?aa=bb&cc=dd

		removeParameterFromURL('asdasdasdasd', 'http://localhost/newteamwork/?aa=bb&cc=dd&ee=ff');
		http://localhost/newteamwork/?aa=bb&cc=dd&ee=ff


*/




function clearParameterFromURL(URL) {
    var url_list = URL.split('?');

    // if there no parameter, return URL;
    if(!url_list[1]){
    	return URL;
    }

    return url_list[0];
}
/* 
	//__________________________
	//
	//		Some example:
	//___________________________

		clearParameterFromURL('http://localhost/newteamwork/');
		http://localhost/newteamwork/

		clearParameterFromURL(http://localhost/newteamwork/?aa=bb&cc=dd&ee=ff');
		http://localhost/newteamwork/

*/


function thereAreParameterInURL(URL){
    var url_list = URL.split('?');

    // if there no parameter, return false;
    if(!url_list[1]){
    	return false;
    }

    return true;
}
/* 
	//__________________________
	//
	//		Some example:
	//___________________________

		thereAreParameterInURL('http://localhost/newteamwork/');
		false

		thereAreParameterInURL('http://localhost/newteamwork/?aa=bb');
		true

		thereAreParameterInURL('http://localhost/newteamwork/?aa=bb&cc=dd&ee=ff');
		true

*/
