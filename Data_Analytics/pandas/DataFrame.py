import pandas as pd

data = {
    "Name":["Sailesh","Indra","Hema"],
    "Age":[20,43,18],
    "City":["Madurai","Thathaneri","BharathiNagar"]
}

df = pd.DataFrame(data)
print(df)