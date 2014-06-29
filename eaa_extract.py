# JSON Creation for Edwards Aquifer Authority Levels
#
# Data Format:
#
# levels_current = Daily Readings
# levels_average = 10 Day Average
#
# Parameter 1:  Bexar J-17
# Parameter 2:  Uvalde J-27
# Parameter 3:  Comal Springs
# Parameter 4:  San Marcos Springs

from bs4 import BeautifulSoup
import urllib2
import json

EAA_URL = "http://data.edwardsaquifer.org/widget_conditions.php"

webinfo = urllib2.urlopen(EAA_URL).read()

soup = BeautifulSoup(webinfo)

leveltags = soup.find_all("td")

level_current = list()
level_average = list()

level_current.append(leveltags[5].get_text())
level_current.append(leveltags[8].get_text())
level_current.append(leveltags[11].get_text())
level_current.append(leveltags[14].get_text())

level_average.append(leveltags[6].get_text())
level_average.append(leveltags[9].get_text())
level_average.append(leveltags[12].get_text())
level_average.append(leveltags[15].get_text())

# Create JSON files

levels_json = '{"bexar" : {"cur": '+ level_current[0] + ', "avg": ' + level_average[0] + ' }, '
levels_json = levels_json + '"uvalde" : {"cur": '+ level_current[1] + ', "avg": ' + level_average[1] + ' }, '
levels_json = levels_json + '"comal" : {"cur": '+ level_current[2] + ', "avg": ' + level_average[2] + ' }, '
levels_json = levels_json + '"sanmarcos" : {"cur": '+ level_current[3] + ', "avg": ' + level_average[3] + ' }}'

json_output = open("aquifer-levels.json",'wb')
json_output.write(levels_json)
json_output.close()
