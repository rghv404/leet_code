def flatten_dictionary(dct):
  res = {}

  def helper(hashMap, origKeyStr):
    for key in hashMap:
      if origKeyStr == "":
        newKey = key
      else:
        newKey = origKeyStr + "." + key if key != "" else origKeyStr
      if isinstance(hashMap[key], str):
        res[newKey] = hashMap[key]
      else:
        print(newKey, key)
        helper(hashMap[key], newKey)
  
  for key in dct:
    if isinstance(dct[key], str):
      res[key] = dct[key]
    else:
      helper(dct[key], key)
  
  print(res)
  
  
dct = {
            "" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "" : {
                        "e" : "1"
                    }
                }
            }
        }



dct = {"":{"a":"1"},"b":"3"}

flatten_dictionary(dct)