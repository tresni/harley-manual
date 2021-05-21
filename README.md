# Harley Davidson Automatic Manual Downloader

I wanted to get an owner's manual for my wife's new bike (2003 883 Sportster), but was unable to find a digital version anywhere.  Harley Davidson does offer manuals online, but most of them are only navigable on their website and not offered as a single PDF download.

To create an owners manual, we go through all the available links on the manual page and download the associated PDFs, combines them into a single document, and saves that to disk.

## Requirements

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [progress](https://github.com/verigak/progress/)
* [PyPDF2](https://pythonhosted.org/PyPDF2/)
* [requests](https://docs.python-requests.org/en/master/)

## Install

```
$ pip install https://github.com/tresni/harley-manual/archive/refs/heads/main.zip
```

## Usage

Find the manual you want at https://serviceinfo.harley-davidson.com/ .  When on the manual page (e.g. https://serviceinfo.harley-davidson.com/sip/content/document/view?id=90016 ), copy the URL or just the `id` number.

```
$ harley-manual https://serviceinfo.harley-davidson.com/sip/content/document/view?id=90016
```
or
```
$ harley-manual 90016
```

Some manuals are offered as single PDF documents already (e.g. 90024.)  In that case, `harley-manual` will download that PDF to disk without error.
