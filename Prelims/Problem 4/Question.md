# Sorting students

**Problem Statement:** <br>
After retiring from his job, Jeff Bezos decided to settle down as a teacher in the countryside. However, he wasn’t very good at his new job.

On his first day as a teacher, he was given a list of N students. For each student, Jeff was given his/her name, marks, and age. Help Jeff to sort the list of students according to the following criteria:
 - Students with shorter names are placed before students with longer names
 - If 2 students have the same length name, the student with higher marks are placed earlier
 - If 2 students have the same length name and marks, the student with lower age is placed earlier

**Constraints:** <br>
 - 1 &le; _N_ &le; 10<sup>5</sup>
 - _A<sub>i</sub>_ is a single word
 - _A<sub>i</sub>_ &ne; _A<sub>j</sub>_ (1 &le; _i_, _j_ &le; _N_, _i_ != _j_)
 - 1 &le; |_A<sub>i</sub>_| &le; 100
 - 1 &le; _B<sub>i</sub>_, _C<sub>i</sub>_ &le; 10<sup>9</sup>

**Input Format:** <br>
 - The first line contains a single integer _N_
 - The next _N_ lines contain the details of the _N_ students, where each line contains the details of a single student.
 - Line _i_ + 1 contains 3 space-separated tokens _A<sub>i</sub>_, _B<sub>i</sub>_, and _C<sub>i</sub>_, where _A<sub>i</sub>_ is the name of the _ith_ student, _B<sub>i</sub>_ is the marks of the _ith_ student, and _C<sub>i</sub>_ is the age of the _ith_ student.

**Output Format:** <br>
 - Print the names of students sorted according to the criteria in _N_ seperate lines.

**Sample input:** <br>
```
4
ABCD 85 20
QWERTY 72 24
ASDF 96 14
WASD 85 19
```

**Sample output:** <br>
```
ASDF
WASD
ABCD
QWERTY
```