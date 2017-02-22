import csv, json

def tsv_to_json(inp, out):
    arr = []
    outFile = open(out, 'wb')
    with open(inp, 'rb') as tsvin:
        tsvin = csv.reader(tsvin, delimiter='\t')
        keys = [i for i in tsvin.next()]
        print keys
        for row in tsvin:
            x={}
            for i in range(0, len(row)):
                x.setdefault(keys[i], row[i])
            arr.append(x)
    
    #write output in json file
    json.dump(arr, outFile)

if __name__ == "__main__":
    inp = "data.tsv"
    out = "data.json"
    tsv_to_json(inp, out)
