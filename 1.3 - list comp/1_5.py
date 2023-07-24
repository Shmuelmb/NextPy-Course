f = open("names.txt", "r")
names = f.readlines()

# 1
print(max(names))  # Vladimir

# 2
print(len("".join(([name.replace('\n', '') for name in names]))))  # 38

# 3
print('\n' + "".join([name for name in names if len(min(names, key=len))
      == len(name.replace('\n', ''))]))  # Ed, Jo

# 4
with open("short_names.txt", "w") as f:
    f.write("\n".join([str(len(name.replace('\n', '')))
            for name in names]))

# 5
input_num = int(input("\nenter len number: "))
print("\n".join([name.replace('\n', '')
      for name in names if len(name.replace('\n', '')) == input_num]))
