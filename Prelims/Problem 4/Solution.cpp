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
    stable_sort(students, students + n, [](const Student& a, const Student& b) {
        if (a.name.length() != b.name.length()) {
            return a.name.length() < b.name.length();
        }
        if (a.marks != b.marks) {
            return a.marks > b.marks;
        }
        return a.age < b.age;
    });

    // Print the names of the students
    for (Student student : students) {
        cout << student.name << endl;
    }
}