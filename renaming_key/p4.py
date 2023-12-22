# Changing the key name from the dictionary

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
def met1():
    sample_dict.pop('city')
    print(sample_dict)
    sample_dict.update({"location":"New york"})
    print(sample_dict)

# met1()

def met2():
    del sample_dict['city']
    print(sample_dict)
    sample_dict.update({"location":"New york"})
    print(sample_dict)
    
# met2()

def met3():
    sample_dict["location"]=sample_dict["city"]
    del sample_dict["city"]
    print(sample_dict)
    
# met3()

if __name__ == "__main__":
    met2()
    # met1()
    # met3()