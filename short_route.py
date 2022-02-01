
point_1 = (0, 2)  # координаты второй точки
point_2 = (2, 5)  # координаты второй точки
point_3 = (6, 6)  # координаты третьей точки
point_4 = (8, 3)  # координаты четвертой точки
point_5 = (5, 2)  # координаты пятой точки
# расстояния между точками
route_part_12 = route_part_21 = (((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5)
route_part_13 = route_part_31 = (((point_3[0] - point_1[0]) ** 2 + (point_3[1] - point_1[1]) ** 2) ** 0.5)
route_part_14 = route_part_41 = (((point_4[0] - point_1[0]) ** 2 + (point_4[1] - point_1[1]) ** 2) ** 0.5)
route_part_15 = route_part_51 = (((point_5[0] - point_1[0]) ** 2 + (point_5[1] - point_1[1]) ** 2) ** 0.5)
route_part_23 = route_part_32 = (((point_3[0] - point_2[0]) ** 2 + (point_3[1] - point_2[1]) ** 2) ** 0.5)
route_part_24 = route_part_42 = (((point_4[0] - point_2[0]) ** 2 + (point_4[1] - point_2[1]) ** 2) ** 0.5)
route_part_25 = route_part_52 = (((point_5[0] - point_2[0]) ** 2 + (point_5[1] - point_2[1]) ** 2) ** 0.5)
route_part_34 = route_part_43 = (((point_4[0] - point_3[0]) ** 2 + (point_4[1] - point_3[1]) ** 2) ** 0.5)
route_part_35 = route_part_53 = (((point_5[0] - point_3[0]) ** 2 + (point_5[1] - point_3[1]) ** 2) ** 0.5)
route_part_45 = route_part_54 = (((point_5[0] - point_4[0]) ** 2 + (point_5[1] - point_4[1]) ** 2) ** 0.5)
# список всех возможных маршрутов
all_routes = [ 
    {"(2, 5)": route_part_12, "(6, 6)": route_part_12 + route_part_23,
    "(8, 3)": route_part_12 + route_part_23 + route_part_34,
    "(5, 2)": route_part_12 + route_part_23 + route_part_34 + route_part_45,
    "(0, 2)": route_part_12 + route_part_23 + route_part_34 + route_part_45 + route_part_51},
    {"(2, 5)": route_part_12, "(5, 2)": route_part_12 + route_part_25,
    "(6, 6)": route_part_12 + route_part_25 + route_part_53,
    "(8, 3)": route_part_12 + route_part_25 + route_part_53 + route_part_34,
    "(0, 2)": route_part_12 + route_part_25 + route_part_53 + route_part_34 + route_part_41},
    {"(2, 5)": route_part_12, "(8, 3)": route_part_12 + route_part_24,
    "(5, 2)": route_part_12 + route_part_24 + route_part_45,
    "(6, 6)": route_part_12 + route_part_24 + route_part_45 + route_part_53,
    "(0, 2)": route_part_12 + route_part_24 + route_part_45 + route_part_53 + route_part_31},
    {"(2, 5)": route_part_12, "(8, 3)": route_part_12 + route_part_24,
    "(6, 6)": route_part_12 + route_part_24 + route_part_43,
    "(5, 2)": route_part_12 + route_part_24 + route_part_43 + route_part_35,
    "(0, 2)": route_part_12 + route_part_24 + route_part_43 + route_part_35 + route_part_51},
    {"(2, 5)": route_part_12, "(6, 6)": route_part_12 + route_part_23,
    "(5, 2)": route_part_12 + route_part_23 + route_part_35,
    "(8, 3)": route_part_12 + route_part_23 + route_part_35 + route_part_54,
    "(0, 2)": route_part_12 + route_part_23 + route_part_35 + route_part_54 + route_part_41},
    {"(2, 5)": route_part_12, "(5, 2)": route_part_12 + route_part_25,
    "(8, 3)": route_part_12 + route_part_25 + route_part_54,
    "(6, 6)": route_part_12 + route_part_25 + route_part_54 + route_part_43,
    "(0, 2)": route_part_12 + route_part_25 + route_part_54 + route_part_43 + route_part_31},
    {"(6, 6)": route_part_13, "(2, 5)": route_part_13 + route_part_32,
    "(8, 3)": route_part_13 + route_part_32 + route_part_24,
    "(5, 2)": route_part_13 + route_part_32 + route_part_24 + route_part_45,
    "(0, 2)": route_part_13 + route_part_32 + route_part_24 + route_part_45 + route_part_51},
    {"(6, 6)": route_part_13, "(2, 5)": route_part_13 + route_part_32,
    "(5, 2)": route_part_13 + route_part_32 + route_part_25,
    "(8, 3)": route_part_13 + route_part_32 + route_part_25 + route_part_54,
    "(0, 2)": route_part_13 + route_part_32 + route_part_25 + route_part_54 + route_part_41},
    {"(6, 6)": route_part_13, "(8, 3)": route_part_13 + route_part_34,
    "(2, 5)": route_part_13 + route_part_34 + route_part_42,
    "(5, 2)": route_part_13 + route_part_34 + route_part_42 + route_part_25,
    "(0, 2)": route_part_13 + route_part_34 + route_part_42 + route_part_25 + route_part_51},
    {"(6, 6)": route_part_13, "(8, 3)": route_part_13 + route_part_34,
    "(5, 2)": route_part_13 + route_part_34 + route_part_45,
    "(2, 5)": route_part_13 + route_part_34 + route_part_45 + route_part_52,
    "(0, 2)": route_part_13 + route_part_34 + route_part_45 + route_part_52 + route_part_21},
    {"(6, 6)": route_part_13, "(5, 2)": route_part_13 + route_part_35,
    "(2, 5)": route_part_13 + route_part_35 + route_part_52,
    "(8, 3)": route_part_13 + route_part_35 + route_part_52 + route_part_24,
    "(0, 2)": route_part_13 + route_part_35 + route_part_52 + route_part_24 + route_part_41},
    {"(6, 6)": route_part_13, "(5, 2)": route_part_13 + route_part_35,
    "(8, 3)": route_part_13 + route_part_35 + route_part_54,
    "(2, 5)": route_part_13 + route_part_35 + route_part_54 + route_part_42,
    "(0, 2)": route_part_13 + route_part_35 + route_part_54 + route_part_42 + route_part_21},
    {"(8, 3)": route_part_14, "(2, 5)": route_part_14 + route_part_42,
    "(6, 6)": route_part_14 + route_part_42 + route_part_23,
    "(5, 2)": route_part_14 + route_part_42 + route_part_23 + route_part_35,
    "(0, 2)": route_part_14 + route_part_42 + route_part_23 + route_part_35 + route_part_51},
    {"(8, 3)": route_part_14, "(2, 5)": route_part_14 + route_part_42,
    "(5, 2)": route_part_14 + route_part_42 + route_part_25,
    "(6, 6)": route_part_14 + route_part_42 + route_part_25 + route_part_53,
    "(0, 2)": route_part_14 + route_part_42 + route_part_25 + route_part_53 + route_part_31},
    {"(8, 3)": route_part_14, "(6, 6)": route_part_14 + route_part_43,
    "(2, 5)": route_part_14 + route_part_43 + route_part_32,
    "(5, 2)": route_part_14 + route_part_43 + route_part_32 + route_part_25,
    "(0, 2)": route_part_14 + route_part_43 + route_part_32 + route_part_25 + route_part_51},
    {"(8, 3)": route_part_14, "(6, 6)": route_part_14 + route_part_43,
    "(5, 2)": route_part_14 + route_part_43 + route_part_35,
    "(2, 5)": route_part_14 + route_part_43 + route_part_35 + route_part_52,
    "(0, 2)": route_part_14 + route_part_43 + route_part_35 + route_part_52 + route_part_21},
    {"(8, 3)": route_part_14, "(5, 2)": route_part_14 + route_part_45,
    "(2, 5)": route_part_14 + route_part_45 + route_part_52,
    "(6, 6)": route_part_14 + route_part_45 + route_part_52 + route_part_23,
    "(0, 2)": route_part_14 + route_part_45 + route_part_52 + route_part_23 + route_part_31},
    {"(8, 3)": route_part_14, "(5, 2)": route_part_14 + route_part_45,
    "(6, 6)": route_part_14 + route_part_45 + route_part_53,
    "(2, 5)": route_part_14 + route_part_45 + route_part_53 + route_part_32,
    "(0, 2)": route_part_14 + route_part_45 + route_part_53 + route_part_32 + route_part_21},
    {"(5, 2)": route_part_15, "(2, 5)": route_part_15 + route_part_52,
    "(6, 6)": route_part_15 + route_part_52 + route_part_23,
    "(8, 3)": route_part_15 + route_part_52 + route_part_23 + route_part_34,
    "(0, 2)": route_part_15 + route_part_52 + route_part_23 + route_part_34 + route_part_41},
    {"(5, 2)": route_part_15, "(2, 5)": route_part_15 + route_part_52,
    "(8, 3)": route_part_15 + route_part_52 + route_part_24,
    "(6, 6)": route_part_15 + route_part_52 + route_part_24 + route_part_43,
    "(0, 2)": route_part_15 + route_part_52 + route_part_24 + route_part_43 + route_part_31},
    {"(5, 2)": route_part_15, "(6, 6)": route_part_15 + route_part_53,
    "(2, 5)": route_part_15 + route_part_53 + route_part_32,
    "(8, 3)": route_part_15 + route_part_53 + route_part_32 + route_part_24,
    "(0, 2)": route_part_15 + route_part_53 + route_part_32 + route_part_24 + route_part_41},
    {"(5, 2)": route_part_15, "(6, 6)": route_part_15 + route_part_53,
    "(8, 3)": route_part_15 + route_part_53 + route_part_34,
    "(2, 5)": route_part_15 + route_part_53 + route_part_34 + route_part_42,
    "(0, 2)": route_part_15 + route_part_53 + route_part_34 + route_part_42 + route_part_21},
    {"(5, 2)": route_part_15, "(8, 3)": route_part_15 + route_part_54,
    "(2, 5)": route_part_15 + route_part_54 + route_part_42,
    "(6, 6)": route_part_15 + route_part_54 + route_part_42 + route_part_23,
    "(0, 2)": route_part_15 + route_part_54 + route_part_42 + route_part_23 + route_part_31},
    {"(5, 2)": route_part_15, "(8, 3)": route_part_15 + route_part_54, 
    "(6, 6)": route_part_15 + route_part_54 + route_part_43, 
    "(2, 5)": route_part_15 + route_part_54 + route_part_43 + route_part_32, 
    "(0, 2)": route_part_15 + route_part_54 + route_part_43 + route_part_32 + route_part_21}]
# значение длины кратчайшего маршрута
short_route = min(finish["(0, 2)"] for finish in all_routes)
# количества возможных маршрутов
total_routes = len(all_routes)
# ищем кратчайшие маршруты для почтальона
i = 0
while i < total_routes:
    if all_routes[i]["(0, 2)"] == short_route:
        print("'(0, 2)'", '->', all_routes[i], '=', short_route)
    i += 1
