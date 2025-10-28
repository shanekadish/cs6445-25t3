# Week 7 Tutorial

## Report 1 Feedback

Stats:
Average Mark: 60
Std. Deviation: 16 

All tutors used the same (fairly objective) marking rubric, which covered presentation, findings, things asked for, and analysis (small). Some of these we're able to share with students (e.g. missing table of contents, missing version for tools, missing hashes, etc.), and some we're not (e.g. specific pieces of evidence that would have aided the investigation).

Please read Andrew's discourse post thoroughly: https://discourse01.cse.unsw.edu.au/25T3/COMP6445/t/report-2-guidance/171

- [ ] Table of Contents present
- [ ] Executive Summary is present (and clear)
- [ ] Qualifications section present
- [ ] Disclaimer section present
- [ ] Background section present
- [ ] Findings Labelled Clearly
- [ ] Tooling was consistently labelled WITHOUT VERSIONS
- [ ] Tooling was consistently labelled WITH VERSIONS
- [ ] Utilsation of exhibits
- [ ] Labelling of exhibits
- [ ] Paths of artifacts shown and labelled where possible
- [ ] Consistency in Timezone / Format
- [ ] Timezone is AEST/ACST
- [ ] ONLY the hash of hdd.7z was verified
- [ ] Conclusions / Recommendations present
- [ ] Timeline makes sense
- [ ] Report was easy to follow

See above to see where you might have lost marks on the presentation side of things. We have a similar rubric for evidence findings, things asked for, and overall analysis which I will not share since they're still relevant for report 2. You should be able to get an idea for some of those things by reading Andrew's discourse post above.

For the actual evidence findings rubric, here are some (not all) areas you may have lost marks (directly from Andrew's post)
* Did you see Alyx’s email to John Davis?
  * Can you confirm that Alyx (the person) sent the email?
* Did Alyx have a password on her computer account?
  * What does it mean if she did / did not?
* Do we know if files were actually copied to the USB?
  * Counter example: What if the USB was just plugged in but no files were copied?
* Other than files being simply located in the Downloads folder, how can we verify if files were actually downloaded, or where they came from?
  * Counter example 1: What if they already on the computer from a long time ago
  * Counter example 2: What if fake files were copied to the USB?
* Did you have a timeline? Did it make sense?
* Did you accuse Alyx? Was the evidence strong enough?
* Did you make good use of possibilities (likely/unlikely, etc.)
* Did the things that you ask for make sense? Would they have aided the investigation? E.g. email/network logs which we give you for report 2.

I'm happy to discuss and provide individual feedback during class today.

## Report 2 Tips

https://discourse01.cse.unsw.edu.au/25T3/COMP6445/t/report-2-guidance/171

## Mobile Forensics

## Background
Take a look at Andrew's notes before you do the challenges:
* https://featherbear.cc/UNSW-COMP6845-ios/#all
* https://featherbear.cc/UNSW-COMP6845-android/#all

## Android Challanges

### ALEAPP MacOS Installation
```
$ git clone git@github.com:abrignoni/ALEAPP.git
$ cd ~/ALEAPP

# You'll need to install some python libraries. It's generally best to do this in a virtual environment so that you don't interfere with your system python installation.
$ python3 -m venv venv
$ source venv/bin/activate

$ pip3 install --requirement requirements.txt

# In order to use the ALEAPP GUI, I also had to install Tkinter (python-tk)
$ brew install python-tk

$ python3 aleappGUI.py

# Now unzip the Android image zip file and select the .tar image file that you'd like to analyze in the GUI, leave all the modules ticked, and click 'Process'. Then you'll be given an option to open the report in your browser.
```

Note that you probably won't be able to solve all of the Android challenges using ALEAPP alone. You might need to poke around the disk image itself as well.

## iOS Challenges

Use the pre-generated ArtEx2 report that we provide here: https://featherbear.cc/UNSW-COMP6845-ios-artex/
