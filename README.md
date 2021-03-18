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
## human2machine	

> Long long time ago, there were a programmers like Neo	[card.png](files/card.png)
> **ALIMCTF(TRINITY_KEYPUNCH)**
## Xeon not found	

> Neo doesnt know key from Xeon	[xeon.py](files/xeon.py)	
> **alimCTF{n30_d03s_n0t_kn0w_pyth0n}**
## vedroid

> Meet the Rick, he lives in Matrix too	[alimCTF2021.apk](files/alimCTF2021.apk)	
> **alimCTF{the_best_app_the_w0rld}**
## to turst or not to trust	

> In God we trust	[notrust.png](files/notrust.png)	
> **alimCTF{trust_n0_0n3_1n_the_w3b}**
## snow	

> password is 1234	[letitsnow.txt](files/letitsnow.txt)	
> **alimCTF{im_going_to_enjoy_watching_you_die_mr_anderson}**
## last strike beat	

> Press L to win	[fight.png](files/fight.png)	
> **alimCTF{deus_ex_machina}**
## procrastinate	

> Skip skip pause skip	[youtubify.gif](files/youtubify.gif)	
> **alimCTF{w@snt_that_fun}**
## mine or yours	

> alim.alatoo.edu.kg:25565		
> **alimCTF{dont_stop_mining}**
## garbage collector	

> nc alim.alatoo.edu.kg 4711		
> **alimCTF{netcat_is_beast}**
## printerr	

> Nebuchadnezzar has one important detail broken and the only way to fix it is to be 3d printed, but it seems to be oken transfered	[3dr.pint.stl](files/3dr.pint.stl)	
> **alimCTF{stereolithography}**

## follow the horse	

> Agents are searching for that person we should find her first here is what we have 人们还能笑的时候，是不容易被打败的。. Find  ip [screenshot.png](files/screenshot.png)
> **alimCTF{39.108.11.206}**

## double trouble	

> My fear is 46f153285194qo6s31gv3kc71oj59513393q86i8		
> **alimCTF{claustrophobia}**
## Ouch that hurts	

> Our memories	[track_magick.zip](files/track_magick.zip)	
> **alimCTF{Memorial_Hospital}**

