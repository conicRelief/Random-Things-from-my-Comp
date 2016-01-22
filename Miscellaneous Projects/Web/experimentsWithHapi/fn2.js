Hapi = require('hapi');

server = new Hapi.Server();

function run_cmd(cmd, args, callBack ) {
    var spawn = require('child_process').spawn;
    var child = spawn(cmd, args);
    var resp = "";

    child.stdout.on('data', function (buffer) { resp += buffer.toString() });
    child.stdout.on('end', function() { callBack (resp) });
}


server.connection({
	host:'localhost',
	port: 8080});

server.route({
	method: 'GET',
	path: '/specs',
	handler: function (request, reply)
	{
		var returnObject = { 
			ram : {
				total:"",
				used:"",
				free:""
				},
				files : [] 
			};		

		run_cmd( "vm_stat", [""],function(text)
		{
			reply(text);
		});
	
	}
});

server.route({
	method: 'GET',
	path: '/ls',
	handler: function (request, reply)
	{

				var viewData = { 
				    directories : [],
				    files : [] 
				};		
		run_cmd( "find", [".","-type","d","-depth","1"],function(text)
		{
			var tokenized = text.split("\n");
			for (var i = 0; i < tokenized.length; i++) 
			{
				viewData.directories.push(tokenized[i].replace("./",""));
			}		
			run_cmd( "find", [".","-type","f","-depth","1"],function(text2){

				var tokenized = text2.split("\n");

				for (var i = 0; i < tokenized.length; i++) {
				viewData.files.push(tokenized[i].	replace("./",""));
				}
				reply(
					JSON.stringify(viewData));
			});

		});
	}
});

server.route({
	method: 'POST',
	path: '/command',
	handler: function (request, reply)
	{

			command = request.payload.command;
			// parameters = request.payload.parameters;
			// console.log(parameters);
			console.log(request.payload);
			params = request.payload.params.split(" ");
		    console.log(params);

		run_cmd( command, params,function(text)
				{

			console.log(text);

				reply(text);
			});
	}
});




server.start(() => 
{
	console.log('Server running at:', server.info.uri);
})