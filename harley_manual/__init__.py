#! /usr/bin/env python3

import argparse
from io import BytesIO
from math import ceil
from urllib.parse import parse_qs, urlparse

import PyPDF2
import requests
from bs4 import BeautifulSoup
from progress.bar import Bar


def merge_manual():
    base = "https://serviceinfo.harley-davidson.com"
    chunk = 4096
    urls = []
    r = requests.Session()

    parser = argparse.ArgumentParser("Harley Davidson Automatic Manual Downloader")
    parser.add_argument("manual", help="Either the URL to the manual or the manual id")
    args = parser.parse_args()

    try:
        manual = int(args.manual)
    except ValueError:  # should mean we have a URL
        manual = parse_qs(urlparse(args.manual).query).id

    response = r.get(f"{base}/sip/service/document/{manual}", stream=True)
    if response.status_code != requests.codes.ok:
        print(f"Unable to locate manual {manual}")
        return

    if response.headers.get("content-type") == "application/pdf":
        file_size = ceil(int(response.headers.get("content-length")) / chunk)
        with open(f"HD Manual {manual}.pdf", "wb") as fp:
            for content in Bar(
                "Downloading", max=file_size, suffix="ETA %(eta_td)s"
            ).iter(response.iter_content(chunk)):
                fp.write(content)
        return

    soup = BeautifulSoup(response.raw, "lxml")

    writer = PyPDF2.PdfFileMerger()
    links = soup.find_all("a", target="procedure-iframe")
    for link in Bar("Merging", suffix="ETA %(eta_td)s").iter(links):
        href = urlparse(link["href"])
        pdfurl = urlparse(parse_qs(href.query)["pdfUrl"][0]).path
        if pdfurl not in urls:
            response = r.get(f"{base}{pdfurl}")
            writer.append(BytesIO(response.content))
            urls.append(pdfurl)

    writer.write(f"HD Manual {manual}.pdf")


if __name__ == "__main__":
    merge_manual()
