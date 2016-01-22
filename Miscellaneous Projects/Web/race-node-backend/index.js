var server = require("./server");
var router = require("./router");
var requestHandlers = require("./requestHandlers");

var handle = {};
handle["/"] = requestHandlers.start;
handle["/start"] = requestHandlers.start;

handle["/tracks"] = requestHandlers.all_tracks;
handle["/upload"] = requestHandlers.upload;



server.start(router.route,handle);

