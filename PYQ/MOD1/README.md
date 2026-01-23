# Module 1 – Python Programming (KTU S6) - 2019 SCHEME
## Previous Year Question Programs

---

## 🔹 June 2022 Question Paper

## 🅰️ PART A 

### Q1. Write a program to check whether a number is even or odd.

```python
1. What is the output of the following print statement in Python?
(a) print(9//2) (b) print(9/2)
```
### Output
```
(a) 4
(b) 4.5
```

### Q2. Write a Python program to count number of even numbers and odd numbers in a given set of n numbers.
```python
n = int(input("Enter number of elements: "))
even = 0
odd = 0

for i in range(n):
  num = int(input("Enter number: "))
  if num%2 == 0:
    even += 1
  else:
    odd += 1

print("Even numbers count: ", even)
print("Odd numbers count: ", odd)
```

### Output
```
Enter number of elements: 6
Enter number 1: 1
Enter number 2: 2
Enter number 3: 3
Enter number 4: 4
Enter number 5: 5
Enter number 6: 6

Even numbers count: 3
Odd numbers count: 3
```

## 🅰️ PART B

