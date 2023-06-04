import requests
city = '@6801'
url = 'https://aqicn.org/feed' + city + '/?token='
api_key = 'b77d3aeca61a0cd899a2a90d6ea4219e72efdd5d'

main_url = url + api_key
r = requests.get(main_url)
data = r.json()['data']
aqi = data['aqi']
iaqi = data['iaqi']
dew = iaqi.get('dew','Nil')
no2 = iaqi.get('no2','Nil')
o3 = iaqi.get('o3','Nil')
so2 = iaqi.get('so2','Nil')
pm10 = iaqi.get('pm10','Nil')
pm25 = iaqi.get('pm25','Nil')
pollen = iaqi.get('pol','Nil')

print(f'{city}Jakość powietrza w Olesno:',aqi,'\n')
print('')
print('Dew :',dew['v'])
print('no2 :',no2['v'])
print('Ozone :',o3['v'])
print('sulphur :',so2['v'])
print('pm10 :',so2['v'])
print('pm25 :',pm25['v'])