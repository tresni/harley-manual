# Harley Davidson Automatic Manual Downloader

I wanted to get an owner's manual for my wife's new bike (2003 883 Sportster), but was unable to find a digital version anywhere.  Harley Davidson does offer manuals online, but most of them are only navigable on their website and not offered as a single PDF download.

To create an owners manual, we go through all the available links on the manual page and download the associated PDFs, combines them into a single document, and saves that to disk.

## Requirements

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [progress](https://github.com/verigak/progress/)
* [PyPDF2](https://pythonhosted.org/PyPDF2/)
* [requests](https://docs.python-requests.org/en/master/)