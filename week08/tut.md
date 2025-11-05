# Week 8 Tutorial

## Detection
* Splunk (log database)
  * Useful for analyzing very large datasets of logs (more powerful than a simple `grep`)
  * Very often network logs (e.g. from an Apache/nginx web server), but also lots of other types of logs possible
  * Has its own language for searching/querying datasets, called Search Processing Language (SPL) see https://www.splunk.com/en_us/blog/learn/splunk-cheat-sheet-query-spl-regex-commands.html for a cheatsheet
    * In practice, Google for things as you need them, e.g. "filter for this IP address and NOT this http status code"
  * A type of SIEM (Security Information and Event Management) system
* Process Monitor (similar to `top`, `htop`, `strace`, `ps` on Linux, but for Windows)
  * Provides info on all running processes in the system (e.g. operations being performed, files being accessed)
  * Useful for analyzing (running) malware (ideally in an isolated VM)
  * What files is this program reading/writing?
  * What registry keys is this program reading/writing?
* Wireshark
  * Also useful for analyzing (running) malware
  * Who is this program trying to contact? (look at the DNS hostname)

### Using Splunk
* Make sure to go through https://featherbear.cc/UNSW-COMP6845-splunk/#all
* Install Splunk with Docker by following [this guide](https://featherbear.cc/UNSW-COMP6845-splunk/#all)
  * You'll need to install Docker first if you don't already have it installed
  * Think of Docker like a lightweight, headless VM. Extremely common tool out in industry
* After installing Docker, pull the Splunk Docker image
  * If on an Apple Silicon Mac you'll need to explicilty override the platform via `docker pull --platform linux/amd64 splunk/splunk:latest`
* Once you've pulled the image, you can run it with `docker run -it -e SPLUNK_GENERAL_TERMS=--accept-sgt-current-at-splunk-com -e SPLUNK_START_ARGS=--accept-license -e SPLUNK_PASSWORD=helloworld -p 8000:8000 -p 8089:8089 splunk/splunk start`, then navigate to `http://localhost:8000` and login with `admin` and `helloworld`
* Download sample log file from https://drive.google.com/uc?export=download&id=1Beso6HHk63uDz2S8f8VZnukhma1PZxTB
* Then ingest into Splunk with `Settings > Add Data > Upload > Source Type: access_combined (which is a format for web server logs) > Submit`
  * For other types of logs (e.g. execution logs, JSON, CSV, etc.) find and select the appropriate source type
* Default search query will be something like `source="access.log" host="f88a73fc0d4b" sourcetype="access_combined_wcookie"`
* Take a look at the "Interesting Fields"
  * Note that sometimes Splunk doesn't notice all of the different fields. In these cases, select "Extract New Fields" and tell Splunk how to detect the fields (e.g. how are they delimited? Either simple character or regex)
* Search for all requests from client with IP addr `91.99.30.32`: add `clientip="91.99.30.32"` to the search query
* Search for all responses from server that were not 200 OK: `source="access.log" host="f88a73fc0d4b" sourcetype="access_combined_wcookie" status!=200`
* Search for all unsuccessful responses from server (400+): `source="access.log" host="f88a73fc0d4b" sourcetype="access_combined_wcookie" status>=400`
* It is often useful to click on one of the interesting fields and find the 'Rare Values' (e.g. uri_path)

### Using Process Monitor
* Back to Windows VM, yay
* Download and install Process Monitor https://learn.microsoft.com/en-us/sysinternals/downloads/procmon on your Windows VM
* Capture will start immediately when you open the app
* Stop capture, clear capture, start capture, open notepad, stop capture, ctrl+f for Notepade.exe, right click, include
  * Filter for `WriteFile` operations to see text written to document
  * Try recapturing with filter on and writing more text
* Run SpyPlane.exe and look at the operations in Process Monitor
* Note that Wireshark may also be useful for these challenges