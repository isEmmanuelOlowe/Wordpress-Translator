# How to use `Wordpress_Translate.py`

## About

 A python script to translate all Wordpress posts using GoogleTrans. 

## Prerequisites 

**First you must install python 3. The download link and full installation instructions are available of https://www.python.org/**

**After install you must navigate to command prompt on windows.**

![1528909159851](C:\Users\JANET4~1\AppData\Local\Temp\1528909159851.png)

**open the command prompt and then enter the commands**

```bash
pip install googletrans
```

```bash
pip install python-wordpress-xmlrpc
```

## Now you are able to run script

![1528909626585](C:\Users\JANET4~1\AppData\Local\Temp\1528909626585.png)

Now you can run the script by just double clicking file.

## Input

### URL

The URL is the link to website from homepage. e.g. www.google.com (without a slash)

### Username and Password

The username and password of admin of Wordpress site

### Language Codes

Each language has a corresponding language code which is used to reference it in the program. 

| Afrikaans |
| --------- |
| af        |

| Albanian |
| -------- |
| sq       |

| Arabic 	ar |
| ------------- |
| ar            |

| Belarusian |
| ---------- |
| be         |

| Bulgarian |
| --------- |
| bg        |

| Catalan |
| ------- |
| ca      |

| Chinese Simplified |
| ------------------ |
| zh-CN              |

| Chinese Traditional |
| ------------------- |
| zh-TW               |

| Croatian |
| -------- |
| hr       |

| Czech |
| ----- |
| cs    |

| Danish |
| ------ |
| da     |

| Dutch |
| ----- |
| nl    |

| English |
| ------- |
| en      |

| Estonian |
| -------- |
| et       |

| Filipino |
| -------- |
| tl       |

| Finnish |
| ------- |
| fi      |

| French |
| ------ |
| fr     |

| Galician |
| -------- |
| gl       |

| German |
| ------ |
| de     |

| Greek |
| ----- |
| el    |

| Hebrew |
| ------ |
| iw     |

| Hindi |
| ----- |
| hi    |

| Hungarian |
| --------- |
| hu        |

| Icelandic |
| --------- |
| is        |

| Indonesian |
| ---------- |
| id         |

| Irish |
| ----- |
| ga    |

| Italian |
| ------- |
| it      |

| Japanese |
| -------- |
| ja       |

| Korean |
| ------ |
| ko     |

| Latvian |
| ------- |
| lv      |

| Lithuanian |
| ---------- |
| lt         |

| Macedonian |
| ---------- |
| mk         |

| Malay |
| ----- |
| ms    |

| Maltese |
| ------- |
| mt      |

| Norwegian |
| --------- |
| no        |

| Persian |
| ------- |
| fa      |

| Polish |
| ------ |
| pl     |

| Portuguese |
| ---------- |
| pt         |

| Romanian |
| -------- |
| ro       |

| Russian |
| ------- |
| ru      |

| Serbian |
| ------- |
| sr      |

| Slovak |
| ------ |
| sk     |

| Slovenian |
| --------- |
| sl        |

| Spanish |
| ------- |
| es      |

| Swahili |
| ------- |
| sw      |

| Swedish |
| ------- |
| sv      |

| Thai |
| ---- |
| th   |

| Turkish |
| ------- |
| tr      |

| Ukrainian |
| --------- |
| uk        |

| Vietnamese |
| ---------- |
| vi         |

| Welsh |
| ----- |
| cy    |

| Yiddish |
| ------- |
| yi      |

When asked for language of page enter the language of page. When asked for desired language to translate to enter language code of language you want to translate to.

## Done

Now you can wait back and wait for script to finish.

## Errors

If some posts are unable to be translated. The part of the post which cause the error will be printed in terminal (if ran from terminal) or available in CSV file.