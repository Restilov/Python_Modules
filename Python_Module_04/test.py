x = "selam"
y = "hi"
z = "resti"
# f = open("file.md", "w")
# print(x,y,z,sep="AAAAA", file=f)
# print("hi")

r = "resti\nselam\ntheexam\npython"

my_list = r.splitlines()
print(*my_list, sep="SELAM")
print(*r.splitlines(), sep="AAA")
print(r.split("\n"))

# e = "HEY".join(x) + "R"
# print(e)