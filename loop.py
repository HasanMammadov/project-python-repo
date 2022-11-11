names=['andy','david','alex']
namesDict = {}
for i,name in enumerate(names):
    namesDict[name] = i
    print(name, namesDict.get(name))

    # test
    