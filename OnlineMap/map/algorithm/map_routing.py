import requests
import xml.etree.ElementTree as ET

from .grapth_analyses import Graph
from .map_pen import Vertice, Line, Color


def MapRouting1(starting_point, end_point): #удалить после отладки функции map_routing

    svg_url1 = f'https://map.spbgasu.ru/images/maps/{5}.svg'
    svg_content1 = requests.get(svg_url1).text

    svg_url2 = f'https://map.spbgasu.ru/images/maps/{6}.svg'
    svg_content2 = requests.get(svg_url2).text
    #какая то логика для отрисовки линий

    return svg_content1, svg_content2

ffGASU_vertices ={
    # Нулевой этаж
    
    "00111320" : Vertice('1070', '92'),
    "00111520" : Vertice('1070', '92'),
    "00110120" : Vertice('1123', '140'),
    "00110121" : Vertice('1134', '129'),
    "00111321" : Vertice('1094', '105'),
    "00111322" : Vertice('1110', '94'),
    
    "00100020" : Vertice('1470.57', '402.3'),
    "00100021" : Vertice('1503.67', '421.83'),
    "00100022" : Vertice('1563.9', '386.1'),
    "00110020" : Vertice('1502.67', '346.03'),
    "00110220" : Vertice('1611.9', '358.03'),
    "00113710" : Vertice('1583.87', '399.87'),
    
    # Первый этаж

    # Второй этаж
    "01111120" : Vertice('2342.42', '859.19'),
    "01111121" : Vertice('2347.9', '854.03'),
    "01111021" : Vertice('2306.61', '830.48'),
    "01111020" : Vertice('2299.84', '835'),
    "01111820" : Vertice('2312.1', '825'),
    "01110921" : Vertice('2265.97', '805.32'),
    "01110920" : Vertice('2258.55', '810.81'),
    "01111921" : Vertice('2251.77', '798.87'),
    "01111920" : Vertice('2259.84', '793.39'),
    "01110821" : Vertice('2222.1', '781.13'),
    "01110820" : Vertice('2215.97', '786.29'),
    "01112020" : Vertice('2215.32', '768.23'),
    "01112021" : Vertice('2207.9', '773.71'),
    "01110721" : Vertice('2186.94', '761.45'),
    "01110720" : Vertice('2180.48', '766.61'),
    "01110620" : Vertice('2156.61', '751.77'),
    "01110621" : Vertice('2167.58', '742.42'),
    "01110622" : Vertice('2177.26', '735'),
    "01110623" : Vertice('2152.42', '717.26'),
    "01110624" : Vertice('2114.35', '693.39'),
    "01110625" : Vertice('2095', '700.48'),
    "01110421" : Vertice('2050.48', '676.29'),
    "01110420" : Vertice('2037.26', '683.06'),
    
    # Третий этаж
    
    # Четвертый этаж
    
    # Пятый этаж
    
    # Шестой этаж
    
    # Седьмой этаж
    "07770830" : Vertice('1350', '-91.7'), #Кабинет №708А
    "07770831" : Vertice('1344.4', '-86.2'), #Выход из кабинета №708А
    "07771031" : Vertice('1365.3', '-73.7'), #Кабинет №710А
    "07771030" : Vertice('1372.7', '-78.2'), #Выход из кабинета №710А
    "07771230" : Vertice('1404', '-60.3'), #Кабинет №712А
    "07771231" : Vertice('1397.9', '-54.8'), #Выход из кабинета №712А
    "07771430" : Vertice('1465.1', '-25.2'), #Кабинет №714А
    "07771431" : Vertice('1459.1', '-19'), #Выход из кабинета №714А
    "07771630" : Vertice('1534.4', '14.9'), #Кабинет №716А
    "07771631" : Vertice('1528.5', '21.4'), #Выход из кабинета №716А
    "07771830" : Vertice('1579.8', '41.3'), #Кабинет №718А
    "07771831" : Vertice('1572.3', '47.2'), #Выход из кабинета №718А
    "07771832" : Vertice('1568.2', '44.9'),
    "07771931" : Vertice('1547.2', '58.7'), #Выход из кабинета №719А
    "07700030" : Vertice('1566', '70.4'), #Лестница 1 А
    "07771930" : Vertice('1518', '76.7'), #Кабинет №719А
    "07700130" : Vertice('1403.5', '-34'), #Лестница 2 A
    "07700131" : Vertice('1351.2', '-65.1'), #Лестница 2 A
    "07770630" : Vertice('1281.4', '-35.1'), #Кабинет №706С
    "07770631" : Vertice('1287.6', '-28.4'), #Выход из кабинета №706С
    "07770330" : Vertice('1221.5', '22.9'), #Кабинет №703С
    "07770331" : Vertice('1213', '14.9'), #Выход из кабинета №703С
    "07770430": Vertice('1197.1', '14.3'), #Кабинет №704С
    "07770431" : Vertice('1203.5', '20.3'), #Выход из кабинета №704С
    "07772032" : Vertice('1126.1', '65.4'),
    "07772020" : Vertice('1135.3', '72.8'), #Кабинет №720С
    "07771920" : Vertice('1119', '59.5'), #Кабинет №719С
    "07700022" : Vertice('1065.4', '100.7'), #угол коридора
    "07771722" : Vertice('1047.2', '89.8'),
    "07771820" : Vertice('1073.2', '73.2'), #Кабинет №718С
    "07771720" : Vertice('1032.3', '99'), #Кабинет №717С
    "07771521" : Vertice('1079.1', '109'), #Выход из кабинета №715С
    "07771520" : Vertice('1065.8', '118.8'), #Кабинет №715С
    "07771321" : Vertice('1130.51', '139.26'), #Выход из кабинета №713С
    "07771320" : Vertice('1121.2', '150.1'), #Кабинет №713С
    "07771421" : Vertice('1135', '141.3'), #Выход из кабинета №714С
    "07771420" : Vertice('1142.8', '134.6'), #Кабинет №714С
    "07771221" : Vertice('1173.6', '163.7'), #Выход из кабинета №712С
    "07771220" : Vertice('1181.2', '156.1'), #Кабинет №712С
    "07771121" : Vertice('1183.49', '170.29'), #Выход из кабинета №711С
    "07771120" : Vertice('1173.5', '180.3'), #Кабинет №711С
    "07770921" : Vertice('1224.7', '194.1'), #Кабинет №709С
    "07770920" : Vertice('1214.2', '204.3'), #Выход из кабинета №709С
    "07771021" : Vertice('1227.76', '195.54'), #Выход из кабинета №710С
    "07771020" : Vertice('1235.66', '187.64'), #Кабинет №710С
    "07770821" : Vertice('1273.66', '222.29'), #Выход из кабинета №708С
    "07770820" : Vertice('1281.66', '214.08'), #Кабинет №708С
    "07770521" : Vertice('1346.72', '265.26'), #Выход из кабинета №705С
    "07770520" : Vertice('1337.08', '275.79'), #Кабинет №705С
    "07770621" : Vertice('1365.16', '275.79'), #Выход из кабинета №706С
    "07770620" : Vertice('1372.95', '266.97'), #Кабинет №706С
    "07770421" : Vertice('1418.95', '307.19'), #Выход из кабинета №704С
    "07770420" : Vertice('1427.66', '297.97'), #Кабинет №704С
    "07770321" : Vertice('1424.42', '310.94'), #Выход из кабинета №703С
    "07770320" : Vertice('1415.3', '320.87'), #Кабинет №703С
    "07770220" : Vertice('1464.54', '320.36'), #Кабинет №702С и Тут должен быть туалет, но его нет на карте
    "07770221" : Vertice('1456.64', '328.88'), #Кабинет №702С и Тут должен быть туалет, но его нет на карте
    "07700122" : Vertice('1528.7', '371.5'),
    "07770121" : Vertice('1543.6', '379.8'), #Выход из кабинета №701С
    "07770120": Vertice('1597.59', '348.39'), #Кабинет №701С
    "07700221" : Vertice('1483.2', '399.9'),
    "07700220" : Vertice('1477.1', '395.6'),
    "07700321" : Vertice('1083.59', '111.35'),
    "07700320" : Vertice('1104.86', '96.45'), #лестница 3 С
    "07700132" : Vertice('1396.6', '-38'),
    "07700133" : Vertice('1407.8', '-48.5'),
    "07700137" : Vertice('1317.1', '-45.37'), #Тут должен быть туалет, но его нет на карте
    "07700037" : Vertice('1325.6', '-37.1'), #Тут должен быть туалет, но его нет на карте
    
    # Восьмой этаж
}

#Формат заполнения графа смежности (делается к сожалению вручную ничего поделать не могу)
# {location_from : Edge(location_to, path_weigth)}
# От вершин обознащающих кабинеты исходят пути с весом нуль (т.к. прилегающие вершины
#                                                   обознащают что мы никуда не идём)
# Все осатльные пути взвешиваем на глаз по карте, стараясь попадать в отношение 1:1 метров
# Желательно писать только целые числа для того чтобы в последствии не путать себя и других

# Часть 1-го этажа ГАСУ строительного корпуса (first_floor_GASU_matrix)

ffGASU_matrix ={
    # Нулевой этаж
    '00111322': {'00111321' : 2},
    '00111321': {'00111320' : 1, '00111520': 1, '00110121': 2, '00111322': 1},
    '00110121': {'00110120' : 1, '00111321': 1},
    '00111320': {'00111321' : 1},
    '00111520': {'00111321' : 1},
    '00110120': {'00110121' : 1},
    '00100020': {'00100021' : 1},
    '00100021': {'00100020' : 2, '00100022' : 4},
    '00100022': {'00100021' : 4, '00113710' : 1, '00110220' : 2, '00110020': 4},
    '00110020': {'00100022' : 4},
    '00110220': {'00100022' : 2},
    '00113710': {'00100022' : 1},

    # Первый этаж

    # Второй этаж
    '01111120' : {'01111121' : 1},
    '01111121' : {'01111120' : 1, '01111021' : 1},
    '01111021' : {'01111121' : 1,'01111020' : 1, '01111820' : 1, '01110921' : 1},
    '01111020' : {'01111021' : 1},
    '01111820' : {'01111021' : 1},
    '01110921' : {'01111021' : 1, '01110920' : 1, '01111921' : 1},
    '01110920' : {'01110921' : 1},
    '01111921' : {'01110921' : 1, '01111920' : 1,'01110821' : 1},
    '01111920' : {'01111921' : 1},
    '01110821' : {'01111921' : 1, '01110820' : 1, '01112021' : 1},
    '01110820' : {'01110821' : 1},
    '01112021' : {'01110821' : 1, '01110820' : 1, '01110721' : 1},
    '01112020' : {'01112021' : 1},
    '01110721' : {'01112021' : 1,'01110720' : 1, '01110621' : 1},
    '01110720' : {'01110721' : 1},
    '01110621' : {'01110620' : 1, '01110721' : 1, '01110622' : 1},
    '01110620' : {'01110621' : 1},
    '01110622' : {'01110621' : 1, '01110623' : 1},
    '01110623' : {'01110622' : 1, '01110624' : 2},
    '01110624' : {'01110623' : 2, '01110625' : 1},
    '01110625' : {'01110624' : 1, '01110421' : 2},
    '01110421' : {'01110420' : 1, '01110625' : 2},
    '01110420' : {'01110421' : 1},
    
    # Третий этаж
    
    # Четвертый этаж
    
    # Пятый этаж
    
    # Шестой этаж
    
    # Седьмой этаж
    "07770830" : {'07770831' : 1}, #Кабинет №708А
    "07770831" : {'07770830' : 1, '07771031' : 1}, #Выход из кабинета №708А
    "07771031" : {'07771030' : 1, '07770831' : 1, '07771231' : 1, '07700131' : 1}, #Выход из кабинета №710А
    "07771030" : {'07771031' : 1},#Кабинет №710А
    "07771230" : {'07771231' : 1}, #Кабинет №712А
    "07771231" : {'07771230' : 1, '07771031' : 1, '07700133' : 1}, #Выход из кабинета №712А
    "07771430" : {'07771430' : 1}, #Кабинет №714А
    "07771431" : {'07771430' : 1, '07700133' : 2, '07771631' : 2}, #Выход из кабинета №714А
    "07771630" : {'07771631' : 1}, #Кабинет №716А
    "07771631" : {'07771630' : 1, '07771431' : 2, '07771832' : 1}, #Выход из кабинета №716А
    "07771830" : {'07771831' : 1}, #Кабинет №718А
    "07771831" : {'07771830' : 1, '07771832' : 1}, #Выход из кабинета №718А
    "07771832" : {'07771831' : 1, '07771631' : 1, '07771931' : 1},
    "07771931" : {'07771930' : 1, '07771832' : 1, '07771831' : 1}, #Выход из кабинета №719А
    "07700030" : {'07771931' : 1}, #Лестница 1 А
    "07771930" : {'07771931' : 1}, #Кабинет №719А
    "07700130" : {'07700132' : 1}, #Лестница 2 A
    "07700132": {'07700130': 1, '07700133' : 1, '07700131' : 2}, #Лестница 2 A
    "07700133": {'07700132': 1, '07771231' : 1, '07771431' : 2},
    "07700131" : {'07700132' : 2, '07771031' : 1, '07700137' : 1},
    "07700137": {'07700037': 1, '07770631' : 1, '07700131' : 2},  # Тут должен быть туалет, но его нет на карте
    "07700037": {'07700137': 1},  # Тут должен быть туалет, но его нет на карте
    "07770630" : {'07770631' : 1}, #Кабинет №706С
    "07770631" : {'07770630' : 1, '07770331' : 4, '07700137' : 1}, #Выход из кабинета №706С
    "07770330" : {'07770331' : 1}, #Кабинет №703С
    "07770331" : {'07770330' : 1, '07770431' : 1, '07770631' : 4}, #Выход из кабинета №703С
    "07770430": {'07770431' : 1}, #Кабинет №704С
    "07770431" : {'07770430' : 1, '07772032' : 4, '07770331' : 1}, #Выход из кабинета №704С
    "07772032" : {'07772020' : 1, '07771920' : 1, '07700022' : 3, '07770431' : 4}, #Выход из кабинета №719С и №720С
    "07772020" : {'07772032' : 1}, #Кабинет №720С
    "07771920" : {'07772032' : 1}, #Кабинет №719С
    "07700022" : {'07771722' : 1, '07772032' : 3, '07771521' : 1}, #угол коридора
    "07771722" : {'07771820' : 2, '07771720' : 1, '07700022' : 1},
    "07771820" : {'07771722' : 2}, #Кабинет №718С
    "07771720" : {'07771722' : 1}, #Кабинет №717С
    "07771521" : {'07771520' : 1, '07700321' : 1, '07700022' : 1}, #Выход из кабинета №715С
    "07771520" : {'07771521' : 1}, #Кабинет №715С
    "07771321" : {'07771320' : 1, '07771421' : 1, '07700321' : 2}, #Выход из кабинета №713С
    "07771320" : {'07771321' : 1}, #Кабинет №713С
    "07771421" : {'07771420' : 1, '07771221' : 2, '07771321' : 1}, #Выход из кабинета №714С
    "07771420" : {'07771421' : 1}, #Кабинет №714С
    "07771221" : {'07771220' : 1, '07771121' : 1, '07771421' : 2}, #Выход из кабинета №712С
    "07771220" : {'07771221' : 1}, #Кабинет №712С
    "07771121" : {'07771120' : 1, '07770921' : 2, '07771221' : 1}, #Выход из кабинета №711С
    "07771120" : {'07771121' : 1}, #Кабинет №711С
    "07770920" : {'07770921' : 1}, #Кабинет №709С
    "07770921" : {'07770920' : 1, '07771021' : 1, '07771121' : 2}, #Выход из кабинета №709С
    "07771021" : {'07771020' : 1, '07770821' : 2, '07770921' : 1}, #Выход из кабинета №710С
    "07771020" : {'07771021' : 1}, #Кабинет №710С
    "07770821" : {'07770820' : 1, '07770521' : 3, '07771021' : 2}, #Выход из кабинета №708С
    "07770820" : {'07770821' : 1}, #Кабинет №708С
    "07770521" : {'07770520' : 1, '07770621' : 1, '07770821' : 3}, #Выход из кабинета №705С
    "07770520" : {'07770521' : 1}, #Кабинет №705С
    "07770621" : {'07770620' : 1, '07770421' : 3, '07770521' : 1}, #Выход из кабинета №706С
    "07770620" : {'07770621' : 1}, #Кабинет №706С
    "07770421" : {'07770420' : 1, '07770321' : 1, '07770621' : 3}, #Выход из кабинета №704С
    "07770420" : {'07770421' : 1}, #Кабинет №704С
    "07770321" : {'07770221' : 2, '07770320' : 1, '07770421' : 1}, #Выход из кабинета №703С
    "07770320" : {'07770321' : 1}, #Кабинет №703С
    "07770220" : {'07770221' : 1}, #Кабинет №702С и Тут должен быть туалет, но его нет на карте
    "07770221" : {'07770220' : 1, '07700122' : 3, '07770321' : 2}, #Кабинет №702С и Тут должен быть туалет, но его нет на карте
    "07700122" : {'07770121' : 1, '07770221' : 3, '07700221' : 2},
    "07770121" : {'07770120' : 3, '07700122' : 1}, #Выход из кабинета №701С
    "07770120": {'07770121' : 3}, #Кабинет №701С
    "07700221" : {'07700122' : 2, '07700220' : 1},
    "07700220" : {'07700221' : 1},
    "07700321" : {'07700320' : 1, '07771321' : 2, '07771521' : 1},
    "07700320" : {'07700321' : 1}, #лестница 3 С
    # Восьмой этаж
}

G = Graph(ffGASU_matrix)
# location_start, location_end = input('Введите через пробел location_start и location_end').split() #удалить после отладки


def MapRouting(location_start, locatino_end):
    path = G.shortest_path(location_start, locatino_end)
    print(path)

    r = requests.get('https://map.spbgasu.ru/images/maps/7.svg')

    root = ET.fromstring(r.content)

    ET.register_namespace('', 'http://www.w3.org/2000/svg')

    for pos in range(len(path) - 1):
        Line(ffGASU_vertices[path[pos]], ffGASU_vertices[path[pos+1]], Color(193, 68, 36)).get_line_code(root)

    # tree.write('res.svg')

    return ET.tostring(root, encoding='unicode', method='xml')
