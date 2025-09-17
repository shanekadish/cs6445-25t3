# Icebreakers

## About Me

What's your
- name
- degree
- favourite course so far
- least favourite course so far
- favourite password

# Course Administrivia

## Assessments
- 20%: weekly/fortnightly challenges
- 40%: forensics reports
  - 15%: report 1
  - 25%: report 2
- 40%: final

## Resources
- Official course forum: https://discourse01.cse.unsw.edu.au/25T3/COMP6445/
- SecSoc discord: https://tr.ee/loSdNPErJJ
- CSESoc discord: https://discord.gg/CUTCuKh5
- Course email address: cs6445@cse.unsw.edu.au
- My email address: s.kadish@unsw.edu.au

## Other bits n pieces
- LiveOverflow YT channel: https://www.youtube.com/liveoverflow
- https://ctf101.org/forensics/overview/
- https://gchq.github.io/CyberChef/

---

## Optional: Set up a Kali VM
- For Apple Silicon Macbooks, I'd recommend UTM. Otherwise VirtualBox should be fine.
- For UTM, use these instructions: https://www.kali.org/docs/virtualization/install-utm-guest-vm/
- Rationale: VM is good to isolate your host machine from potential malware. Kali is good because it comes with lots of security tools already installed (Autopsy, Sleuth Kit, Volatility, binwalk)
- Strictly speaking you should also disable networking and other sharing with host (e.g. clipboard) for extra isolation but I think that'd be overkill for this course

# Tutorial slides
https://jimsforensics.com/tutorials/1

# Kahoot
https://wayground.com/admin/quiz/6654f44bc22aa06ed8d1bccf/68445-intro-quiz?source=admin&trigger=quizPage

# File Metadata
- This is me: https://webcms3.cse.unsw.edu.au/users/z5075632
  - Where was I?
  - When was the photo taken?
- Has anyone seen the Netflix documentary 'Running With The Devil' about John McAfee?
  - https://en.wikipedia.org/wiki/John_McAfee#Death_of_Gregory_Faull
    - > In December 2012, the magazine Vice accidentally gave away McAfee's location at a Guatemalan resort, when a photo taken by one of its journalists accompanying him was posted with the Exif geolocation metadata still attached.
- `exiftool` demo
  - Note that it is trivial to spoof EXIF data using `exiftool`, e.g. `exiftool -DateTimeOriginal="2020:01:01 12:00:00" photo.jpg`. It may or may not be easy to detect whether the EXIF data has been spoofed depending on how sophisticated the spoof was.

---

# Steganography
- What type of file is `mystery`?
  - `file mystery`
  - `vi mystery`
  - `binwalk mystery`
  - `xxd mystery` and find PDF magic bytes suggested by `binwalk`
- https://en.wikipedia.org/wiki/List_of_file_signatures
- This is a very weak form of steganography, relying on the fact that PNG decoders stop after reading the IEND chunk.

