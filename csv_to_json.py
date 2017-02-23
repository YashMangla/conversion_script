# Copyright (c) 2017, Yash Mangla and Contributors
# MIT License. See license.txt
'''
    convert comma's separated file to JSON file
'''

import csv
import json

def tsv_to_json(inp, out):
    arr = []
    outFile = open(out, 'wb')
        # here i opened file in Universal mode you can change this according to your requirment.
    with open(inp, 'rU') as csvin:
        csvin = csv.reader(csvin, delimiter=',')
        keys = [i for i in csvin.next()]
        print keys
        for row in csvin:
            x={}
            for i in range(0, len(row)):
                x.setdefault(keys[i], row[i])
            arr.append(x)

    #write output in json file
    json.dump(arr, outFile)

if __name__ == "__main__":
    inp = "sample.csv"
    out = "sample.json"
    tsv_to_json(inp, out)