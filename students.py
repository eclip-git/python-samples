
students = {"andy": {"id": 1001, "age": 24},
            "james": {"id": 1002, "age": 22},
            "mary": {"id": 1003, "age": 25}}


def enroll(name, age):
    if name not in students:
        ids = len(students)+1
        info = {"id": (ids+1000), "age": age}
        students[name] = info
        print(f"{name} now enrolled as {students[name]}")
    else:
        students[name]["age"] = age
        print(f"updated {name} enrollment to {students[name]}")


enroll("jim", 24)
enroll("james", 25)
enroll("bobo", 26)
enroll("bobo", 27)


