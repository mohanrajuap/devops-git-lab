student = {
    "name": "mohan",
    "marks": [10, 20, 30, 40],
    "subjects": ("maths", "science", "english")
}

print(student["marks"][1])         # 20
print(student["subjects"][2])      # english

student["marks"].append(95)        # add 95 to marks list

print(student)
