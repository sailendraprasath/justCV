import pandas as pd

data = {
    "Name":["Benjamin","Francis","Hannah","Isabella","James"],
    "Marks":[85,90,33,88,92]
}

data_frame = pd.DataFrame(data)

data_frame["Passed"] = data_frame["Marks"] >= 35 

def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 50:
        return 'C'
    else:
        return 'D'
    
data_frame["Grade"]  = data_frame["Marks"].apply(get_grade)

# print(data_frame)

print("All Students:\n", data_frame)

print("\nFailed Students:\n", data_frame[data_frame["Passed"] == False])