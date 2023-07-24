from random import random

import numpy as np
from PIL import Image, ImageDraw, ImageFont

np.set_printoptions(suppress=True)


# np.set_printoptions(Supress = True)
# def get_rand_box():
#     start_x = random() * 3200
#     start_y = random() * 2000
#     width = random() * 300 + 50
#     height = random() * 200 + 30
#     return [start_x, start_y, start_x + width, start_y + height]
# boxes = [get_rand_box() for _ in range(100)]


boxes = [
    [2508.47428911, 915.02960329, 2783.26939476, 1007.84987855],
    [3034.6874079, 1648.84387642, 3257.66968839, 1691.00769834],
    [1315.51908376, 1253.69000289, 1506.26182445, 1456.00498787],
    [136.19325052, 1786.39643654, 198.45948777, 1938.98658293],
    [1696.63859432, 421.58176972, 2032.93253225, 636.47667598],
    [56.90552702, 743.24794566, 250.00560401, 918.5292016],
    [522.13410196, 1375.02077601, 748.30876317, 1463.70336703],
    [1613.38036278, 791.17615083, 1745.67144102, 856.14961441],
    [1188.96334625, 1257.93690012, 1392.83407481, 1356.58799905],
    [2278.42485562, 478.40214029, 2429.2335008, 646.60490413],
    [1611.0267297, 1961.38970979, 1730.70429649, 2128.07760256],
    [2206.3087746, 104.8308647, 2350.07167813, 260.1632693],
    [262.53652666, 1224.09219573, 415.93420223, 1306.66951555],
    [1095.92577604, 1426.56765146, 1169.06790367, 1621.02152529],
    [2557.61120496, 1315.08206801, 2692.14936768, 1500.27490048],
    [1234.03068198, 1244.62277514, 1452.17253303, 1275.71046947],
    [1184.80581382, 1169.0846051, 1497.53192212, 1338.99608837],
    [1577.7379405, 1028.54617508, 1915.26410294, 1085.43022364],
    [97.16537998, 1608.31917113, 313.15810812, 1676.44348577],
    [645.09929117, 1867.13496823, 757.99552075, 2036.98612716],
    [772.09662844, 449.17956639, 860.08148444, 499.45896939],
    [2780.73751152, 18.26186835, 3020.58525598, 64.75763766],
    [896.86802971, 237.99489685, 1159.62995892, 429.45653832],
    [2684.22635853, 1303.22477921, 2768.04883341, 1493.62918601],
    [667.62028059, 1853.63874299, 994.73892838, 1944.74350208],
    [2064.37171691, 334.09352485, 2187.29722226, 551.65169101],
    [2629.09201435, 1653.62160016, 2707.15987707, 1837.9048636],
    [2405.84819482, 977.1627691, 2696.77769121, 1084.00841146],
    [2338.48155404, 357.59075301, 2602.09643189, 586.05761122],
    [2561.42694651, 1192.98270592, 2906.96224161, 1348.28812086],
    [3033.62538237, 1659.0507552, 3359.91547765, 1814.23318401],
    [2687.57342688, 1590.94182927, 2755.84125328, 1623.57562954],
    [2291.65400501, 1488.97629979, 2350.64100497, 1655.88212202],
    [785.24984825, 1800.79638489, 1097.96144664, 1895.83760471],
    [901.93867276, 1338.72369694, 986.195685, 1380.42168408],
    [2450.40427264, 1828.46844322, 2582.26278651, 1986.15396429],
    [1594.49240248, 1501.59269884, 1810.48373767, 1581.47408313],
    [2858.55001856, 79.5198182, 3186.9584076, 281.06976243],
    [2921.74178691, 681.13832378, 3143.12616671, 720.36616651],
    [2434.28262326, 414.4403609, 2751.74011749, 639.03542582],
    [205.95514789, 1384.23534363, 547.60593798, 1441.1072128],
    [196.22977509, 83.29342476, 469.04280751, 205.44812331],
    [561.36180882, 12.36407894, 880.41402834, 239.11744347],
    [3102.19370035, 728.48465506, 3157.09012071, 908.75021402],
    [1996.44502015, 72.12745835, 2293.1969528, 244.57035572],
    [2413.68497105, 1136.30890379, 2689.34019037, 1307.58780357],
    [2087.78715508, 800.19301487, 2310.90939926, 1018.20817531],
    [567.5178776, 14.07660134, 619.76174326, 103.1992764],
    [192.77950555, 1489.06176768, 411.04469698, 1633.31787138],
    [669.38861672, 1182.92207246, 933.22536808, 1345.07268103],
    [1620.32491502, 1222.81477263, 1683.6337731, 1424.97336212],
    [3158.76025648, 10.39298618, 3440.70642773, 213.28445985],
    [12.04123999, 8.41137969, 253.54134758, 220.11740078],
    [852.92591827, 956.91151364, 1129.18314769, 1109.03647173],
    [643.60683812, 1910.83288813, 872.11866875, 1946.99271165],
    [2778.07732234, 559.91695919, 3041.83763748, 719.01068918],
    [2644.03171901, 1256.59687937, 2905.10083788, 1320.15363977],
    [2358.70753004, 1745.96209556, 2659.34676273, 1805.43363629],
    [2663.64505619, 179.99043148, 2952.61927872, 355.59127843],
    [1640.08377602, 1063.07342058, 1796.08009243, 1199.66688112],
    [3033.6728334, 1966.02393313, 3143.90544438, 2106.40938575],
    [2506.28444092, 1690.52267283, 2765.22040331, 1747.74663378],
    [630.16788849, 1305.8260637, 957.85851551, 1367.27905638],
    [2767.5680757, 1972.44308518, 2931.96982664, 2067.92203524],
    [2767.24577661, 980.91559013, 2868.8922413, 1046.02437708],
    [1292.8158492, 1572.02620343, 1420.89132799, 1674.49654129],
    [2902.74234482, 644.04146099, 3111.01433397, 710.46582469],
    [2758.44677604, 134.74275055, 2920.45053972, 288.47458611],
    [967.8614371, 901.52046151, 1262.67630769, 1048.77862486],
    [2201.57684637, 1844.13248701, 2440.24569051, 1931.07745193],
    [2695.91783772, 510.44854967, 2854.5173477, 697.7633569],
    [2297.24999239, 1800.60051822, 2630.60626843, 1904.29531202],
    [2054.05491884, 62.22323635, 2375.0451966, 255.83569436],
    [3198.92463532, 1430.47261601, 3529.94141336, 1597.73505632],
    [2326.46162942, 459.72773873, 2517.68947638, 662.31662001],
    [1541.5678645, 1755.31497867, 1627.84034474, 1845.22571777],
    [1086.19355757, 1559.09117096, 1389.47729879, 1631.97547609],
    [1881.27853968, 1219.848096, 1982.03129841, 1370.26908974],
    [1822.88402063, 273.93455253, 2171.94933019, 424.618526],
    [971.30422969, 446.47010158, 1037.00283805, 588.63509072],
    [22.56664487, 546.41973752, 326.10804298, 775.73452579],
    [2065.75817652, 1042.04025179, 2253.27789657, 1095.35546863],
    [1550.27001798, 272.50172134, 1862.01019321, 480.50552274],
    [2305.51449827, 260.51197625, 2398.09280401, 457.0601794],
    [1064.70265846, 1077.44287412, 1303.02464201, 1260.2381211],
    [258.7058094, 4.61898122, 608.26625933, 64.45229784],
    [2434.4147091, 919.45568013, 2623.53896093, 1059.17854782],
    [2892.33641911, 670.17020995, 3176.74884297, 874.47305269],
    [1381.05888592, 1725.64751329, 1692.36770331, 1934.52227427],
    [2191.31074992, 844.44055291, 2511.7644765, 920.85709236],
    [405.76995522, 808.67935358, 526.44637033, 1010.54037456],
    [1568.58164083, 1499.65197076, 1657.72358278, 1565.67172089],
    [1196.26676721, 1579.28103061, 1343.11772085, 1723.69785757],
    [1328.41963735, 802.20907847, 1538.39543198, 1024.19076167],
    [518.74910523, 1012.31482387, 684.74937753, 1228.9305202],
    [1597.08060753, 1569.81874791, 1796.51328065, 1735.79970809],
    [2095.8995096, 127.15228053, 2380.27623663, 248.98375886],
    [3134.82492691, 422.89693824, 3198.77540122, 478.02272413],
    [1103.04032375, 1247.06426743, 1310.8438419, 1415.57613525],
    [2683.06044, 612.02311844, 2868.50447613, 813.19514696],
]

# boxes = np.array(boxes)


def draw_bboxes_on_pil_image(draw, boxes, fnt):
    for idx, box in enumerate(boxes):
        draw.text((box[0], box[1]), str(idx), fill=(0, 0, 255), font=fnt)
        draw.rectangle(box, outline=(255, 0, 0), width=2)


def draw_random_lines_between_boxes(draw, boxes, fnt):

    for _ in range(100):
        rand_idx1 = int(random() * len(boxes))
        rand_idx2 = int(random() * len(boxes))
        start_box = boxes[rand_idx1]
        end_box = boxes[rand_idx2]

        start_x = (start_box[0] + start_box[2]) // 2
        start_y = (start_box[1] + start_box[3]) // 2
        end_x = (end_box[0] + end_box[2]) // 2
        end_y = (end_box[1] + end_box[3]) // 2

        random_color = (int(random() * 255), int(random() * 255), int(random() * 255))

        draw.line(((start_x, start_y), (end_x, end_y)), fill=random_color, width=1)


# prepare empty image
img = Image.new("RGB", (3400, 2500), (255, 255, 255))

# prepare draw
draw = ImageDraw.Draw(img)

boxes = [list(map(int, box)) for box in boxes]
texts = [str(random()) for _ in range(len(boxes))]

fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 100)
# draw_boxes(draw, boxes, fnt)
# draw_random_lines_between_boxes(draw, boxes, fnt)
# img.show()


sort_boxes_by_line(boxes, texts)
