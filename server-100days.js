var express = require('express');
var server = express();
var fs = require("fs");
var https = require('https');
var port = 443;
var path = require('path');

var credentials = {
    key: fs.readFileSync('/etc/letsencrypt/live/tg1799.itp.io/privkey.pem'),
    cert: fs.readFileSync('/etc/letsencrypt/live/tg1799.itp.io/fullchain.pem')
};

server.use(express.static('public'));
console.log("listening at port " + port);

const httpsServer = https.createServer(credentials, server);
httpsServer.listen(443, () => {
    console.log('HTTPS Server running on port 443');
});

server.get('/100days', function(req, res) {
    res.sendFile('index.html', {
        root: path.join(__dirname, '../public/100days')
    });
});
