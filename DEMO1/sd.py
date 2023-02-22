colors=["Red","Green","Blue"]
print(colors[2])
print(type(colors))
colors.append("pink")
print(colors)
colors.insert(1,"Blue")
print(colors)
#colors.remove("Green","Blue")
print(colors)
print(len(colors))

Student_info= {
    "student_name": "Bob",
    "Student_mail_id": "bob@gmail.com",
    "marks":[90,98,87,67,54],
    "sports":{
        "indoor": "chess",
        "outdoor": "hockey"
    }
}
print(Student_info)
print(type(Student_info["marks"]))
print(Student_info["marks"][2])
all_marks=Student_info["marks"]
print(all_marks[0])
print(Student_info["sports"]["outdoor"])