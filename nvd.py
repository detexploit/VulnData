###########################################################
# nvd.py
# Data gathering / re-formatting script for NVD Vulnerbility Information
# VulnData (https://github.com/moppoi5168/VulnData)
# Licensed by GPL License
###########################################################

import datetime
import glob
import json
import os
import subprocess
import urllib.request
import zipfile

product_dict = {}


def main():
    print('[nvd.py] Gathering latest vulnerability data ......')
    year = datetime.date.today().year
    newestfile = 'nvdcve-1.0-' + str(year) + '.json'
    os.remove('NVD/' + newestfile)
    url = 'https://nvd.nist.gov/feeds/json/cve/1.0/' + newestfile + '.zip'
    saveas = 'tmp.zip'
    urllib.request.urlretrieve(url, saveas)
    with zipfile.ZipFile('tmp.zip') as existing_zip:
        existing_zip.extractall('NVD/')
    os.remove('tmp.zip')
    print('[nvd.py] Re-formatting the vulnerability data ......')
    files = glob.glob(os.path.join('./NVD','*.json'))
    for file in files:
        pd = {}
        nowyear = file[17:-5]
        with open(file, mode='r', errors='replace') as jf:
            json_dict = json.load(jf)
            cve_list = json_dict['CVE_Items']
            for x in cve_list:
                for y in x['cve']['affects']['vendor']['vendor_data']:
                    for z in y['product']['product_data']:
                        app_name = z['product_name']
                        for i in z['version']['version_data']:
                            app_version = i['version_value']
                            pd[app_name] = app_version
        product_dict[nowyear] = pd
    year_list = range(2002, year + 1)
    print('[nvd.py] Writing the re-formatted data to ./NVD-DETEXPLOIT/??.detexploit ......')
    for pdata in product_dict:
        pd = product_dict[pdata]
        with open('./NVD-DETEXPLOIT/NVDVULN_' + pdata + '.detexploit', mode='w') as f:
            pload = ''
            for p in pd:
                app_name = p
                app_version = pd[p]
                pload = pload + app_name + '/,/,/,/' + app_version + '\n'
            f.write(pload)
    print('[nvd.py] Pushing files into GitHub Remote Repository ......')
    subprocess.Popen(r'git add *', stdout=subprocess.PIPE, shell=True)
    subprocess.Popen(r'git commit -m "Daily Data Update"', stdout=subprocess.PIPE, shell=True)
    subprocess.Popen(r'git push origin master', stdout=subprocess.PIPE, shell=True)


if __name__ == "__main__":
    main()
