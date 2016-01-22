var exec = require("child_process").exec;

function all_tracks(response)
{
	console.log("Request handler 'start' was called.");
	var content = "empty";

	exec("cat ./data/race_tracks.json", function (error,stdout,stderr)
	{
		content = stdout;
		response.writeHead(200,{"Content-Type":"text/plain"});
		response.write(content);
		response.end();
	});

	return content;

}
function start(response)
{
	console.log("Request handler 'start' was called.");
	var content = "empty";

	exec("cat ./data/race_tracks.json", function (error,stdout,stderr)
	{
		content = stdout;
		response.writeHead(200,{"Content-Type":"text/plain"});
		response.write(content);
		response.end();
	});

	return content;
}

function upload(response)
{
console.log("Request handler 'upload' was called");

response.writeHead(200, {"Content-Type": "text/plain"});
response.write("Hello World");
response.end();

}

exports.start = start;
exports.upload = upload;
exports.all_tracks = all_tracks;

