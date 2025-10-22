`brew install wireshark wireshark-app`

Show how to export packet bytes

Show how to copy value

Check bottom left on wireshark for filter when hovering over a value, e.g. tcp.sourceport

* Open wireshark, show traffic graphs
  * Talk about en0, loopback
* Run `ping 127.0.0.1` and show traffic on loopback interface

Demo
* Show machine IP address via `System Settings > Network`, confirm same in Wireshark
* View unencrypted packets going to localhost/loopback
* View unencrypted packets going to http website
* View encrypted packets going to https website
  * Decrypt using SSLKEYLOGFILE

## View HTTP traffic on the loopback interface
1. Run `python3 -m http.server 8000`
2. Navigate to `127.0.0.1:8000/index.html`
3. Open Wireshark, click on loopback interface, filter for `http`, refresh browser page, observe unencrypted data
4. Can also try with other files in this directory, e.g. `tut.md`
5. Run an HTTP server that has some basic authorization with `python3 auth_http_server.py --bind 127.0.0.1 --port 8000 --user shane --pass a_secure_password`
6. Show that you can see credentials in Wireshark by looking at authorization header

# View HTTP traffic on your WiFi network interface
1. Open wireshark, click `WiFi: en0` (assuming you're on WiFi)
2. Visit http://neverssl.com
3. Filter for `http` traffic on Wireshark, view request and response in plaintext

## View HTTPs traffic on the loopback interface
1. Open loopback interface on wireshark
2. Run `python3 https_server.py --bind 127.0.0.1 --port 8443` to start HTTPS server
3. Run `SSLKEYLOGFILE=/tmp/sslkeys.log /Applications/Firefox.app/Contents/MacOS/firefox &` to start Firefox and save SSL keys
7. Filter for `tls` traffic on Wireshark, observe that you can't view plaintext responses
4. Load e.g. `https://127.0.0.1:8443/index.html` and show students that content in Wireshark is encrypted
5. Give Wireshark path to SSLKEYLOGFILE via `Wireshark > Preferences > Protocols > TLS > (Pre)-Master-Secret log filename = /tmp/sslkeys.log`
6. Now show students that you can read the unencrypted content of index.html, etc.

## Too complicated, don't do
# View HTTPs traffic on your WiFi network interface
1. Open wireshark, click `WiFi: en0` (assuming you're on WiFi)
2. Visit https://www.paulgraham.com/field.html
3. Filter for `tls` traffic on Wireshark, observe that you can't view plaintext responses
4. Now run browser with `SSLKEYLOGFILE=/tmp/sslkeys.log /Applications/Firefox.app/Contents/MacOS/firefox &`
5. Give Wireshark path to SSLKEYLOGFILE via `Wireshark > Preferences > Protocols > TLS > (Pre)-Master-Secret log filename = /tmp/sslkeys.log`
6. Reload https://www.paulgraham.com/field.html and dig around for response. Might need to filter for http2
   1. Try this filter: `(http2) && (_ws.col.info == "HEADERS[7]: 200 OK, DATA[7], DATA[7] (text/html)")`
