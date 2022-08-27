#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;

// Struct for storing student data
struct Student {
    string name;
    int marks, age;
};

// Array for student array
// Created on the heap
Student students[100000];

int main() {
    // Take input
    int n;
    cin >> n;
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
