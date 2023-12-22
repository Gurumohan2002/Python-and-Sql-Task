# Getting the key from the dictionary which has lowest mark in it.

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

a=list(sample_dict.values())

def met1():
    x=a.index(min(a))
    key, value = list(sample_dict.items())[x]
    print(key)

def met2():
    for key,value in sample_dict.items():
        if value == min(a):
            print(key)

if __name__ == "__main__":
    met2()
    # met1()
    
    