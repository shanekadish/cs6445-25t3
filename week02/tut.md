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