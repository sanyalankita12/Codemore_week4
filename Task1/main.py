import module_customed
import pandas as pd

print("=== Using Custom Module ===")

print("Addition:", module_customed.add(10, 5))
print("Subtraction:", module_customed.subtract(10, 5))
print("Multiplication:", module_customed.multiply(10, 5))
print("Division:", module_customed.divide(10, 5))

print("\n=== Using Pandas Package ===")

student_data = {
    "Name": ["Rahul", "Aman", "Priya"],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(student_data)

print(df)