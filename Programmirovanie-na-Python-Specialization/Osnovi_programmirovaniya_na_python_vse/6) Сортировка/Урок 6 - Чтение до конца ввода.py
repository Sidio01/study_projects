fin = open('input.txt', 'r', encoding='utf8')
# a = int(fin.readline())
# b = int(fin.readline())
# print(a + b)
# lines = fin.readlines()
# print([lines[0].strip(), lines[1].strip()])
# for line in fin:
#     print(int(line) + 1)
# f = fin.read()
# print([f])
fout = open('output.txt', 'w', encoding='utf8')
print(sum(map(int, fin.readlines())), file=fout)
fout.close()
