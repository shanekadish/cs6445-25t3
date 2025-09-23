Had pretty much no issues installing Windows 11 VM using VMWare Fusion on Apple Silicon Mac. Just used all defaults. Then followed Andrew's steps and video here: https://discourse01.cse.unsw.edu.au/25T3/COMP6445/t/preparing-for-week-2/38

64GB seemed not to be enough when extracting m57biz. Changed to 100GB but think I now need to reinstall Windows VM because I can't extend C drive since they're not contiguous.

MAKE SURE TO CLICK CUSTOMIZE AT THE END OF WINDOWS 11 INSTALLATION DIALOGUE AND MAKE IT > 80GB. I MADE MINE 100.

---

What is an E01 file? What tools can we use to analyse them? Demo `ewfinfo`.

Press `s` in tutorial slides to open up tutorial notes.

---

Report 1 has been released: https://webcms3.cse.unsw.edu.au/COMP6445/25T3/resources/116256 due October 12th. First step is to get Autopsy up and running on a Windows VM.

---

"When a file is "deleted" using a FAT file system, the directory entry remains almost unchanged except for the first character of the file name, preserving most of the "deleted" file's name, along with its time stamp, file length and — most importantly — its physical location on the disk." -- https://en.wikipedia.org/wiki/Undeletion#FAT_file_systems

## Demo: Find the remnants of a deleted file

```
# Create a 10MiB blank disk image
$ dd if=/dev/zero of=disk.img bs=1M count=10
10+0 records in
10+0 records out
10485760 bytes (10 MB, 10 MiB) copied, 0.00710028 s, 1.5 GB/s
$ ls -l disk.img 
-rw-rw-r-- 1 shane shane 10485760 Sep 23 07:37 disk.img

# Format the image as a FAT filesystem. FAT is commonly used on removable storage media (e.g. USBs) and some Windows systems.
$ mkfs.vfat disk.img
mkfs.fat 4.2 (2021-01-31)

# Mount the disk image to a directory where we can add/remove files.
# Files under mnt/ will be FAT-compliant (e.g. they will use `0xE5` to mark a directory entry as deleted: https://en.wikipedia.org/wiki/Design_of_the_FAT_file_system#Directory_entry)
$ mkdir mnt
$ sudo mount -o loop disk.img mnt

# Create a file with a secret message under mnt/ and confirm that the contents get saved
$ sudo bash -c 'echo "THIS IS A TOP SECRET MESSAGE!" > mnt/secret.txt'
$ cat mnt/secret.txt
THIS IS A TOP SECRET MESSAGE!

# Delete the file
$ sudo rm mnt/secret.txt

# Unmount the mnt directory so that we can begin inspecting the disk image
$ sudo umount mnt

# Hexdump the entire disk image
# Observe the boot sector in the first few bytes describing the FS type (FAT16 in this case) and other information
# Observe that the first character of the filename (secret.txt) has been overwritten with `0xe5` which is the "Entry has been previously erased and/or is available" marker on FAT filesystems
# Observe the deleted file contents
$ hexdump --canonical disk.img
00000000  eb 3c 90 6d 6b 66 73 2e  66 61 74 00 02 04 04 00  |.<.mkfs.fat.....|
00000010  02 00 02 00 50 f8 14 00  20 00 02 00 00 00 00 00  |....P... .......|
00000020  00 00 00 00 80 00 29 ed  b6 17 1b 4e 4f 20 4e 41  |......)....NO NA|
00000030  4d 45 20 20 20 20 46 41  54 31 36 20 20 20 0e 1f  |ME    FAT16   ..|
00000040  be 5b 7c ac 22 c0 74 0b  56 b4 0e bb 07 00 cd 10  |.[|.".t.V.......|
00000050  5e eb f0 32 e4 cd 16 cd  19 eb fe 54 68 69 73 20  |^..2.......This |
00000060  69 73 20 6e 6f 74 20 61  20 62 6f 6f 74 61 62 6c  |is not a bootabl|
00000070  65 20 64 69 73 6b 2e 20  20 50 6c 65 61 73 65 20  |e disk.  Please |
00000080  69 6e 73 65 72 74 20 61  20 62 6f 6f 74 61 62 6c  |insert a bootabl|
00000090  65 20 66 6c 6f 70 70 79  20 61 6e 64 0d 0a 70 72  |e floppy and..pr|
000000a0  65 73 73 20 61 6e 79 20  6b 65 79 20 74 6f 20 74  |ess any key to t|
000000b0  72 79 20 61 67 61 69 6e  20 2e 2e 2e 20 0d 0a 00  |ry again ... ...|
000000c0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
000001f0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 55 aa  |..............U.|
00000200  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00000800  f8 ff ff ff 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000810  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00003000  f8 ff ff ff 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00003010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00005800  e5 73 00 65 00 63 00 72  00 65 00 0f 00 ae 74 00  |.s.e.c.r.e....t.|
00005810  2e 00 74 00 78 00 74 00  00 00 00 00 ff ff ff ff  |..t.x.t.........|
00005820  e5 45 43 52 45 54 20 20  54 58 54 20 00 47 6d ad  |.ECRET  TXT .Gm.|
00005830  36 5b 36 5b 00 00 6d ad  36 5b 03 00 1e 00 00 00  |6[6[..m.6[......|
00005840  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
0000a000  54 48 49 53 20 49 53 20  41 20 54 4f 50 20 53 45  |THIS IS A TOP SE|
0000a010  43 52 45 54 20 4d 45 53  53 41 47 45 21 0a 00 00  |CRET MESSAGE!...|
0000a020  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00a00000
```

## Demo: Recover the deleted file

Note that `photorec` won't work here, because `photorec` carves out deleted files by searching the disk for file signatures (e.g. file signatures for PNG, PDF etc.) but the file we deleted was a plain text ASCII file, which doesn't have a signature. Other tools (e.g. The Sleuth Kit) can recover files based on the file metadata (e.g. the `0xE5` marker on directory entries in FAT filesystems).

```
# Show deleted files in disk.img using `fls` (part of The Sleuth Kit)
$ fls -d disk.img
r/r * 4: secret.txt

# Display the contents of the deleted file with inode number 4 using `icat` (also part of The Sleuth Kit)
$ icat disk.img 4
THIS IS A TOP SECRET MESSAGE!
```

# Find the deleted files stored in USB_key.img. Download here: https://unsw.sharepoint.com/sites/SecEDUForensics/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FSecEDUForensics%2FShared%20Documents%2FGeneral%2F2025%2Fdemos%2Ffile%20recovery&p=true&ga=1

```
┌──(shane㉿kali)-[~/cs6445-25t3/week02]
└─$ cat USB_key.hash && md5sum USB_key.img
88b0217001cb52f604fac3006137555d  USB_key.img
88b0217001cb52f604fac3006137555d  USB_key.img

# Check FS type and see that it's EXFAT
┌──(shane㉿kali)-[~/cs6445-25t3/week02]
└─$ hexdump --canonical USB_key.img | head
00000000  eb 76 90 45 58 46 41 54  20 20 20 00 00 00 00 00  |.v.EXFAT   .....|
00000010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00000040  20 00 00 00 00 00 00 00  e0 63 07 00 00 00 00 00  | ........c......|
00000050  80 00 00 00 00 02 00 00  80 02 00 00 2c ec 00 00  |............,...|
00000060  06 00 00 00 0f d9 85 5c  00 01 02 00 09 03 01 80  |.......\........|
00000070  57 00 00 00 00 00 00 00  f4 f4 f4 f4 f4 f4 f4 f4  |W...............|
00000080  f4 f4 f4 f4 f4 f4 f4 f4  f4 f4 f4 f4 f4 f4 f4 f4  |................|
*
000001f0  f4 f4 f4 f4 f4 f4 f4 f4  f4 f4 f4 f4 f4 f4 55 aa  |..............U.|

┌──(shane㉿kali)-[~/cs6445-25t3/week02]
└─$ mkdir usb_mnt                             

┌──(shane㉿kali)-[~/cs6445-25t3/week02]
└─$ sudo mount -t exfat USB_key.img usb_mnt 
[sudo] password for shane: 

# See non-deleted files
┌──(shane㉿kali)-[~/cs6445-25t3/week02]
└─$ ls -l usb_mnt 
total 208992
-rwxr-xr-x 1 root root 1935092 Mar 11  2019  aaron-burden-160110-unsplash.jpg
-rwxr-xr-x 1 root root 1049666 Mar 11  2019  andreas-gucklhorn-286746-unsplash.jpg
-rwxr-xr-x 1 root root 5545084 Mar 11  2019  andrew-worley-299610-unsplash.jpg
-rwxr-xr-x 1 root root 2712299 Mar 11  2019  byron-stumman-1194077-unsplash.jpg
-rwxr-xr-x 1 root root 3634354 Mar 11  2019  carlos-hernandez-1133995-unsplash.jpg
-rwxr-xr-x 1 root root 3864949 Mar 11  2019  charl-folscher-540836-unsplash.jpg
-rwxr-xr-x 1 root root 7966255 Mar 11  2019  christopher-burns-189796-unsplash.jpg
-rwxr-xr-x 1 root root 3037031 Mar 11  2019  clem-onojeghuo-218551-unsplash.jpg
-rwxr-xr-x 1 root root 7036725 Mar 11  2019  clint-bustrillos-1365479-unsplash.jpg
-rwxr-xr-x 1 root root 4748322 Mar 11  2019  cmdr-shane-610506-unsplash.jpg
-rwxr-xr-x 1 root root 3715739 Mar 11  2019  curtis-macnewton-316895-unsplash.jpg
-rwxr-xr-x 1 root root  473894 Mar 11  2019  daryn-stumbaugh-58483-unsplash.jpg
-rwxr-xr-x 1 root root 3751935 Mar 11  2019  david-clode-527265-unsplash.jpg
-rwxr-xr-x 1 root root 2839242 Mar 11  2019  eamonn-maguire-57074-unsplash.jpg
-rwxr-xr-x 1 root root 2089506 Mar 11  2019  fabio-issao-123332-unsplash.jpg
-rwxr-xr-x 1 root root 2992148 Mar 11  2019  fancycrave-252342-unsplash.jpg
-rwxr-xr-x 1 root root 3515467 Mar 11  2019  fancycrave-264508-unsplash.jpg
-rwxr-xr-x 1 root root 4412878 Mar 11  2019  fancycrave-310182-unsplash.jpg
-rwxr-xr-x 1 root root 4045379 Mar 11  2019  fancycrave-391044-unsplash.jpg
-rwxr-xr-x 1 root root 5072212 Mar 11  2019  fancycrave-494260-unsplash.jpg
-rwxr-xr-x 1 root root 2200102 Mar 11  2019  filipe-resmini-1311491-unsplash.jpg
-rwxr-xr-x 1 root root 1898410 Mar 11  2019  fredy-jacob-764477-unsplash.jpg
-rwxr-xr-x 1 root root 3532293 Mar 11  2019  frida-bredesen-328727-unsplash.jpg
-rwxr-xr-x 1 root root 3658768 Mar 11  2019  graphic-node-1360830-unsplash.jpg
-rwxr-xr-x 1 root root 2727189 Mar 11  2019  heather-zabriskie-65701-unsplash.jpg
-rwxr-xr-x 1 root root 1966102 Mar 11  2019  himesh-kumar-behera-327253-unsplash.jpg
-rwxr-xr-x 1 root root 8649219 Mar 11  2019  ilinca-roman-1276314-unsplash.jpg
-rwxr-xr-x 1 root root 4818558 Mar 11  2019  jabez-samuel-1329720-unsplash.jpg
-rwxr-xr-x 1 root root 1474036 Mar 11  2019  jamie-street-206985-unsplash.jpg
-rwxr-xr-x 1 root root 4002013 Mar 11  2019  jason-ortego-5383-unsplash.jpg
-rwxr-xr-x 1 root root 6050649 Mar 11  2019  jeffrey-hamilton-571430-unsplash.jpg
-rwxr-xr-x 1 root root 2264508 Mar 11  2019  jiri-sifalda-299258-unsplash.jpg
-rwxr-xr-x 1 root root 7427969 Mar 11  2019  joao-silas-29233-unsplash.jpg
-rwxr-xr-x 1 root root 3512363 Mar 11  2019  joel-jasmin-forestbird-595545-unsplash.jpg
-rwxr-xr-x 1 root root 4576664 Mar 11  2019  josh-applegate-1414230-unsplash.jpg
-rwxr-xr-x 1 root root 1428982 Mar 11  2019  joshua-earle-33443-unsplash.jpg
-rwxr-xr-x 1 root root  805526 Mar 11  2019  kevin-ku-364843-unsplash.jpg
-rwxr-xr-x 1 root root  763895 Mar 11  2019  leslie-holder-555818-unsplash.jpg
-rwxr-xr-x 1 root root 3086738 Mar 11  2019  louis-tricot-1165630-unsplash.jpg
-rwxr-xr-x 1 root root 4081084 Mar 11  2019  luther-bottrill-646018-unsplash.jpg
-rwxr-xr-x 1 root root 4711498 Mar 11  2019  marija-zaric-1370544-unsplash.jpg
-rwxr-xr-x 1 root root 1405736 Mar 11  2019  mario-purisic-52769-unsplash.jpg
-rwxr-xr-x 1 root root 7221413 Mar 11  2019  markus-spiske-1423-unsplash.jpg
-rwxr-xr-x 1 root root  178727 Mar 11  2019  matt-artz-353279-unsplash.jpg
-rwxr-xr-x 1 root root 2036511 Mar 11  2019  matteo-vistocco-1201062-unsplash.jpg
-rwxr-xr-x 1 root root 2718032 Mar 11  2019  matthew-kosloski-137750-unsplash.jpg
-rwxr-xr-x 1 root root  801142 Mar 11  2019  matthew_t_rader-1141526-unsplash.jpg
-rwxr-xr-x 1 root root 1496449 Mar 11  2019  mavis-cw-164128-unsplash.jpg
-rwxr-xr-x 1 root root 2888740 Mar 11  2019  mikael-stenberg-1177524-unsplash.jpg
-rwxr-xr-x 1 root root 2116319 Mar 11  2019  mr-cup-fabien-barral-86074-unsplash.jpg
-rwxr-xr-x 1 root root 2850093 Mar 11  2019  nimish-chauhan-538714-unsplash.jpg
-rwxr-xr-x 1 root root 3928250 Mar 11  2019  peter-hershey-125608-unsplash.jpg
-rwxr-xr-x 1 root root 2699164 Mar 11  2019  ravi-n-jha-540497-unsplash.jpg
-rwxr-xr-x 1 root root  674545 Mar 11  2019  rawpixel-1055774-unsplash.jpg
-rwxr-xr-x 1 root root 4292757 Mar 11  2019  richard-payette-522432-unsplash.jpg
-rwxr-xr-x 1 root root  176482 Aug 10  2020 'screen_shot (1).jpg'
-rwxr-xr-x 1 root root 2150012 Mar 11  2019  thomas-martinsen-2158-unsplash.jpg
-rwxr-xr-x 1 root root 3560819 Mar 11  2019  thomas-millot-462080-unsplash.jpg
-rwxr-xr-x 1 root root 2642984 Mar 11  2019  tobias-tullius-1238848-unsplash.jpg
-rwxr-xr-x 1 root root 6186742 Mar 11  2019  todd-quackenbush-701-unsplash.jpg
-rwxr-xr-x 1 root root 3001823 Mar 11  2019  ulrich-pickert-659441-unsplash.jpg
-rwxr-xr-x 1 root root 1753791 Mar 11  2019  vipul-uthaiah-1206340-unsplash.jpg
-rwxr-xr-x 1 root root 4114433 Mar 11  2019  yash-raut-1096197-unsplash.jpg
-rwxr-xr-x 1 root root 3774642 Mar 11  2019  yash-raut-1121691-unsplash.jpg
-rwxr-xr-x 1 root root 3120591 Mar 11  2019  yu-kato-613711-unsplash.jpg

┌──(shane㉿kali)-[~/cs6445-25t3/week02]
└─$ open usb_mnt/yu-kato-613711-unsplash.jpg 

┌──(shane㉿kali)-[~/cs6445-25t3/week02]
└─$ photorec USB_key.img 
PhotoRec 7.2, Data Recovery Utility, February 2024
Christophe GRENIER <grenier@cgsecurity.org>
https://www.cgsecurity.org

┌──(shane㉿kali)-[~/cs6445-25t3/week02]
└─$ ls -l recup_dir.1 
total 85044
-rw-rw-r-- 1 shane shane 1428982 Sep 23 09:38 f0263472.jpg
-rw-rw-r-- 1 shane shane  805526 Sep 23 09:38 f0266264.jpg
-rw-rw-r-- 1 shane shane  763895 Sep 23 09:38 f0267840.jpg
-rw-rw-r-- 1 shane shane 3086738 Sep 23 09:38 f0273128.jpg
-rw-rw-r-- 1 shane shane 4081084 Sep 23 09:38 f0279160.jpg
-rw-rw-r-- 1 shane shane 4711498 Sep 23 09:38 f0287136.jpg
-rw-rw-r-- 1 shane shane 1405736 Sep 23 09:38 f0296344.jpg
-rw-rw-r-- 1 shane shane 7221413 Sep 23 09:38 f0299096.jpg
-rw-rw-r-- 1 shane shane  178727 Sep 23 09:38 f0313208.jpg
-rw-rw-r-- 1 shane shane 2036511 Sep 23 09:38 f0313560.jpg
-rw-rw-r-- 1 shane shane  801142 Sep 23 09:38 f0317544.jpg
-rw-rw-r-- 1 shane shane 2718032 Sep 23 09:38 f0319112.jpg
-rw-rw-r-- 1 shane shane 1496449 Sep 23 09:38 f0324424.jpg
-rw-rw-r-- 1 shane shane 2888740 Sep 23 09:38 f0327352.jpg
-rw-rw-r-- 1 shane shane 2116319 Sep 23 09:38 f0333000.jpg
-rw-rw-r-- 1 shane shane 2850093 Sep 23 09:38 f0337136.jpg
-rw-rw-r-- 1 shane shane 3928250 Sep 23 09:38 f0342704.jpg
-rw-rw-r-- 1 shane shane 2699164 Sep 23 09:38 f0350384.jpg
-rw-rw-r-- 1 shane shane  674545 Sep 23 09:38 f0355656.jpg
-rw-rw-r-- 1 shane shane 4292757 Sep 23 09:38 f0356976.jpg
-rw-rw-r-- 1 shane shane 2150012 Sep 23 09:38 f0373760.jpg
-rw-rw-r-- 1 shane shane 3560819 Sep 23 09:38 f0377960.jpg
-rw-rw-r-- 1 shane shane 2642984 Sep 23 09:38 f0384920.jpg
-rw-rw-r-- 1 shane shane 6186742 Sep 23 09:38 f0390088.jpg
-rw-rw-r-- 1 shane shane 3001823 Sep 23 09:38 f0402176.jpg
-rw-rw-r-- 1 shane shane 1753791 Sep 23 09:38 f0408040.jpg
-rw-rw-r-- 1 shane shane 4114433 Sep 23 09:38 f0411472.jpg
-rw-rw-r-- 1 shane shane 3774642 Sep 23 09:38 f0419512.jpg
-rw-rw-r-- 1 shane shane 3120591 Sep 23 09:38 f0426888.jpg
-rw-rw-r-- 1 shane shane 2355200 Sep 23 09:38 f0432984.apple
-rw-rw-r-- 1 shane shane 4166903 Sep 23 09:38 f0437584.jpg
-rw-rw-r-- 1 shane shane    7653 Sep 23 09:38 report.xml

sudo umount usb_mnt
```

---

# Autopsy demo