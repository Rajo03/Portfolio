from bs4 import BeautifulSoup
import requests
import time
import sys



try:
    page = requests.get('https://www.amazon.pl/Garmin-Fenix-multisportowy-zegarek-czarny/dp/B07W2Z2ZS1?ref_=Oct_d_obs_d_20788343031&pd_rd_w=Qw1OR&pf_rd_p=f3c0087e-c101-4b01-8657-8ee971af1154&pf_rd_r=PKHPCZGA4WW4192F8RRE&pd_rd_r=8bd5f171-8878-4ce1-9f33-8d5eb4625bb2&pd_rd_wg=oZ5tp&pd_rd_i=B07W2Z2ZS1')
    
except Exception as e:
    error_type, error_obj, error_info = sys.exc_info()
    print ('error')
    print (error_type, 'line', error_info.tb_lineo)
    
time.sleep(1)

soup = BeautifulSoup(page.text,'html.parser')
links = soup.find_all('span',attrs={'class':'_p13n-desktop-sims-fbt_price_p13n-sc-price__bCZQt'})

page

links

for i in links:
    print (i.text)
    print("\n")