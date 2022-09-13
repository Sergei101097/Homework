# import random
#
# o = []
# for i in range(100):
#     pas = random.randint(1,365)
#     o.append(pas)
#
# s = o[0:30]
# c = o[30:61]
#
# print(s,'\n',c)
#     # x=list(map(int, s))
#     # xx =list(map(int, c))
#     # v = sum(x)
#     # vv = sum(xx)
#     # print(v + vv/20)




# import random
#
# outfile = open('wer.txt', 'w')
# for i in range(1,365+1):
#     pas = random.randint(1,365)
#     outfile.write(str(pas) + '\n')



total = []
f = open('wer.txt','r')
m = f.readlines()
for i in m:
    f = i.rstrip('\n')
    total.append(f)

y = total[0:30]
f = total[31:59]
m = total [60:90]
a = total[91:121]
mm = total [122:152]
i = total
ii = total
av = total

print(len(y))
print(len(f))
print(len(m))
print(len(a))
print(len(mm))
print(total)
