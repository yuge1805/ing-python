# while
i = 0
while i < 10:
    print(f"i:{i}")
    i += 1
else:
    print(f"finished, i:{i}")

# for
msg = "人生苦短，及时行乐"
for s in msg:
    print(s)
else:
    print(",yuge")

print("for range-----------------------------------")

# for range
for j in range(1, 10):
    print(j)

print("for range, step: 2-----------------------------------")

for j in range(1, 10, 2):
    print(j)