```{python}
data = 1234
print(type(data))

#integer to string
data = str(data)

[i for i in data]

for i in range(10):
    print(i)

for i in data:
    print(i)


print("마지막", data[-1])
print("-"*20)

data_byte = data.encode()
print(type(data))
print(data)
print("-"*20)


# string with byte to decoding string
data_str = data_byte.decode("utf-8")

print(data_byte)
print(data_str)

print(type(data_byte))
print(type(data_str))

print([i for i in data_byte])

for i in data_byte:
    print(i)
print([i for i in data_str])

# string with byte to string
data_list = list(data)

# list to string
data = "".join(data_list)

# string to float
data_float = float(data_str)
```
