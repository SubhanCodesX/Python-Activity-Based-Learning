n = int(input("Enter number of subjects: "))

if n <= 0:
    print("Enter at least one subject")
else:
    total1 = total2 = 0
    names = []
    marks = []

    for i in range(n):
        name = input("Enter subject name: ")
        m1 = int(input("Assessment 1 marks: "))
        m2 = int(input("Assessment 2 marks: "))

        if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100:
            print("Invalid marks")
            break

        total1 += m1
        total2 += m2
        names.append(name)
        marks.append(m2)

        print("Change in", name, ":", m2 - m1)

    else:
        print("Assessment 1 total:", total1)
        print("Assessment 2 total:", total2)

        if total2 > total1:
            print("Performance improved")
        elif total2 < total1:
            print("Performance declined")
        else:
            print("Performance unchanged")

        lowest = marks.index(min(marks))
        print("Lowest-scoring subject:", names[lowest])