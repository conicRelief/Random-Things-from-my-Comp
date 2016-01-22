var colors = require('colors');

function green(msg) {
    console.log(msg.green);
}
function orange(msg){
	console.log(msg.yellow);
}

function seperator()
	{

	process.stdout.write("\n \n");
	for (i = 0; i < 40; i++) {
    	process.stdout.write("-".red + "=".green);
	}
  process.stdout.write("\n");



}

function race()
{console.log(x);}
exports.seperator = seperator;
exports.green = green;
exports.orange = orange;
