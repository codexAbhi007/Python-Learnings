import json

with open(r'Docs\states.json')as f, open(r'Docs\states_new.json','a') as g:
    data = json.load(f)
    # print(data)
    # print(type(data))

    f.seek(0)
    data2 = json.load(f)

    for state in data2['states']:
        # print(state['name'], state['abbreviation'])
        del state['area_codes']

    json.dump(data2, g,indent=2)


    