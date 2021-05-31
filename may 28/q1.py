name = ["alan", "john", "tania", "ahmad", "ali", "muddassar","raheel","hamza"]
age = [12,13,14,15,17,16,13,13]
people = []
def find(a,b):
    for a in range(8):
        j = {}
        j.update({"name": name[a]})
        j.update({"age": age[a]})
        people.append(j)
    print(people)
find(name,age)
