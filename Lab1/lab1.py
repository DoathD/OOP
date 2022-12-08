from operator import attrgetter
from Lab1.country import *

FILENAME = r".\\output_file.txt"
NUM_COUNTRY = 13

list_country = list(range(0,NUM_COUNTRY))

list_country[0] = Country("Russia",145.478,1820,17098246)
list_country[1] = Country("Belgium",11.521,619,30528)
list_country[2] = Country("USA",301.693,21433,9826675)
list_country[3] = Country("China",1410.539,18100,9596961)
list_country[4] = Country("France",68.084,2551,643801)
list_country[5] = Country("GreatBritain",67.081,3376,242495)
list_country[6] = Country("Germany",83.695,4672,357578)
list_country[7] = Country("Italy",58.983,1848,302073)
list_country[8] = Country("Canada",38.929,2016,9984670)
list_country[9] = Country("Kazakhstan",19.644,207,2724902)
list_country[10] = Country("Japan",125.440,5080,377975)
list_country[11] = Country("SouthKorea",51.744,1804,100210)
list_country[12] = Country("NorthKorea",26.111,17,120540)
print(*list_country)

print("Сортировка по имени")
list_country.sort(key=attrgetter('name'))
print(*list_country)

print("Сортировка по численности населения")
list_country.sort(key=attrgetter('population'))
print(*list_country)

with open(FILENAME, "w", encoding="utf8") as file:
    [file.write(str(list_country[i])) for i in range(len(list_country))]
