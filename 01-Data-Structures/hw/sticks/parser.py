import numpy as np
import statistics
from collections import Counter


def jsParser(data):

    data = data[1:-2]
    data = data.replace('null', '"null"').replace('"', '').replace('Gew\\u00fcrztraminer', 'Gewurztraminer')
    data = data.split('}, ')

    wine_data = list()
    for vine in data:
        keys = []
        values = []
        vine = vine.split(', ')
        for characteristic in vine:
            characteristic = characteristic.replace('[', '').replace('{', '')
            for el in range(len(characteristic.split(': '))-1):
                    keys.append((characteristic.split(': ')[el]))
                    values.append((characteristic.split(': ')[el+1]))
        wine_data.append(dict(zip(keys, values)))

    return wine_data


def stats(variety: str, stast: dict):
    prices = []
    most_common_region = []
    most_common_country = []
    avarage_score = []
    for vine in winedata_full:
        if vine['variety'] == variety:
            if vine['price'] != 'null':
                prices.append(int(vine['price']))
            else:
                pass
            if vine['province'] != 'null':
                most_common_region.append(vine['province'])
            else:
                pass
            if vine['country'] != 'null':
                most_common_country.append(vine['country'])
            else:
                pass
            if vine['points'] != 'null':
                avarage_score.append(int(vine['points']))
            else:
                pass
        else:
            pass
    stast['avarege_price'] = statistics.mean(prices)
    stast['min_price'] = min(prices)
    stast['max_price'] = max(prices)
    stast['most_common_region'] = Counter(most_common_region).most_common()[0][0]
    stast['most_common_country'] = Counter(most_common_country).most_common()[0][0]
    stast['avarage_score'] = statistics.mean(avarage_score)

    return stats


def to_markdown(file: str):

    replaces = (('{', '\n\n'), (',', '\n'), ('}', '\n\n'))
    for replace in replaces:
        file = file.replace(*replace)

    return file


with open('./winedata_1.json') as wine1:
    wine1 = wine1.read()
winedata_1 = jsParser(wine1)

with open('./winedata_2.json') as wine2:
    wine2 = wine2.read()
winedata_2 = jsParser(wine2)

######################
# merge файлов
######################
winedata_full = winedata_2.copy()
for i in winedata_1:
    if i not in winedata_2:
        winedata_full.append(i)

######################
# сортировка
######################
wine1_s = wine1.replace('null', '0')
wine2_s = wine2.replace('null', '0')

winedata_1_s = jsParser(wine1_s)
winedata_2_s = jsParser(wine2_s)

winedata_full_to_sort = winedata_2_s.copy()
for i in winedata_1_s:
    if i not in winedata_2_s:
        winedata_full_to_sort.append(i)

sorted_data = sorted(winedata_full_to_sort, key=lambda k: (-int(k['price']), k['variety']))


######################
# статистика по сортам
######################
Riesling_stats = {'avarege_price': [],
                  'min_price': [],
                  'max_price': [],
                  'most_common_region': [],
                  'most_common_country': [],
                  'avarage_score': []}
Gewurztraminer_stats = Riesling_stats.copy()
Merlot_stats = Riesling_stats.copy()
Tempranillo_stats = Riesling_stats.copy()
Red_Blend_stats = Riesling_stats.copy()

wines = ['Riesling',
         'Gewurztraminer',
         'Merlot',
         'Tempranillo',
         'Red Blend']

wine_stats = [Riesling_stats,
              Gewurztraminer_stats,
              Merlot_stats,
              Tempranillo_stats,
              Red_Blend_stats]

for wine in range(len(wines)):
    stats(wines[wine], wine_stats[wine])

wine = {'Riesling': Riesling_stats,
        'Gewurztraminer': Gewurztraminer_stats,
        'Merlot': Merlot_stats,
        'Tempranillo': Tempranillo_stats,
        'Red Blend': Red_Blend_stats}

######################
# общая статистика
######################
# самое дорогое и самое дешевое
names = []
values = []

for vine in winedata_full:
    if vine['price'] != 'null':
        values.append(int(vine['price']))
        names.append(vine['title'])
    else:
        pass

# для поиска коллизий
values = np.array(values)
max_index = np.where(values == max(values))[0]
min_index = np.where(values == min(values))[0]


most_expensive_wine = [names[i] for i in max_index]
cheapest_wine = [names[i] for i in min_index]

# высокая оценка и низкая оценка
names = []
values = []

for vine in winedata_full:
    if vine['points'] != 'null':
        values.append(int(vine['points']))
        names.append(vine['title'])
    else:
        pass

# для поиска коллизий
values = np.array(values)
max_index = np.where(values == max(values))[0]
min_index = np.where(values == min(values))[0]

highest_score = [names[i] for i in max_index]
lowest_score = [names[i] for i in min_index]

# most_expensive_coutry  and  cheapest_coutry
countries = []
values = []
means = []


for vine in winedata_full:
    if vine['country'] != 'null' and vine['price'] != 'null':
        if vine['country'] not in countries:
            countries.append(vine['country'])
        else:
            pass
    else:
        pass

for country in countries:
    values = []
    for vine in winedata_full:
        if vine['country'] == country and vine['price'] != 'null':
            values.append(int(vine['price']))
    means.append(statistics.mean(values))


# для поиска коллизий
means = np.array(means)
max_index = np.where(means == max(means))[0]
min_index = np.where(means == min(means))[0]

most_expensive_coutry = [countries[i] for i in max_index]
cheapest_coutry = [countries[i] for i in min_index]

# most_rated_country  and  #underrated_country
countries = []
values = []
means = []

for vine in winedata_full:
    if vine['country'] != 'null' and vine['points'] != 'null':
        if vine['country'] not in countries:
            countries.append(vine['country'])
        else:
            pass
    else:
        pass

for country in countries:
    values = []
    for vine in winedata_full:
        if vine['country'] == country and vine['points'] != 'null':
            values.append(int(vine['points']))
    means.append(statistics.mean(values))

# для поиска коллизий
means = np.array(means)
max_index = np.where(means == max(means))[0]
min_index = np.where(means == min(means))[0]

most_rated_country = [countries[i] for i in max_index]
underrated_country = [countries[i] for i in min_index]

# most_active_commentator

names = []

for vine in winedata_full:
    if vine['taster_name'] != 'null':
        names.append(vine['taster_name'])
    else:
        pass

most_active_commentator = Counter(names).most_common()[0][0]

######################
# запись в файл
######################
with open('./winedata_full.json', 'w') as f:
    f.write(str(winedata_full).replace('\'', '"'))

with open('./stats.json', 'w') as f:
    f.write('{"statistics": {"wine": ')
    f.write(str(wine).replace('\'', '"'))
    f.write('}, ')
    f.write(f'"most_expensive_wine": {most_expensive_wine}, ')
    f.write(f'"cheapest_wine": {cheapest_wine}, ')
    f.write(f'"highest_score": {highest_score}, ')
    f.write(f'"lowest_score": {lowest_score}, ')
    f.write(f'"most_expensive_coutry": {most_expensive_coutry}, ')
    f.write(f'"cheapest_coutry": {cheapest_coutry}, ')
    f.write(f'"most_rated_country": {most_rated_country}, ')
    f.write(f'"underrated_country": {underrated_country}, ')
    f.write(f'"most_active_commentator": {most_active_commentator} ')
    f.write('} } ')

with open('./stats.md', 'w') as f:
    f.write('Statistics: \nWine:')
    f.write(to_markdown(str(wine)))
    f.write('"')
