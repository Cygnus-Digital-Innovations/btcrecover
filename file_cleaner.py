from itertools import count


t,ta,line=0,0,'dummy'
count1 = 0
with open('rockyou.txt') as f:
    with open('rockyou-alpha.txt','w') as fa:
        while True:
            count1 += 1
            if count1 > 14344391:
                break
            if count1 % 10000 == 0:
                print(count1)
            try:
                line = f.readline().rstrip()
                if not line:
                    continue
                t += 1
                if line.isalpha():
                    ta +=1
                    fa.write(line + '\n')
            except:
                pass
print(t,ta)