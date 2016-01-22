// server.js

var http = require("http");
var url = require("url");
var print = require("./big_blocky_messages");
function start(route,handle)
{


	function onRequest(request, response)
	{
		var pathname = url.parse(request.url).pathname;
		print.seperator();
		print.orange("Request for " + pathname+ " recieved");
		route(handle,pathname,response)

		}
	http.createServer(onRequest).listen(8888);
	print.green("Server has started. Prepare yourself");
}

exports.start = start;

