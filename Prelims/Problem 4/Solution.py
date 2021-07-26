def solve():
    # Take input
    n = int(input())
    students = []
    for i in range(n):
        inp = input().split()
        name = inp[0]
        marks = int(inp[1])
        age = int(inp[2])
        students.append([name, marks, age])

    # First sort on basis of age
    students.sort(key = lambda x: x[2])

    # Then sort on basis of marks
    students.sort(key = lambda x: -x[1])

    # Finally sort on basis of name length
    students.sort(key = lambda x: len(x[0]))

    # Print the names of the students
    for student in students:
        print(student[0])

if __name__ == '__main__':
    solve()