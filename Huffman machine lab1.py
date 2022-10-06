import random
N=4 #Задаем размер таблицы и кол-во функций
K=2 #Задаем K
def generation(N, K): #функция по созданию таблицы NxN с K единицами
    m= [[0] * N for i in range(N)] #матрица с будущими 1 и 0
    temp_massive=[0]*N #массив, вычисляющий количество единиц в столбце соответствующего индекса
    for i in range(N): #перебор N строк
        for j in range(K): #добиваемся случайным образом K единиц в строке
            red_line=0 #переменная, которая определяет ошибку и зацикливание
            while True: #"бесконечный" цикл в котором определяем места единиц(ы)
                temp=random.randint(0, N-1)#случайным образом подбираем место единицы от 0 до N-1 (т.к. массив до N-1)
                if temp!=i and temp_massive[temp]!=K and m[i][temp]!=1:#temp!=i проверка, что место выбранное случайно не на диагонали, temp_massive[temp]!=K проверка, что в столбце не больше K единиц, m[i][temp]!=1 проверка, что на этом месте не 1
                    m[i][temp]=1 #изменение цифры в матрице
                    temp_massive[temp]+=1 #добавление единицы в числе единиц столбца temp
                    break #выход из while
                else:
                    red_line+=1 #увеличивается red_line, так как есть риск зацикливания
                #print(temp, m)
                if red_line>N**2: #если red_line превышает предел, тогда делаем проверку теоретической возможности поставить 1 в этой строке
                    z=0 #маркер типа flag
                    for t in range (N): #проверка каждого места в строке
                        if temp_massive[t]!=K and m[i][t]==0 and t!=i: #проверка на количество единиц, диагональ и единицу на проверяемой позиции
                            z+=1 #если есть возможность поставить единицу, то изменяем flag
                    if z==0:#flag не был изменен, 1 некуда поставить
                        return 0#если flag не был изменен, то прерываем функцию и потом мы запустим её заново
                    else: #если 1 есть где поставить продолжаем случайный подбор
                        red_line=0
    return m #возврат конечной матрицы
while True: #"бесконечный" цикл в связи с отсутствием данных, когда нам попадется "правильная" матрица в связи с случайностью
    m = generation(N, K)#запуск матрицы
    if m!=0:#если матрица была возвращена (не 0), тогда прерываем цикл
        break
    
#for _ in range(N): #вывод матрицы
#    print(m[_])

#Объявление функций при K=2:
def f1_1(a, b): # A ∨ B
    if int(a) or int(b):
        return 1
    return 0
def f2_1(a, b):#функция A ∧ B
    if int(a) and int(b):
        return 1
    return 0
def f3_1(a, b):# функция ¬A ∨ B
    if not(int(a)) or int(b):
        return 1
    return 0
def f4_1(a, b): #функция A ⊕ B
    if int(a)+int(b)%2==1:
        return 1
    return 0
def f5_1(a, b): # A ∧ ¬B
    if int(a) and not(int(b)):
        return 1
    return 0

#Объявление функций при K=3:
def f1_2(a, b, c): # A ∨ B ∨ C
    if int(a) or int(b) or int(c):
        return 1
    return 0
def f2_2(a, b, c):#функция A ∧ B ∧ C
    if int(a) and int(b) and int(c):
        return 1
    return 0
def f3_2(a, b, c):# функция ¬A ∨ B ∨ C
    if not(int(a)) or int(b) or int(c):
        return 1
    return 0
def f4_2(a, b, c): #функция A ⊕ B ⊕ C
    if int(a)+int(c)+int(b)%2==1:
        return 1
    return 0
def f5_2(a, b, c): # A ∧ ¬B ∧ C
    if int(a) and not(int(b)) and int(c):
        return 1
    return 0

def g(m, c1, N, K): #функция по генерации следующего элемента
    t='' #сюда будем его записывать
    if K==2: #проверка количества единиц в строках матрицы
        for v in range(N): #перебираем номер функции и её строку в матрице
            for i in range(N-1):#поиск единицы
                for j in range(i+1, N):#поиск второй единицы
                    if m[v][i]==1 and m[v][j]==1:#проверка единиц
                        if v==0:#в строках ниже подбор соответствующей функции и передача соответствующих значений строки c1
                            t=t+str(f1_1(c1[i], c1[j]))
                        if v==1:
                            t=t+str(f2_1(c1[i], c1[j]))
                        if v==2:
                            t=t+str(f3_1(c1[i], c1[j]))
                        if v==3:
                            t=t+str(f4_1(c1[i], c1[j]))
                        if v==4:
                            t=t+str(f5_1(c1[i], c1[j]))
    if K==3: #те же операции, что и выше
        for v in range(N): 
            for i in range(N-2):
                for j in range(i+1, N-1):
                    for k in range(j+1, N):
                        if m[v][i]==1 and m[v][j]==1 and m[v][k]==1:
                            if v==0:
                                t=t+str(f1_2(c1[i], c1[j], c1[k]))
                            if v==1:
                                t=t+str(f2_2(c1[i], c1[j], c1[k]))
                            if v==2:
                                t=t+str(f3_2(c1[i], c1[j], c1[k]))
                            if v==3:
                                t=t+str(f4_2(c1[i], c1[j], c1[k]))
                            if v==4:
                                t=t+str(f5_2(c1[i], c1[j], c1[k]))
    return t #возврат строки 

def distributor(c1, m, N, K, final_massive_position):# функция расспределения по другим функциям
    global final_massive 
    for j in range((2**N)*2): #максимальное число различных элементов 16
        final_massive[final_massive_position].append(g(m, final_massive[final_massive_position][-1], N, K)) #генерация комбинации и добавление её в финальный набор                

final_massive=[[] for i in range(2**N)]#массив наборов комбинаций 
future_massive=[]

for i in range(2**N):#составление всех возможных изначальных бинарных наборов
    c1=bin(i)[2:]#перевод в нормальный вид
    for _ in range(N-1):#добавление незначащих нулей
        if len(c1)!=N:
            c1='0'+c1
    future_massive.append(c1)
    final_massive[i].append(c1)
    distributor(c1, m, N, K, i)

#print(final_massive)
#НА ДАННЫЙ МОМЕНТ У НАС СФОРМИРОВАЛСЯ МАССИВ С ЭЛЕМЕНТАМИ, ОСТАЛОСЬ НАЙТИ АТТТРАКТОРЫ ВО ВСЕХ ПОДМАССИВАХ
#print(future_massive)
#Начинаем поиск аттракторов
    
attractors=[]#массив для аттракторов
for i in range(2**N): #перебор элементов списка final_massive
    for j in range(2**N): #поиск возможных аттракторов 
        if final_massive[i].count(future_massive[j])>1:#если количество элементов равных элементу future_massive[j] больше 2, значит есть аттрактор
            t=0 #калькулятор элементов равных future_massive[j]
            for _ in range((2**N)*2+1): #перебор всех элементов для нахождения индекса второго элемента, равного future_massive[j]
                if final_massive[i][_]==future_massive[j]: #если элемент равен увеличиваем количество элементов
                    t+=1
                    if t==2:
                        break
            attractors.append(final_massive[i][(final_massive[i].index(future_massive[j])):_])#добавление аттрактора
            break
#print(attractors)
#У нас есть массив со всеми аттракторами, осталось найти количество различных

count=0
for i in range(2**N):
    flag=True #flag-показатель уникальности аттрактора
    for j in range(i+1, 2**N):
        if attractors[i]==attractors[j]:#если он не уникальный, тогда
            flag=False
            break
    if flag==True:
        count+=1
print(count)


#Ниже код с поиском уникальных элементов списка из интернета
#def get_unique_numbers(numbers):
#    unique = []
#    for number in numbers:
#        if number in unique:
#            continue
#        else:
#            unique.append(number)
#    return unique
#print(len(get_unique_numbers(attractors)))

