import copy
from operator import itemgetter
start=[[1, 2, 3], [8, 0, 4], [7, 6, 5]]
target=[[5, 3, 4], [6, 0, 7], [8, 2, 1]]
story, steps=[], 0

def left_rule(s, t1, t2):
    s[t1][t2], s[t1][t2-1]=s[t1][t2-1], s[t1][t2]
    return s
def up_rule(s, t1, t2):
    s[t1][t2], s[t1-1][t2]=s[t1-1][t2], s[t1][t2]
    return s
def right_rule(s, t1, t2):
    s[t1][t2], s[t1][t2+1]=s[t1][t2+1], s[t1][t2]
    return s
def down_rule(s, t1, t2):
    s[t1][t2], s[t1+1][t2]=s[t1+1][t2], s[t1][t2]
    return s

def evristic1(s, f):
    c=0
    for i in range(3):
        for j in range(3):
            if s[i][j]!=f[i][j]:
                c+=1
    return c

def search_zero_position(s):
    if 0 in s[0]:
        return 0, s[0].index(0)
    elif 0 in s[1]:
        return 1, s[1].index(0)
    else:
        return 2, s[2].index(0)

def check(s, last_step, deep, distance):
    global story, target, steps
    print('Step: ', steps, 'Deep:', deep, "Distance: ", distance, s)
    steps+=1
    if deep>1000:
        return 0
    if story.count(s)==1:
        return 0
    elif s==target:
        print('ПОБЕДА!')
        return 1
    else:
        story.append(s)
        t1, t2 = search_zero_position(s)
        r1, r4, r2, r3=0, 0, 0, 0
        s_r1, s_r2, s_r3, s_r4= 'error', 'error', 'error', 'error'
        if last_step!='left' and t2!=2:
            new_list = copy.deepcopy(s)
            s_r1=right_rule(new_list, t1, t2)
            r1=evristic1(s_r1, target)
        if last_step!='right' and t2!=0:
            new_list = copy.deepcopy(s)
            s_r2=left_rule(new_list, t1, t2)
            r2=evristic1(s_r2, target)
        if last_step!='down' and t1!=0:
            new_list = copy.deepcopy(s)
            s_r3=up_rule(new_list, t1, t2)
            r3=evristic1(s_r3, target)
        if last_step!='up' and t1!=2:
            new_list = copy.deepcopy(s)
            s_r4=down_rule(new_list, t1, t2)
            r4=evristic1(s_r4, target)
        hey=[[r1, s_r1, 'right'],[r2, s_r2, 'left'],[r3,s_r3,'up'],[r4,s_r4, 'down']]
        #print(hey)
        hey=sorted(hey, key=itemgetter(0))
        if hey[0][1]!='error':
            if check(hey[0][1], hey[0][2], deep+1, hey[0][0])==1:
                return 1
        if hey[1][1]!='error':
            if check(hey[1][1], hey[1][2], deep+1, hey[1][0])==1:
                return 1
        if hey[2][1]!='error':
            if check(hey[2][1], hey[2][2], deep+1, hey[2][0])==1:
                return 1   
        if hey[3][1]!='error':
            if check(hey[3][1], hey[3][2], deep+1, hey[3][0])==1:
                return 1
    
            
if check(start, 'none', 0, evristic1(start, target))==1:
    print('УРА!')






def evristic2(s, f):
    c=0
    for i in range(3):
        for j in range(3):
            z=False
            for k in range(3):
                for t in range(3):
                    if s[i][j]==f[k][t]:
                        z=True
                        c=c+abs(k-i)+abs(t-j)
                        break
                if z==True:
                    break
    return c





def check1(s, last_step, deep, distance):
    global story, target, steps
    print('Step: ', steps, 'Deep:', deep, "Distance: ", distance, s)
    steps+=1
    if deep>1005:
        return 0
    if story.count(s)==1:
        return 0
    elif s==target:
        print('ПОБЕДА!')
        return 1
    else:
        story.append(s)
        t1, t2 = search_zero_position(s)
        r1, r4, r2, r3=0, 0, 0, 0
        s_r1, s_r2, s_r3, s_r4= 'error', 'error', 'error', 'error'
        if last_step!='left' and t2!=2:
            new_list = copy.deepcopy(s)
            s_r1=right_rule(new_list, t1, t2)
            r1=evristic2(s_r1, target) 
        if last_step!='right' and t2!=0:
            new_list = copy.deepcopy(s)
            s_r2=left_rule(new_list, t1, t2)
            r2=evristic2(s_r2, target) 
        if last_step!='down' and t1!=0: 
            new_list = copy.deepcopy(s)
            s_r3=up_rule(new_list, t1, t2)
            r3=evristic2(s_r3, target) 
        if last_step!='up' and t1!=2:
            new_list = copy.deepcopy(s)
            s_r4=down_rule(new_list, t1, t2)
            r4=evristic2(s_r4, target) 
        hey=[[r1, s_r1, 'right'],[r2, s_r2, 'left'],[r3,s_r3,'up'],[r4,s_r4, 'down']]
        #print(hey)
        hey=sorted(hey, key=itemgetter(0))
        if hey[0][1]!='error':
            if check1(hey[0][1], hey[0][2], deep+1, hey[0][0])==1:
                return 1
        if hey[1][1]!='error':
            if check1(hey[1][1], hey[1][2], deep+1, hey[1][0])==1:
                return 1
        if hey[2][1]!='error':
            if check1(hey[2][1], hey[2][2], deep+1, hey[2][0])==1:
                return 1   
        if hey[3][1]!='error':
            if check1(hey[3][1], hey[3][2], deep+1, hey[3][0])==1:
                return 1


#if check1(start, 'none', 0, evristic2(start, target))==1:
#    print('УРА!')    
