// not used anymore bc ned https for integration with portfolio website

var express = require("express");
var server = express();
var fs = require("fs");
var port = 80;
server.use(express.static("public"));
console.log("listening at port " + port);
server.listen(port);

server.get("/100days", function(req, res) {
    res.sendFile("index.html", {
        root: path.join(__dirname, "../public/100days"),
    });
    // var fileToSend = "index.html";
    // res.sendfile(fileToSend, {
    //   root: '.'
    // });
});