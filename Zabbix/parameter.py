import sys
import json
import random


if (sys.argv[1] == 'print'):
    if (sys.argv[2] == 'random_int_value'):
        print(random.randint(0, 100))
elif (sys.argv[1] == 'create_items'):
    array_items = []
    for i in range(1, (int(sys.argv[2]))):
        row = {}
        row["{#ITEMNAME}"] = "Otus_important_metrics_"
        row["{#ITEMTYPE}"] = "random_int_value"
        row["{#ITEMNUMBER}"] = i
        array_items.append(row)
    print(json.dumps(array_items))
    
