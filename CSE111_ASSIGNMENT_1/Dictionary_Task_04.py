# Solution to Task 4 (Dict)

key_dict = {" ": 0, ".,?!:": 1, "ABC": 2, "DEF": 3, "GHI": 4, "JKL": 5, "MNO": 6, "PQRS": 7, "TUV": 8, "WXYZ": 9}
[[print(str(k)*(j.index(i)+1), end="") for j, k in key_dict.items() if i in j]for i in input().upper()]
