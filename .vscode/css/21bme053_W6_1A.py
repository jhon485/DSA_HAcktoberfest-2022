s = ["Simple ","Anushka","Prerna "]
if len(s)==0:
    print("Empty")
else:
    print("Non Empty")
s.append("Himanshu")
s.append("Ankur")
s.append("Sanika")
s.append("Gaytri")
s.append("Samarth")
s.append("Sambhav")
s.append("Ayush ")
print(len(s))
s.pop(2)
s.pop(5)
s.pop(1)
s.pop(3)
print(s)
s.append("10")
s.append("20")
print(s)
s.clear()
print(s)
