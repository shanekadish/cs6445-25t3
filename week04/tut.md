# Week 4 Tutorial

https://webcms3.cse.unsw.edu.au/static/uploads/course/COMP6445/25T3/9f96132f36c1455fc8a1d0d1513809ca5e94daa421e053ea748d8cf536ab90a7/COMP6445_25T3_Week4_Technical_Lecture_Memory_Forensics.pdf

https://jimsforensics.com/tutorials/4/#/

https://cases.jimsforensics.com/challenges

https://github.com/volatilityfoundation/volatility3

https://en.wikipedia.org/wiki/WannaCry_ransomware_attack

## Volatility

Installation on my MacBook using `pipx`

```
> pipx install volatility3
  installed package volatility3 2.26.2, installed using Python 3.13.7
  These apps are now globally available
    - vol
    - volshell
done! ✨ 🌟 ✨
```

```
> strings wcry.raw | grep 'encrypt'
Indicates whether to encrypt the message before forwarding.
Windows 2000 supports 3 levels of Encryption are: Low: Only data sent from client to server is protected by encryption based on server's standard key strength. Data sent from Server to client is not protected. Medium / Client Compatible: All data sent between Server and client is protected by encryption based on server's standard key strength. High: All data sent between Server and client is protected by encryption based on server's maximum key strength. Windows 2001 supports 2 levels of Encryption: Client Compatible andHigh.
NIC returns 0 supported auth/encrypt pair
Absorbing error %d when disabling encryption
ExtractConfigFromProfile[encryption]: FAILed, dwError=<%d>
miscReloadDatabase: Can't get encryption 0x%08x
            print 'Test encryption: ', c
\fs22\loch\af31502\hich\af31502\dbch\af53\insrsid14313477\charrsid5733561 \hich\af31502\dbch\af53\loch\f31502 our important files are encrypted.
e because they have been encrypted. Maybe you are busy looking for a way to recover your files, but do not waste your time. Nobody can recover your files without our decryption service.
\par }{\rtlch\fcs1 \af53 \ltrch\fcs0 \fs22\loch\af31502\hich\af31502\dbch\af53\insrsid15289305\charrsid5275506 \hich\af31502\dbch\af53\loch\f31502 Ang iyong mahalagang mga file ay naka-encrypt.
Marami sa iyong mga dokumento, mga larawan, video, database at iba pang mga file ay hindi na maa-access dahil ang mga ito ay nai-naka-encrypt. Siguro ikaw ay abala naghahanap para sa isang paraan upang mabawi ang iyong mga file, ngunit huwag mag-aksaya ng
A:  Ooops, your important files are encrypted. It means you will not be able to access them anymore until they are decrypted.
encrypt
DwAddClientIpSecFilter: Already a filter with a different encryption(%d) type exists for ths dest address. port=%d
AddIpSecFilter, port=%d, fServer=%d, encryption=%d
DwAddClientIpSecFilter: Already a filter with a different encryption(%d) type exists for ths dest address. port=%d
AddIpSecFilter, port=%d, fServer=%d, encryption=%d
Failed to encrypt data: 0x%x
We do not want to receive any compression or encryption from the remote side
We do not require encryption locally; we won't request for it
We do not want any compression or encryption on the local side
Not disabling encryption; Not forcing encryption
Will not force encryption: type not specified
Will force encryption
MD4 encryption
SR encryption
bad encryption type reset to SRE
Checking encryption. Policy=0x%x,Types=0x%x,Mask=0x%x
Strong encryption
Checking encryption. Policy=0x%x,Types=0x%x,Mask=0x%x
Strong encryption
\WINDOWS\Help\encrypt.chm = "encryptW.chm","183ce"
client EAP encryption
 ~/cs6445-25t3/week04  main ?1                                                                                                                                                       11:04:37 AM
```

Notes

- See ransom note in both English and Tagalog and other languages

```
> strings wcry.raw | grep 'bitcoin'
http://www.btcfrog.com/qr/bitcoinPNG.php?address=%s
https://www.google.com/search?q=how+to+buy+bitcoin
Send $%d worth of bitcoin to this address:
\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid9575898\charrsid3415140 \hich\af31502\dbch\af31505\loch\f31502 About}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid3230241\charrsid3415140 \hich\af31502\dbch\af31505\loch\f31502  bitcoin>.
\par \hich\af31502\dbch\af31505\loch\f31502 \hich\f31502 Tjek venligst den nuv\'e6\loch\f31502 \hich\f31502 rende pris p\'e5\loch\f31502 \hich\f31502  Bitcoin og k\'f8\loch\f31502 \hich\f31502 b nogle bitcoins. For mere information, klik p\'e5\loch\f31502  <}{
\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid9575898\charrsid3415140 \hich\af31502\dbch\af31505\loch\f31502 How to buy}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid3230241\charrsid3415140 \hich\af31502\dbch\af31505\loch\f31502  bitcoins>.
\uc1\u-29722\'3f\uc2\u24773\'b1\'a1}{\rtlch\fcs1 \af53\afs22 \ltrch\fcs0 \fs22\loch\af18\hich\af18\dbch\af18\insrsid4986254\charrsid8656048 \hich\af18\dbch\af18\loch\f18  <About bitcoin>}{\rtlch\fcs1 \af90\afs22 \ltrch\fcs0
\hich\af18\dbch\af18\loch\f18 <How to buy bitcoins>}{\rtlch\fcs1 \af90\afs22 \ltrch\fcs0 \fs22\loch\af18\hich\af18\dbch\af18\insrsid4986254\charrsid8656048 \loch\af18\hich\af18\dbch\f18 \u12290\'a1\'43}{\rtlch\fcs1 \af53\afs22 \ltrch\fcs0
\par }{\rtlch\fcs1 \af53 \ltrch\fcs0 \fs22\loch\af31502\hich\af31502\dbch\af53\insrsid13717663\charrsid6386681 \hich\af31502\dbch\af53\loch\f31502 Pembayaran diterima hanya di Bitcoin. Untuk informasi lebih lanjut, klik <About bitcoin>.
\par \hich\af31502\dbch\af53\loch\f31502 Silakan pe\hich\af31502\dbch\af53\loch\f31502 riksa harga Bitcoin saat ini dan beli beberapa bitcoin. Untuk informasi lebih lanjut, klik <}{\rtlch\fcs1 \af53 \ltrch\fcs0
\fs22\loch\af31502\hich\af31502\dbch\af53\insrsid15301782 \hich\af31502\dbch\af53\loch\f31502 How to buy}{\rtlch\fcs1 \af53 \ltrch\fcs0 \fs22\loch\af31502\hich\af31502\dbch\af53\insrsid13717663\charrsid6386681 \hich\af31502\dbch\af53\loch\f31502  bitcoin}
\fs22\loch\af31502\hich\af31502\dbch\af53\insrsid14313477\charrsid5733561 \hich\af31502\dbch\af53\loch\f31502 ayment is accepted in Bitcoin only. For more i\hich\af31502\dbch\af53\loch\f31502 nformation, click <About bitcoin>.
\par \hich\af31502\dbch\af53\loch\f31502 Please check the current price of Bitcoin and buy some bitcoins. For more information, click <How to buy bitcoins>.
\hich\af31502\dbch\af31505\loch\f31502 How to buy bitcoins}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid13253629\charrsid13383269 \hich\af31502\dbch\af31505\loch\f31502 >}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid13253629\charrsid13383269
 bitcoin>.
\par \hich\af31502\dbch\af53\loch\f31502 Mangyaring suriin ang kasalukuyang presyo ng Bitcoin at bumili ng il\hich\af31502\dbch\af53\loch\f31502 ang mga bitcoins. Para sa karagdagang impormasyon, i-click <}{\rtlch\fcs1 \af53 \ltrch\fcs0
 bitcoins>.
\fs22\loch\af31502\hich\af31502\dbch\af53\insrsid16074940 \hich\af31502\dbch\af53\loch\f31502 About}{\rtlch\fcs1 \af53 \ltrch\fcs0 \fs22\loch\af31502\hich\af31502\dbch\af53\insrsid1584092\charrsid16074940 \hich\af31502\dbch\af53\loch\f31502  bitcoin>.
\par \hich\af31502\dbch\af53\loch\f31502 Controleer de huidige prijs van Bitcoin en koop\hich\af31502\dbch\af53\loch\f31502  een aantal bitcoins. Kl}{\rtlch\fcs1 \af53 \ltrch\fcs0 \fs22\loch\af31502\hich\af31502\dbch\af53\insrsid16074940
\hich\af31502\dbch\af53\loch\f31502 ik voor meer info\hich\af31502\dbch\af53\loch\f31502 rmatie op <}{\rtlch\fcs1 \af53 \ltrch\fcs0 \fs22\loch\af31502\hich\af31502\dbch\af53\insrsid16074940 \hich\af31502\dbch\af53\loch\f31502 How to buy bitcoins}{
es, clique em <About bitcoin>.
\par \hich\af31502\dbch\af31505\loch\f31502 \hich\f31502 Verifique o pre\'e7\loch\f31502 o atual do Bitcoin e compre alguns bitcoins. Para obter mais\hich\af31502\dbch\af31505\loch\f31502 \hich\f31502  informa\'e7\'f5\loch\f31502 es, clique em <}{\rtlch\fcs1
\af2 \ltrch\fcs0 \f31502\fs22\insrsid7362391 \hich\af31502\dbch\af31505\loch\f31502 How to buy }{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid8666578\charrsid7362391 \hich\af31502\dbch\af31505\loch\f31502 bitcoins>.
\hich\af31502\dbch\af31505\loch\f31502  <}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid13383269\charrsid13383269 \hich\af31502\dbch\af31505\loch\f31502 About bitcoin}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid13253629\charrsid13383269
\'eb\'e8\'ea\'ed\'e5\'f2\'e5\loch\f31529 \hich\f31529  \'e2\'fa\'f0\'f5\'f3\loch\f31529  <About bitcoin>.
\'e0\loch\f31529 \hich\f31529  Bitcoin \'e8\loch\f31529 \hich\f31529  \'ea\'f3\'ef\'e5\'f2\'e5\loch\f31529 \hich\f31529  \'ec\'e0\'eb\'ea\'ee\loch\f31529 \hich\f31529  bitcoins. \'c7\'e0\loch\f31529 \hich\f31529  \'ef\'ee\'e2\'e5\'f7\'e5\loch\f31529
\hich\af31502\dbch\af31505\loch\f31502 <How to buy bitcoins>.}{\rtlch\fcs1 \af2\afs22 \ltrch\fcs0 \f31502\fs22\insrsid1210503\charrsid3293431
a samo u Bitcoinu. Za vi\'9a\loch\f31528 e informacija kliknite <About bitcoin>.
\par }{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\insrsid10496485\charrsid4460681 \hich\af31502\dbch\af31505\loch\f31502 \hich\f31502 Provjerite trenutnu cijenu Bitcoina i kupite neke bitcoine. Za vi\'9a\loch\f31502 e informacija kliknite <}{\rtlch\fcs1 \af2
\ltrch\fcs0 \f31502\insrsid4928345\charrsid4460681 \hich\af31502\dbch\af31505\loch\f31502 How to buy}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\insrsid10496485\charrsid4460681 \hich\af31502\dbch\af31505\loch\f31502  bitcoin}{\rtlch\fcs1 \af2 \ltrch\fcs0
\ltrch\fcs0 \f31502\fs22\insrsid8458214\charrsid12743656 \loch\af31502\dbch\af31505\hich\f31502 \uc1\u539\'3f}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid8458214\charrsid12743656 \hich\af31502\dbch\af31505\loch\f31502 i clic pe <About bitcoin>.
\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid8458214\charrsid12743656 \hich\af31502\dbch\af31505\loch\f31502 te bitcoins. Pentru mai multe informa}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid8458214\charrsid12743656
\f31502\fs22\insrsid12743656 \hich\af31502\dbch\af31505\loch\f31502 How to buy bitcoins}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid8458214\charrsid12743656 \hich\af31502\dbch\af31505\loch\f31502 >.
\loch\f31531  <About bitcoin>.
\loch\af31531\dbch\af31505\hich\f31531 \'ef\'f5\loch\f31531 \hich\f31531  Bitcoin \'ea\'e1\'e9\loch\f31531 \hich\f31531  \'e1\'e3\'ef\'f1\'dc\'f3\'f4\'e5\loch\f31531 \hich\f31531  \'ea\'dc\'f0\'ef\'e9\'e1\loch\f31531 \hich\f31531  bitcoins. \'c3\'e9\'e1
\hich\af31502\dbch\af31505\loch\f31502  bitcoins>.
\fs22\lang1033\langfe1028\loch\af11\hich\af11\dbch\af11\langfenp1028\insrsid1060393\charrsid1060393 \hich\af11\dbch\af11\loch\f11  <About bitcoin>}{\rtlch\fcs1 \af41\afs22 \ltrch\fcs0
 accettato solo in Bitcoin. Per ulteriori informazioni, fare clic su <About bitcoin>.
\par \hich\af31502\dbch\af31505\loch\f31502 Controlli prego il prezzo corrente di Bitcoin e comprate dei bitcoins. Per ulteriori informazioni, fare clic su <}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid10358742 \hich\af31502\dbch\af31505\loch\f31502
How to buy}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid13258867\charrsid10358742 \hich\af31502\dbch\af31505\loch\f31502  bitcoins>.
\rtlch\fcs1 \af2 \ltrch\fcs0 \fs22\loch\af11\hich\af11\dbch\af11\insrsid6753449\charrsid7629781 \hich\af11\dbch\af11\loch\f11 How to buy bitcoins}{\rtlch\fcs1 \af2 \ltrch\fcs0 \fs22\loch\af11\hich\af11\dbch\af11\insrsid1725662\charrsid7629781
\hich\f31535 jo cenu Bitcoin un nopirkt da\'fe\loch\f31535 \hich\f31535 as bitcoins. Lai ieg\'fb\loch\f31535 \hich\f31535 tu vair\'e2\loch\f31535 \hich\f31535 k inform\'e2\loch\f31535 \hich\f31535 cijas, noklik\'f0\'ed\loch\f31535 iniet uz <}{\rtlch\fcs1
\af2 \ltrch\fcs0 \f31502\fs22\insrsid854638 \hich\af31502\dbch\af31505\loch\f31502 How to buy}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid9469691\charrsid854638 \hich\af31502\dbch\af31505\loch\f31502  bitcoins\hich\af31502\dbch\af31505\loch\f31502
\hich\af31502\dbch\af31505\loch\f31502  bitcoin>.
\par \hich\af31502\dbch\af31505\loch\f31502 \hich\f31502 Tarkista bitcoinin nykyinen hinta ja osta bitcoins. Saat lis\'e4\loch\f31502 tietoja napsauttamalla <}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid11698073 \hich\af31502\dbch\af31505\loch\f31502
How to buy bitcoins}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid5593755\charrsid11698073 \hich\af31502\dbch\af31505\loch\f31502 >.
r weitere Informationen klicken Sie auf <How to buy bitcoins>.
 buy bitcoins}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid11827162\charrsid10775863 \hich\af31502\dbch\af31505\loch\f31502 >.
 <About bitcoin>.
\par \hich\af31502\dbch\af31505\loch\f31502 \hich\f31502 V\'e4\loch\f31502 \hich\f31502 nligen kolla nuvarande pris p\'e5\loch\f31502 \hich\f31502  Bitcoin och k\'f6\loch\f31502 \hich\f31502 p lite bitcoins. F\'f6\loch\f31502 \hich\f31502
\hich\af31502\dbch\af31505\loch\f31502 bitcoins>.
$%d worth of bitcoin
\hich\af31502\dbch\af31505\loch\f31502 About }{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid4091053\charrsid14050168 \hich\af31502\dbch\af31505\loch\f31502 bitcoin>.
\par \hich\af31502\dbch\af31505\loch\f31502 \hich\f31502 Vennligst sjekk den n\'e5\loch\f31502 \hich\f31502 v\'e6\loch\f31502 \hich\f31502 rende prisen p\'e5\loch\f31502 \hich\f31502  Bitcoin og kj\'f8\loch\f31502 p litt bitcoins. For mer informasjon, klikk <}
\hich\af31502\dbch\af31505\loch\f31502 bitcoins>.
\ltrch\fcs0 \f31502\fs22\insrsid15614891 \hich\af31502\dbch\af31505\loch\f31502 About}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid14574943\charrsid15614891 \hich\af31502\dbch\af31505\loch\f31502  bitcoin>.
\par \hich\af31502\dbch\af31505\loch\f31502 \hich\f31502 Veuillez v\'e9\loch\f31502 rifier le prix actuel de Bitcoin et acheter des bitcoins. Pour plus d'informations, cliquez sur <}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid15614891
\hich\af31502\dbch\af31505\loch\f31502 How to buy}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid14574943\charrsid15614891 \hich\af31502\dbch\af31505\loch\f31502  bitcoins>.
$%d worth of bitcoin
in <}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid3365448 \hich\af31502\dbch\af31505\loch\f31502 About bitcoin}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31532\fs22\insrsid9916548\charrsid3365448 \hich\af31532\dbch\af31505\loch\f31532 \hich\f31532 > se\'e7
\ltrch\fcs0 \f31502\fs22\insrsid3365448 \hich\af31502\dbch\af31505\loch\f31502 How to buy bitcoins}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31532\fs22\insrsid9916548\charrsid3365448 \hich\af31532\dbch\af31505\loch\f31532 \hich\f31532 > 'a t\'fd\loch\f31532
\par \hich\af31502\dbch\af31505\loch\f31502 Por favor, compruebe el precio actual de Bitcoin y compre algunos bitcoins. P\hich\af31502\dbch\af31505\loch\f31502 \hich\f31502 ara obtener m\'e1\loch\f31502 \hich\f31502 s informaci\'f3\loch\f31502
n, haga clic en <}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid16268367 \hich\af31502\dbch\af31505\loch\f31502 How to buy}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid13056521\charrsid16268367 \hich\af31502\dbch\af31505\loch\f31502  bitcoins>.
\loch\f31529  <}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid8528114 \hich\af31502\dbch\af31505\loch\f31502 How to buy bitcoins}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid12997017\charrsid8528114 \hich\af31502\dbch\af31505\loch\f31502 >.
<About bitcoin>}{\rtlch\fcs1 \af2 \ltrch\fcs0 \fs22\loch\af11\hich\af11\dbch\af11\insrsid1725662\charrsid7629781 \loch\af11\hich\af11\dbch\f11 \u12434\'82\'f0\u12463\'83\'4e\u12522\'83\'8a\u12483\'83\'62\u12463\'83\'4e\u12375\'82\'b5\u12390\'82\'c4\u12367
\par }{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31528\fs22\insrsid6824009\charrsid10490236 \hich\af31528\dbch\af31505\loch\f31528 \hich\f31528 Skontrolujte aktu\'e1\loch\f31528 \hich\f31528 lnu cenu produktu Bitcoin a k\'fa\loch\f31528 \hich\f31528 pte si bitcoins. \'cf
\f31502\fs22\insrsid10490236 \hich\af31502\dbch\af31505\loch\f31502 How to buy}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid6824009\charrsid10490236 \hich\af31502\dbch\af31505\loch\f31502  bitcoins>.
\ltrch\fcs0 \f31502\fs22\insrsid14315351\charrsid3475210 \hich\af31502\dbch\af31505\loch\f31502 \hich\f31502 p v\'e0\loch\f31502 o <About bitcoin>.
\loch\af31502\dbch\af31505\hich\f31502 \uc1\u7897\'3f}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31528\fs22\insrsid14315351\charrsid3475210 \hich\af31528\dbch\af31505\loch\f31528 \hich\f31528 t \'ed\loch\f31528 \hich\f31528 t bitcoins. \'d0}{\rtlch\fcs1 \af2
\hich\af31528\dbch\af31505\loch\f31528 \hich\f31528 oin. Aby uzyska\'e6\loch\f31528 \hich\f31528  wi\'ea\loch\f31528 cej informacji, kliknij przycisk <About bitcoin>.
\par \hich\af31528\dbch\af31505\loch\f31528 \hich\f31528 Sprawd\'9f\loch\f31528 \hich\f31528  bie\'bf\'b9\loch\f31528 \hich\f31528 c\'b9\loch\f31528 \hich\f31528  cen\'ea\loch\f31528 \hich\f31528  Bitcoin i kup troch\'ea\loch\f31528 \hich\f31528  bitcoin\'f3
\par \hich\af31502\dbch\af31505\loch\f31502 \hich\f31502 Zkontrolujte pros\'ed\loch\f31502 \hich\f31502 m aktu\'e1\loch\f31502 \hich\f31502 ln\'ed\loch\f31502 \hich\f31502  cenu produktu Bitcoin a kupte si bitcoin. Dal\'9a\'ed\loch\f31502 \hich\f31502
 informace z\'ed\loch\f31502 \hich\f31502 sk\'e1\loch\f31502 \hich\f31502 te klepnut\'ed\loch\f31502 m na odkaz <}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid16339550\charrsid1518393 \hich\af31502\dbch\af31505\loch\f31502 How to buy bitcoins}{
\'ed\'e8\'f2\'e5\'eb\'fc\'ed\'ee\'e9\loch\f31529 \hich\f31529  \'e8\'ed\'f4\'ee\'f0\'ec\'e0\'f6\'e8\'e8\loch\f31529 \hich\f31529  \'ed\'e0\'e6\'ec\'e8\'f2\'e5\loch\f31529  <About bitcoin>.
How to buy}{\rtlch\fcs1 \af2 \ltrch\fcs0 \f31502\fs22\insrsid14315351\charrsid3475210 \hich\af31502\dbch\af31505\loch\f31502  bitcoins>.
    Please send %s to this bitcoin address: %s
http://www.btcfrog.com/qr/bitcoinPNG.php?address=%s
https://www.google.com/search?q=how+to+buy+bitcoin
Send $%d worth of bitcoin to this address:
http://www.btcfrog.com/qr/bitcoinPNG.php?address=12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw
Send $300 worth of bitcoin to this address:
About bitcoin
How to buy bitcoins?
https://www.google.com/search?q=how+to+buy+bitcoin
http://www.btcfrog.com/qr/bitcoinPNG.php?address=%s
https://www.google.com/search?q=how+to+buy+bitcoin
Send $%d worth of bitcoin to this address:
http://www.btcfrog.com/qr/bitcoinPNG.php?address=%s
https://www.google.com/search?q=how+to+buy+bitcoin
Send $%d worth of bitcoin to this address:
http://www.btcfrog.com/qr/bitcoinPNG.php?address=%s
https://www.google.com/search?q=how+to+buy+bitcoin
Send $%d worth of bitcoin to this address:
http://www.btcfrog.com/qr/bitcoinPNG.php?address=%s
https://www.google.com/search?q=how+to+buy+bitcoin
Send $%d worth of bitcoin to this address:
http://www.btcfrog.com/qr/bitcoinPNG.php?address=%s
https://www.google.com/search?q=how+to+buy+bitcoin
Send $%d worth of bitcoin to this address:
```

Notes

- See ransom note in both English and Tagalog and other languages

```
> vol --file=wcry.raw windows.info
Volatility 3 Framework 2.26.2
Progress:  100.00		PDB scanning finished
Variable	Value

Kernel Base	0x804d7000
DTB	0x39000
Symbols	file:///Users/shane/.local/pipx/venvs/volatility3/lib/python3.13/site-packages/volatility3/symbols/windows/ntoskrnl.pdb/423320282DB842E7BA2B0BFC86A84D75-2.json.xz
Is64Bit	False
IsPAE	False
layer_name	0 WindowsIntel
memory_layer	1 FileLayer
KdDebuggerDataBlock	0x8054cf60
NTBuildLab	2600.xpsp_sp3_qfe.130704-0421
CSDVersion	3
KdVersionBlock	0x8054cf38
Major/Minor	15.2600
MachineType	332
KeNumberProcessors	1
SystemTime	2017-05-12 21:26:32+00:00
NtSystemRoot	C:\WINDOWS
NtProductType	NtProductWinNt
NtMajorVersion	5
NtMinorVersion	1
PE MajorOperatingSystemVersion	5
PE MinorOperatingSystemVersion	1
PE Machine	332
PE TimeDateStamp	Thu Jul  4 02:58:58 2013
```

Notes

- System is Windows XP SP3 (service pack 3)
- SystemTime is 2017 which is when WannaCry was released

```
> vol --file=wcry.raw windows.pslist
Volatility 3 Framework 2.26.2
Progress:  100.00		PDB scanning finished
PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime	File output

4	0	System	0x823c8830	51	244	N/A	False	N/A	N/A	Disabled
348	4	smss.exe	0x82169020	3	19	N/A	False	2017-05-12 21:21:55.000000 UTC	N/A	Disabled
596	348	csrss.exe	0x82161da0	12	352	0	False	2017-05-12 21:22:00.000000 UTC	N/A	Disabled
620	348	winlogon.exe	0x8216e020	23	536	0	False	2017-05-12 21:22:01.000000 UTC	N/A	Disabled
664	620	services.exe	0x821937f0	15	265	0	False	2017-05-12 21:22:01.000000 UTC	N/A	Disabled
676	620	lsass.exe	0x82191658	23	353	0	False	2017-05-12 21:22:01.000000 UTC	N/A	Disabled
836	664	svchost.exe	0x8221a2c0	19	211	0	False	2017-05-12 21:22:02.000000 UTC	N/A	Disabled
904	664	svchost.exe	0x821b5230	9	227	0	False	2017-05-12 21:22:03.000000 UTC	N/A	Disabled
1024	664	svchost.exe	0x821af7e8	79	1366	0	False	2017-05-12 21:22:03.000000 UTC	N/A	Disabled
1084	664	svchost.exe	0x8203b7a8	6	72	0	False	2017-05-12 21:22:03.000000 UTC	N/A	Disabled
1152	664	svchost.exe	0x821bea78	10	173	0	False	2017-05-12 21:22:06.000000 UTC	N/A	Disabled
1484	664	spoolsv.exe	0x821e2da0	14	124	0	False	2017-05-12 21:22:09.000000 UTC	N/A	Disabled
1636	1608	explorer.exe	0x821d9da0	11	331	0	False	2017-05-12 21:22:10.000000 UTC	N/A	Disabled
1940	1636	tasksche.exe	0x82218da0	7	51	0	False	2017-05-12 21:22:14.000000 UTC	N/A	Disabled
1956	1636	ctfmon.exe	0x82231da0	1	86	0	False	2017-05-12 21:22:14.000000 UTC	N/A	Disabled
260	664	svchost.exe	0x81fb95d8	5	105	0	False	2017-05-12 21:22:18.000000 UTC	N/A	Disabled
740	1940	@WanaDecryptor@	0x81fde308	2	70	0	False	2017-05-12 21:22:22.000000 UTC	N/A	Disabled
1768	1024	wuauclt.exe	0x81f747c0	7	132	0	False	2017-05-12 21:22:52.000000 UTC	N/A	Disabled
544	664	alg.exe	0x82010020	6	101	0	False	2017-05-12 21:22:55.000000 UTC	N/A	Disabled
1168	1024	wscntfy.exe	0x81fea8a0	1	37	0	False	2017-05-12 21:22:56.000000 UTC	N/A	Disabled
```

Notes

- explorer.exe started tasksche.exe which started @WanaDecryptor@
  - 1940 1636 tasksche.exe 0x82218da0 7 51 0 False 2017-05-12 21:22:14.000000 UTC N/A Disabled
  - 740 1940 @WanaDecryptor@ 0x81fde308 2 70 0 False 2017-05-12 21:22:22.000000 UTC N/A Disabled
  - 1636 1608 explorer.exe 0x821d9da0 11 331 0 False 2017-05-12 21:22:10.000000 UTC N/A Disabled
- tasksche.exe is not a legitimate Windows process, though it looks similar to taskschd.exe which is legitimate. Disguise attempt

```
> vol --file=wcry.raw windows.pstree
Volatility 3 Framework 2.26.2
Progress:  100.00		PDB scanning finished
PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime	Audit	Cmd	Path

4	0	System	0x823c8830	51	244	N/A	False	N/A	N/A	-	-	-
* 348	4	smss.exe	0x82169020	3	19	N/A	False	2017-05-12 21:21:55.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\smss.exe	\SystemRoot\System32\smss.exe	\SystemRoot\System32\smss.exe
** 620	348	winlogon.exe	0x8216e020	23	536	0	False	2017-05-12 21:22:01.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\winlogon.exe	winlogon.exe	\??\C:\WINDOWS\system32\winlogon.exe
*** 664	620	services.exe	0x821937f0	15	265	0	False	2017-05-12 21:22:01.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\services.exe	C:\WINDOWS\system32\services.exe	C:\WINDOWS\system32\services.exe
**** 1024	664	svchost.exe	0x821af7e8	79	1366	0	False	2017-05-12 21:22:03.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\svchost.exe	C:\WINDOWS\System32\svchost.exe -k netsvcs	C:\WINDOWS\System32\svchost.exe
***** 1768	1024	wuauclt.exe	0x81f747c0	7	132	0	False	2017-05-12 21:22:52.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\wuauclt.exe	"C:\WINDOWS\system32\wuauclt.exe" /RunStoreAsComServer Local\[400]SUSDS81a6658cb72fa845814e75cca9a42bf2	C:\WINDOWS\system32\wuauclt.exe
***** 1168	1024	wscntfy.exe	0x81fea8a0	1	37	0	False	2017-05-12 21:22:56.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\wscntfy.exe	C:\WINDOWS\system32\wscntfy.exe	C:\WINDOWS\system32\wscntfy.exe
**** 1152	664	svchost.exe	0x821bea78	10	173	0	False	2017-05-12 21:22:06.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\svchost.exe	C:\WINDOWS\system32\svchost.exe -k LocalService	C:\WINDOWS\system32\svchost.exe
**** 544	664	alg.exe	0x82010020	6	101	0	False	2017-05-12 21:22:55.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\alg.exe	C:\WINDOWS\System32\alg.exe	C:\WINDOWS\System32\alg.exe
**** 836	664	svchost.exe	0x8221a2c0	19	211	0	False	2017-05-12 21:22:02.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\svchost.exe	C:\WINDOWS\system32\svchost -k DcomLaunch	C:\WINDOWS\system32\svchost.exe
**** 260	664	svchost.exe	0x81fb95d8	5	105	0	False	2017-05-12 21:22:18.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\svchost.exe	C:\WINDOWS\system32\svchost.exe -k LocalService	C:\WINDOWS\system32\svchost.exe
**** 904	664	svchost.exe	0x821b5230	9	227	0	False	2017-05-12 21:22:03.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\svchost.exe	C:\WINDOWS\system32\svchost -k rpcss	C:\WINDOWS\system32\svchost.exe
**** 1484	664	spoolsv.exe	0x821e2da0	14	124	0	False	2017-05-12 21:22:09.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\spoolsv.exe	C:\WINDOWS\system32\spoolsv.exe	C:\WINDOWS\system32\spoolsv.exe
**** 1084	664	svchost.exe	0x8203b7a8	6	72	0	False	2017-05-12 21:22:03.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\svchost.exe	C:\WINDOWS\system32\svchost.exe -k NetworkService	C:\WINDOWS\system32\svchost.exe
*** 676	620	lsass.exe	0x82191658	23	353	0	False	2017-05-12 21:22:01.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\lsass.exe	C:\WINDOWS\system32\lsass.exe	C:\WINDOWS\system32\lsass.exe
** 596	348	csrss.exe	0x82161da0	12	352	0	False	2017-05-12 21:22:00.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\csrss.exe	C:\WINDOWS\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,3072,512 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitialization,2 ProfileControl=Off MaxRequestThreads=16	\??\C:\WINDOWS\system32\csrss.exe
1636	1608	explorer.exe	0x821d9da0	11	331	0	False	2017-05-12 21:22:10.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\explorer.exe	C:\WINDOWS\Explorer.EXE	C:\WINDOWS\Explorer.EXE
* 1956	1636	ctfmon.exe	0x82231da0	1	86	0	False	2017-05-12 21:22:14.000000 UTC	N/A	\Device\HarddiskVolume1\WINDOWS\system32\ctfmon.exe	"C:\WINDOWS\system32\ctfmon.exe" 	C:\WINDOWS\system32\ctfmon.exe
* 1940	1636	tasksche.exe	0x82218da0	7	51	0	False	2017-05-12 21:22:14.000000 UTC	N/A	\Device\HarddiskVolume1\Intel\ivecuqmanpnirkt615\tasksche.exe	"C:\Intel\ivecuqmanpnirkt615\tasksche.exe" 	C:\Intel\ivecuqmanpnirkt615\tasksche.exe
** 740	1940	@WanaDecryptor@	0x81fde308	2	70	0	False	2017-05-12 21:22:22.000000 UTC	N/A	\Device\HarddiskVolume1\Intel\ivecuqmanpnirkt615\@WanaDecryptor@.exe	@WanaDecryptor@.exe	C:\Intel\ivecuqmanpnirkt615\@WanaDecryptor@.exe
 ~/cs6445-25t3/week04  main ?1                                                                                                                                                       11:03:25 AM
```

Notes

- Malware executables live in \Device\HarddiskVolume1\Intel directory, probably made to appear like a driver or system update

```
> vol --file=wcry.raw windows.psscan
Volatility 3 Framework 2.26.2
Progress:  100.00		PDB scanning finished
PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime	File output

860	1940	taskdl.exe	0x1f4daf0	0	-	0	False	2017-05-12 21:26:23.000000 UTC	2017-05-12 21:26:23.000000 UTC	Disabled
536	1940	taskse.exe	0x1f53d18	0	-	0	False	2017-05-12 21:26:22.000000 UTC	2017-05-12 21:26:23.000000 UTC	Disabled
424	1940	@WanaDecryptor@	0x1f69b50	0	-	0	False	2017-05-12 21:25:52.000000 UTC	2017-05-12 21:25:53.000000 UTC	Disabled
1768	1024	wuauclt.exe	0x1f747c0	7	132	0	False	2017-05-12 21:22:52.000000 UTC	N/A	Disabled
576	1940	@WanaDecryptor@	0x1f8ba58	0	-	0	False	2017-05-12 21:26:22.000000 UTC	2017-05-12 21:26:23.000000 UTC	Disabled
260	664	svchost.exe	0x1fb95d8	5	105	0	False	2017-05-12 21:22:18.000000 UTC	N/A	Disabled
740	1940	@WanaDecryptor@	0x1fde308	2	70	0	False	2017-05-12 21:22:22.000000 UTC	N/A	Disabled
1168	1024	wscntfy.exe	0x1fea8a0	1	37	0	False	2017-05-12 21:22:56.000000 UTC	N/A	Disabled
544	664	alg.exe	0x2010020	6	101	0	False	2017-05-12 21:22:55.000000 UTC	N/A	Disabled
1084	664	svchost.exe	0x203b7a8	6	72	0	False	2017-05-12 21:22:03.000000 UTC	N/A	Disabled
596	348	csrss.exe	0x2161da0	12	352	0	False	2017-05-12 21:22:00.000000 UTC	N/A	Disabled
348	4	smss.exe	0x2169020	3	19	N/A	False	2017-05-12 21:21:55.000000 UTC	N/A	Disabled
620	348	winlogon.exe	0x216e020	23	536	0	False	2017-05-12 21:22:01.000000 UTC	N/A	Disabled
676	620	lsass.exe	0x2191658	23	353	0	False	2017-05-12 21:22:01.000000 UTC	N/A	Disabled
664	620	services.exe	0x21937f0	15	265	0	False	2017-05-12 21:22:01.000000 UTC	N/A	Disabled
1024	664	svchost.exe	0x21af7e8	79	1366	0	False	2017-05-12 21:22:03.000000 UTC	N/A	Disabled
904	664	svchost.exe	0x21b5230	9	227	0	False	2017-05-12 21:22:03.000000 UTC	N/A	Disabled
1152	664	svchost.exe	0x21bea78	10	173	0	False	2017-05-12 21:22:06.000000 UTC	N/A	Disabled
1636	1608	explorer.exe	0x21d9da0	11	331	0	False	2017-05-12 21:22:10.000000 UTC	N/A	Disabled
1484	664	spoolsv.exe	0x21e2da0	14	124	0	False	2017-05-12 21:22:09.000000 UTC	N/A	Disabled
1940	1636	tasksche.exe	0x2218da0	7	51	0	False	2017-05-12 21:22:14.000000 UTC	N/A	Disabled
836	664	svchost.exe	0x221a2c0	19	211	0	False	2017-05-12 21:22:02.000000 UTC	N/A	Disabled
1956	1636	ctfmon.exe	0x2231da0	1	86	0	False	2017-05-12 21:22:14.000000 UTC	N/A	Disabled
4	0	System	0x23c8830	51	244	N/A	False	N/A	N/A	Disabled
```

Notes

- psscan finds hidden processes not present in the process linked list OS data structure
  - processes may have terminated, but still have residue in RAM (don't get zero'd out)
- More malware executables found taskdl.exe and taskse.exe
  Additional malicious executables found:
- Another instance of @WanaDecryptor@, probably for persistence or restart

See a command history using `windows.cmdline`

```
> vol --file=wcry.raw windows.cmdline
Volatility 3 Framework 2.26.2
Progress:  100.00		PDB scanning finished
PID	Process	Args

4	System	-
348	smss.exe	\SystemRoot\System32\smss.exe
596	csrss.exe	C:\WINDOWS\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,3072,512 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitialization,2 ProfileControl=Off MaxRequestThreads=16
620	winlogon.exe	winlogon.exe
664	services.exe	C:\WINDOWS\system32\services.exe
676	lsass.exe	C:\WINDOWS\system32\lsass.exe
836	svchost.exe	C:\WINDOWS\system32\svchost -k DcomLaunch
904	svchost.exe	C:\WINDOWS\system32\svchost -k rpcss
1024	svchost.exe	C:\WINDOWS\System32\svchost.exe -k netsvcs
1084	svchost.exe	C:\WINDOWS\system32\svchost.exe -k NetworkService
1152	svchost.exe	C:\WINDOWS\system32\svchost.exe -k LocalService
1484	spoolsv.exe	C:\WINDOWS\system32\spoolsv.exe
1636	explorer.exe	C:\WINDOWS\Explorer.EXE
1940	tasksche.exe	"C:\Intel\ivecuqmanpnirkt615\tasksche.exe"
1956	ctfmon.exe	"C:\WINDOWS\system32\ctfmon.exe"
260	svchost.exe	C:\WINDOWS\system32\svchost.exe -k LocalService
740	@WanaDecryptor@	@WanaDecryptor@.exe
1768	wuauclt.exe	"C:\WINDOWS\system32\wuauclt.exe" /RunStoreAsComServer Local\[400]SUSDS81a6658cb72fa845814e75cca9a42bf2
544	alg.exe	C:\WINDOWS\System32\alg.exe
1168	wscntfy.exe	C:\WINDOWS\system32\wscntfy.exe
```

See DLLs used by the malware using `windows.dlllist --pid=<pid>`. Maybe you can get some idea what the malware does.

```
> vol --file=wcry.raw windows.dlllist --pid=740
Volatility 3 Framework 2.26.2
Progress:  100.00		PDB scanning finished
PID	Process	Base	Size	Name	Path	LoadTime	File output

740	@WanaDecryptor@	0x400000	0x3d000	@WanaDecryptor@.exe	C:\Intel\ivecuqmanpnirkt615\@WanaDecryptor@.exe	N/A	Disabled
740	@WanaDecryptor@	0x7c900000	0xb2000	ntdll.dll	C:\WINDOWS\system32\ntdll.dll	N/A	Disabled
740	@WanaDecryptor@	0x7c800000	0xf6000	kernel32.dll	C:\WINDOWS\system32\kernel32.dll	N/A	Disabled
740	@WanaDecryptor@	0x73dd0000	0xf2000	MFC42.DLL	C:\WINDOWS\system32\MFC42.DLL	N/A	Disabled
740	@WanaDecryptor@	0x77c10000	0x58000	msvcrt.dll	C:\WINDOWS\system32\msvcrt.dll	N/A	Disabled
740	@WanaDecryptor@	0x77f10000	0x49000	GDI32.dll	C:\WINDOWS\system32\GDI32.dll	N/A	Disabled
740	@WanaDecryptor@	0x7e410000	0x91000	USER32.dll	C:\WINDOWS\system32\USER32.dll	N/A	Disabled
740	@WanaDecryptor@	0x77dd0000	0x9b000	ADVAPI32.dll	C:\WINDOWS\system32\ADVAPI32.dll	N/A	Disabled
740	@WanaDecryptor@	0x77e70000	0x93000	RPCRT4.dll	C:\WINDOWS\system32\RPCRT4.dll	N/A	Disabled
740	@WanaDecryptor@	0x77fe0000	0x11000	Secur32.dll	C:\WINDOWS\system32\Secur32.dll	N/A	Disabled
740	@WanaDecryptor@	0x7c9c0000	0x818000	SHELL32.dll	C:\WINDOWS\system32\SHELL32.dll	N/A	Disabled
740	@WanaDecryptor@	0x77f60000	0x76000	SHLWAPI.dll	C:\WINDOWS\system32\SHLWAPI.dll	N/A	Disabled
740	@WanaDecryptor@	0x773d0000	0x103000	COMCTL32.dll	C:\WINDOWS\WinSxS\X86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.6028_x-ww_61e65202\COMCTL32.dll	N/A	Disabled
740	@WanaDecryptor@	0x77120000	0x8b000	OLEAUT32.dll	C:\WINDOWS\system32\OLEAUT32.dll	N/A	Disabled
740	@WanaDecryptor@	0x774e0000	0x13e000	ole32.dll	C:\WINDOWS\system32\ole32.dll	N/A	Disabled
740	@WanaDecryptor@	0x78130000	0x134000	urlmon.dll	C:\WINDOWS\system32\urlmon.dll	N/A	Disabled
740	@WanaDecryptor@	0x3dfd0000	0x1ec000	iertutil.dll	C:\WINDOWS\system32\iertutil.dll	N/A	Disabled
740	@WanaDecryptor@	0x76080000	0x65000	MSVCP60.dll	C:\WINDOWS\system32\MSVCP60.dll	N/A	Disabled
740	@WanaDecryptor@	0x71ab0000	0x17000	WS2_32.dll	C:\WINDOWS\system32\WS2_32.dll	N/A	Disabled
740	@WanaDecryptor@	0x71aa0000	0x8000	WS2HELP.dll	C:\WINDOWS\system32\WS2HELP.dll	N/A	Disabled
740	@WanaDecryptor@	0x3d930000	0xe7000	WININET.dll	C:\WINDOWS\system32\WININET.dll	N/A	Disabled
740	@WanaDecryptor@	0x340000	0x9000	Normaliz.dll	C:\WINDOWS\system32\Normaliz.dll	N/A	Disabled
740	@WanaDecryptor@	0x76390000	0x1d000	IMM32.DLL	C:\WINDOWS\system32\IMM32.DLL	N/A	Disabled
740	@WanaDecryptor@	0x629c0000	0x9000	LPK.DLL	C:\WINDOWS\system32\LPK.DLL	N/A	Disabled
740	@WanaDecryptor@	0x74d90000	0x6b000	USP10.dll	C:\WINDOWS\system32\USP10.dll	N/A	Disabled
740	@WanaDecryptor@	0x732e0000	0x5000	RICHED32.DLL	C:\WINDOWS\system32\RICHED32.DLL	N/A	Disabled
740	@WanaDecryptor@	0x74e30000	0x6d000	RICHED20.dll	C:\WINDOWS\system32\RICHED20.dll	N/A	Disabled
740	@WanaDecryptor@	0x5ad70000	0x38000	uxtheme.dll	C:\WINDOWS\system32\uxtheme.dll	N/A	Disabled
740	@WanaDecryptor@	0x74720000	0x4c000	MSCTF.dll	C:\WINDOWS\system32\MSCTF.dll	N/A	Disabled
740	@WanaDecryptor@	0x755c0000	0x2e000	msctfime.ime	C:\WINDOWS\system32\msctfime.ime	N/A	Disabled
740	@WanaDecryptor@	0x769c0000	0xb4000	USERENV.dll	C:\WINDOWS\system32\USERENV.dll	N/A	Disabled
740	@WanaDecryptor@	0xea0000	0x29000	msls31.dll	C:\WINDOWS\system32\msls31.dll	N/A	Disabled

```

Student questions:
Q: Can you find boot time on Windows using volatility?
A: As far as I can tell there's no simple way to do this (no equivalent to Volatility's `linux.boottime`). But to get a (probably quite accurate) estimate of the system boot time you can run `windows.pslist`/`windows.psscan` and find the process with the earliest `CreateTime`. For example, in the wcry.raw memory image, this is the smss.exe process (Session Manager on Windows, started at boot time):

```
> vol --file=wcry.raw windows.psscan
Volatility 3 Framework 2.26.2
Progress:  100.00		PDB scanning finished
PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime	File output

860	1940	taskdl.exe	0x1f4daf0	0	-	0	False	2017-05-12 21:26:23.000000 UTC	2017-05-12 21:26:23.000000 UTC	Disabled
536	1940	taskse.exe	0x1f53d18	0	-	0	False	2017-05-12 21:26:22.000000 UTC	2017-05-12 21:26:23.000000 UTC	Disabled
424	1940	@WanaDecryptor@	0x1f69b50	0	-	0	False	2017-05-12 21:25:52.000000 UTC	2017-05-12 21:25:53.000000 UTC	Disabled
1768	1024	wuauclt.exe	0x1f747c0	7	132	0	False	2017-05-12 21:22:52.000000 UTC	N/A	Disabled
576	1940	@WanaDecryptor@	0x1f8ba58	0	-	0	False	2017-05-12 21:26:22.000000 UTC	2017-05-12 21:26:23.000000 UTC	Disabled
260	664	svchost.exe	0x1fb95d8	5	105	0	False	2017-05-12 21:22:18.000000 UTC	N/A	Disabled
740	1940	@WanaDecryptor@	0x1fde308	2	70	0	False	2017-05-12 21:22:22.000000 UTC	N/A	Disabled
1168	1024	wscntfy.exe	0x1fea8a0	1	37	0	False	2017-05-12 21:22:56.000000 UTC	N/A	Disabled
544	664	alg.exe	0x2010020	6	101	0	False	2017-05-12 21:22:55.000000 UTC	N/A	Disabled
1084	664	svchost.exe	0x203b7a8	6	72	0	False	2017-05-12 21:22:03.000000 UTC	N/A	Disabled
596	348	csrss.exe	0x2161da0	12	352	0	False	2017-05-12 21:22:00.000000 UTC	N/A	Disabled
348	4	smss.exe	0x2169020	3	19	N/A	False	2017-05-12 21:21:55.000000 UTC	N/A	Disabled <======= You can use this earliest CreateTime as a boot time estimate
620	348	winlogon.exe	0x216e020	23	536	0	False	2017-05-12 21:22:01.000000 UTC	N/A	Disabled
676	620	lsass.exe	0x2191658	23	353	0	False	2017-05-12 21:22:01.000000 UTC	N/A	Disabled
664	620	services.exe	0x21937f0	15	265	0	False	2017-05-12 21:22:01.000000 UTC	N/A	Disabled
1024	664	svchost.exe	0x21af7e8	79	1366	0	False	2017-05-12 21:22:03.000000 UTC	N/A	Disabled
904	664	svchost.exe	0x21b5230	9	227	0	False	2017-05-12 21:22:03.000000 UTC	N/A	Disabled
1152	664	svchost.exe	0x21bea78	10	173	0	False	2017-05-12 21:22:06.000000 UTC	N/A	Disabled
1636	1608	explorer.exe	0x21d9da0	11	331	0	False	2017-05-12 21:22:10.000000 UTC	N/A	Disabled
1484	664	spoolsv.exe	0x21e2da0	14	124	0	False	2017-05-12 21:22:09.000000 UTC	N/A	Disabled
1940	1636	tasksche.exe	0x2218da0	7	51	0	False	2017-05-12 21:22:14.000000 UTC	N/A	Disabled
836	664	svchost.exe	0x221a2c0	19	211	0	False	2017-05-12 21:22:02.000000 UTC	N/A	Disabled
1956	1636	ctfmon.exe	0x2231da0	1	86	0	False	2017-05-12 21:22:14.000000 UTC	N/A	Disabled
4	0	System	0x23c8830	51	244	N/A	False	N/A	N/A	Disabled
```
