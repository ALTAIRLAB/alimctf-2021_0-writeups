# alimctf-2021_0-writeups

Writeups for the first alimCTF-2021 http://alim.alatoo.edu.kg/ctf/ 

- [alimctf-2021_0-writeups](#alimctf-2021_0-writeups)
  - [the digits](#the-digits)
  - [Ceasar XIII](#ceasar-xiii)
  - [Neo's Room Number](#neos-room-number)
  - [Sing bird, please](#sing-bird-please)
  - [Neagents](#neagents)
  - [cryptable](#cryptable)
  - [mailto:matrix](#mailtomatrix)
  - [human2machine](#human2machine)
  - [Xeon not found](#xeon-not-found)
  - [vedroid](#vedroid)
  - [to turst or not to trust](#to-turst-or-not-to-trust)
  - [snow](#snow)
  - [last strike beat](#last-strike-beat)
  - [procrastinate](#procrastinate)
  - [mine or yours](#mine-or-yours)
  - [garbage collector](#garbage-collector)
  - [printerr](#printerr)
  - [follow the horse](#follow-the-horse)
  - [double trouble](#double-trouble)
  - [Ouch that hurts](#ouch-that-hurts)
## the digits

> The digits... what do they mean? 	[alphadigits.jpg](files/alphadigits.jpg)	
> **ALIMCTF{WAKEUPNEO}**	

Image has semi-transparent text which can be decoded by assigning latin letter for each number A - 1, B - 2...
## Ceasar XIII

> Mr.Anderson accepted strange SMS from unkown number: _nyvzPGS{oyhr_be_erq_cvyy}_	
> **alimCTF{blue_or_red_pill}**

One of easiest way to encode information - ROT13. Easiest way is to use https://rot13.com/ or any other analog.

## Neo's Room Number	

> Find Room number where Thomas A. Anderson lived and convert it to binary representation.		
> **alimCTF{1100101}**

This one is easy too. Googling Neo's room number we can find page https://matrix.fandom.com/wiki/Room_101 and convert it using any tool to binary representation.
## Sing bird, please	

> You hear birds but it is not real...	[auda_town.wav](files/auda_town.wav)	
> **alimCTF{link}**

If we try to listen wav file we cant hear any info that sounds like flag. But seems like there is a hint in the name of the file pointing to Audacity software. You can open file in Audacity and view its spectrogram.
## Neagents	

> catch them all before they catch you https://pteacher.github.io/WebProject		
> **alimCTF{th0mps0n_j0hns0n_j0n3s}**

Opening any Browser's inspector (CTRL+SHIFT+I) and searching for alimCTF will give you first part of flag. Next parts could be found inside css and js files' comments.
## cryptable	

> Trinity has recieved encrypted message XLHZSAYAVJT with the key WHOISCYPHER and some [table.txt](files/table.txt)
> **alimCTF{BETRAYALOFC}**

Using table as reference you can find the way to decode. Just find key symbol in row, for instance W and find
## mailto:matrix	

> Ding! You have an email!	[spam_omegaedgeoftomm.txt](files/spam_omegaedgeoftomm.txt)	
> **alimCTF{why_do_my_eyes_hurt}**

To solve this you can use http://spammimic.com/decode.shtml
## human2machine

> Long long time ago, there were a programmers like Neo	[card.png](files/card.png)
> **ALIMCTF(TRINITY_KEYPUNCH)**

This one is also can be solved using online tools https://www.masswerk.at/cardreader/ but you will have such result `\x2400\x1100\x2001\x1020\x2100\x0900\x2008\x2012\x0900\x1001\x2001\x1010\x2001\x0900\x0802\x0812\x1200\x2010\x0802\x1004\x0820\x1010\x2100\x2002\x1012`
which can be decoded using table 
```
A 2400    J 1400    / 0C00
B 2200    K 1200    S 0A00
C 2100    L 1100    T 0900
D 2020    M 1020    U 0820
E 2010    N 1010    V 0810
F 2008    O 1008    W 0808
G 2004    P 1004    X 0804
H 2002    Q 1002    Y 0802
I 2001    R 1001    Z 0801

¢ 2202    ! 1202              : 0202
. 2102    $ 1102    , 0902    # 0102
< 2022    * 1022    % 0822    @ 0022
( 2012    ) 1012    _ 0812    ' 0012
+ 200A    ; 100A    > 080A    = 000A
| 2006    ¬ 1006    ? 0806    " 0006
```

## Xeon not found	

> Neo doesnt know key from Xeon	[xeon.py](files/xeon.py)	
> **alimCTF{n30_d03s_n0t_kn0w_pyth0n}**

just opening file as text will give you flag parts
## vedroid

> Meet the Rick, he lives in Matrix too	[alimCTF2021.apk](files/alimCTF2021.apk)	
> **alimCTF{the_best_app_the_w0rld}**

one of the simplies ways is to use `strings` linux command. But first we need to extract everthing from apk to folder since it is an archive, then just use it on all files like `strings * | grep alimCTF` and you will see flag at the end.
## to turst or not to trust	

> In God we trust	[notrust.png](files/notrust.png)	
> **alimCTF{trust_n0_0n3_1n_the_w3b}**

lets check if file is archive, just rename it to have .zip extension
## snow	

> password is 1234	[letitsnow.txt](files/letitsnow.txt)	
> **alimCTF{im_going_to_enjoy_watching_you_die_mr_anderson}**

you can hide information using stagano method called snow. In linux it can be installed `sudo apt install stegsnow`. And then used `stegsnow -C -p "1234" letitsnow.txt`
## last strike beat	

> Press L to win	[fight.png](files/fight.png)	
> **alimCTF{deus_ex_machina}**

this flag can be revealed if you know what [LSB](https://www.boiteaklou.fr/Steganography-Least-Significant-Bit.html) (less significant bit) is. Also you can find flag using online tool https://stylesuxx.github.io/steganography/

## procrastinate

> Skip skip pause skip	[youtubify.gif](files/youtubify.gif)	
> **alimCTF{w@snt_that_fun}**

first lets extract all images from gif

```
mkdir img
convert youtubify.gif -coalesce img/%d.png
```

then we can write short python script to extract data from qr, asuming we already know that qr data are links to youtube videos we can extract thumbnail images and browse through them. Then we find that image 62 leads us to matrix styled youtube video.

```
import cv2
import requests
from io import BytesIO
from PIL import Image

for i in range(100):
	image = cv2.imread('img/' + str(i) + '.png')
	qrCodeDetector = cv2.QRCodeDetector()
	decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
	print()

	url = 'https://img.youtube.com/vi/' + decodedText[-11:] + '/1.jpg'
	response = requests.get(url)
	img = Image.open(BytesIO(response.content))
	img.save(str(i) + 'x.png')
```

## mine or yours	

> alim.alatoo.edu.kg:25565		
> **alimCTF{dont_stop_mining}**

main part is a port here which is used mainly by minecraft, then lets find out version of minecraft used on https://mcsrvstat.us/ after that you will face another problem with plugins need to installed on client side, but minecraft will give you a hint which one need to install. After you enter the game, you can start searching it. The flag was in cafeteria.
## garbage collector	

> nc alim.alatoo.edu.kg 4711		
> **alimCTF{netcat_is_beast}**

`nc alim.alatoo.edu.kg 4711 | grep alimCTF` will give you an answer, but not immediately, seems like it is not gonna appear after some amout of time ~ 1 minute. 
## printerr	

> Nebuchadnezzar has one important detail broken and the only way to fix it is to be 3d printed, but it seems to be oken transfered	[3dr.pint.stl](files/3dr.pint.stl)	
> **alimCTF{stereolithography}**

we have STL file which has been corrupted on purpose, if we open file with text editor we can see text file with data of coordinates, also we see that name of file has some hint insted of 3dp.rint we see 3dr.pint. We can try exchaning two digits around all dots. Like:

```
fin = open('3dr.pint.stl', 'r')
fout = open('fixed.stl', 'w')

for line in fin:
	r = [list(el) for el in line.split('.')]
	for i in range(len(r) - 1):
		r[i][-1], r[i + 1][0] = r[i + 1][0], r[i][-1]
	r = [''.join(el) for el in r]
	fout.write('.'.join(r))
fout.close()
```

## follow the horse	

> Agents are searching for that person we should find her first here is what we have 人们还能笑的时候，是不容易被打败的。. Find  ip [screenshot.png](files/screenshot.png)
> **alimCTF{39.108.11.206}**

use reverse image search and find the website, after you can find the ip using any tools.
## double trouble	

> My fear is 46f153285194qo6s31gv3kc71oj59513393q86i8		
> **alimCTF{claustrophobia}**

seems like text is SHA-1 encryption, which cannot be decrypted, but if someone used dictionary or any other widespread words then we can search this hashed (encrypted) password in bases. But seems it is not in base and title of task says that it is double trouble. Then we have to decrypt it using another method. 

Since the form of SHA-1 key is not changed it might be kind of substitution cipher (Ceasar, __Vigenere__, Hill, Atbash etc.) https://planetcalc.com/search/?tag=1204. Also some of cipher require key. We can assume that it was **alimctf**. Decrypting with Vigenere and passing that hash to SHA-1 hash base website (ex: https://md5decrypt.net/en/Sha1/) will give you an answer. This may sound as some kind of guessing, but you had enough of time to do it manually :D 
## Ouch that hurts	

> Our memories	[track_magick.zip](files/track_magick.zip)	
> **alimCTF{Memorial_Hospital}**

zip archive have some photos inside. Actually they say nothing, but photo can hide additional information. There are numerous ways to view it. One of them is using ImageMagick subtool: `identify -verbose <image.jpg>`. We can find coordinates in each of them. If we place them on any online map, we can see that ALIM text appears, but one dot is missing at the end. At this location you can find **Mermorial Hospital** (add underscore according to hint placeholder)

