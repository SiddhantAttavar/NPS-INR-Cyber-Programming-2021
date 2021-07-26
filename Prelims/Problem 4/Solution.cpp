#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;

struct Student {
    string name;
    int marks, age;
};

int main() {
    // Take input
    int n;
    cin >> n;
    Student students[n];
    for (int i = 0; i < n; i++) {
        cin >> students[i].name >> students[i].marks >> students[i].age;
    }

    // First sort by age
    sort(students, students + n, [](const Student& a, const Student& b) {
        return a.age < b.age;
    });

    // Then sort by marks
    sort(students, students + n, [](const Student& a, const Student& b) {
        return a.marks > b.marks;
    });

    // Finally sort by name length
    sort(students, students + n, [](const Student& a, const Student& b) {
        return a.name.length() < b.name.length();
    });

    // Print the names of the students
    for (Student student : students) {
        cout << student.name << endl;
    }
}