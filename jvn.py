###########################################################
# jvn.py
# Data gathering / re-formatting script for JVN Vulnerbility Information
# VulnData (https://github.com/moppoi5168/VulnData)
# Licensed by GPL License
###########################################################

from html.parser import HTMLParser

import glob
import os
import tqdm
import urllib.request
import xml.etree.ElementTree as ET

vulnid = []


class html_parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)


    def handle_starttag(self, tag, attrs):
        if tag == "sec:references":
            attrs = dict(attrs)
            if 'source' in attrs and 'id' in attrs:
                if attrs['source'] == 'JVN iPedia':
                    vulnid.append(attrs['id'])


def main():
    print('[jvn.py] Gathering latest vulnerability data ......', end='\n\n')
    year_list = range(1998, 2020)
    month_list = range(1, 13)
    for year in year_list:
        for month in tqdm.tqdm(month_list, desc=str(year)):
            url = 'https://jvndb.jvn.jp/myjvn?method=getVulnOverviewList&feed=hnd&rangeDatePublished=n&rangeDateFirstPublished=n&datePublicStartY=' + str(year) + '&datePublicStartM=' + str(month) + '&datePublicEmdY=' + str(year) + '&datePublicEmdM=' + str(month)
            mem = urllib.request.urlopen(url).read().decode()
            tmp = mem.split('\n')
            parser = html_parser()
            for line in tmp:
                parser.feed(line)



if __name__ == "__main__":
    main()
