# Windows Forensics

## Registry Editor

Windows Registry: A database that stores configuration settings and user activity for the operating system and installed applications.

Demo:

- Open regedit
- Navigate to these locations and note what you see:
- HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation
  - What timezone is the system set to?
- HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
  - What programs are set to auto-start at boot?
- HKEY_USERS\<your SID>\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs
  - What recent documents are listed?

Registry keys reveal both system configuration and user activity.

Note: `whoami /user` on Command Prompt to find user SID.

---

## Prefetch Files

Prefetch Files: Files created by Windows to speed up program startup, which also record when and how often an application was executed.

Demo:

- Open Notepad
- Navigate to C:\Windows\Prefetch.
  - Do you see a new file like NOTEPAD.EXE-XXXXXX.pf?
- Note the file’s last modified time.

Prefetch shows when and how often an application was executed.

Open up NirSoft WinPrefetchView and show run counter.

## Link (LNK) Files

Link Files: Shortcut (.lnk) files that Windows creates when a user opens a file or folder, preserving the original path and access timestamps. These files persist even if the original file is deleted.

Demo:

- Create a simple text file on your Desktop (e.g., test.txt).
- Open it with Notepad.
- Navigate to C:\Users\<YourName>\AppData\Roaming\Microsoft\Windows\Recent.
  - Do you see a .lnk file pointing to test.txt?
- Open the .lnk file with Notepad. Can you find the original path inside?

Link files provide evidence of files being accessed.

Note: Make sure to show hidden files in file explorer otherwise AppData folder won't be visible.

---

## Shellbags

Shellbags: Registry entries that record how folders are accessed and viewed in Windows Explorer, including folders on external drives.

Demo:

- Browse to a few different folders on your system (e.g., C:\Windows\System32).
- Download and run ShellBags Explorer (by Eric Zimmerman).
- Look at the entries for folders you just visited.

Shellbags can prove that a user accessed a folder, even if it’s empty or later deleted.

---

## Event Logs

Event Logs: System-generated logs that record significant events such as logons, shutdowns, errors, and other activity on the computer. Useful for timelining.

Demo:

- Open Event Viewer
- Go to Windows Logs -> Security.
- Find an Event ID 4624 (successful logon). Who logged in, and when?
- Go to Windows Logs -> System.
- Find a system startup or shutdown event.

Logs complement registry and file artifacts by showing precise system events.

---

## Report 1

Marking breakdown

Core

- 30% Investigative Findings
- 40% Analysis of Findings
- 30% Presentation

Extended

- 45% Investigative Findings
- 35% Analysis of Findings
- 20% Presentation

Go over sample reports.

- https://jimsforensics.com/tutorials/resources/m57biz-report-excerpt-andrew.pdf
- https://jimsforensics.com/tutorials/resources/m57biz-report-excerpt-sascha.pdf

---

Questions from students:

Q: How can we load .E01 files into other tools e.g. WinPrefetchView?
A: From what I can tell the easiest way to do this is to download and install FTK Imager on your Windows installation, then `File > Add Evidence Item...` and select the .E01 image/s that you'd like to explore. Once you've loaded the .E01 images, you can locate the resources (e.g. hives, shellbags, prefetch files) that you're interested in, export them into a folder of your choosing, and then open them up from that folder using the relevant application. For example, I was able to extract the .pf prefetch files from an image (from `C:\WINDOWS\Prefetch`), and then open them up in WinPrefetchView (you'll need to go to `Options > Advanced Options` and modify the prefetch folder). Personally I find the Autopsy workflow more straightforward.

Q: Can I get a short extension for the challenges/reports?
A: For extensions (even short extensions), it would be best to contact cs6445@cse.unsw.edu.au.

Q: How can I download the ingest files from Autopsy?
A: After Autopsy has finished doing the ingest, all of the ingested files are placed in a case directory. On my machine that case Directory is under `Desktop/autopsy`, it will be different for you depending on where you told Autopsy to place the case directory when you ran the ingest modules. If you copy over that case directory to another Windows installation you should be able to load that case in Autopsy (without having to re-run the ingest).

Q: Are the sample reports samples of report 1 or report 2?
A: They are sampple report 1s from a _much_ earlier (pre-trimester) offering of this course.