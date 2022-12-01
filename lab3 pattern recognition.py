import numpy as np  # используется с методами dot, eye, zeros, linalg.inv
import math # для извлечения корня

#Зададим элементы классов
o_1 = [0, 0, 1, 0, 0,
      0, 1, 0, 1, 0,
      0, 1, 0, 1, 0,
      0, 1, 0, 1, 0,
      0, 0, 1, 0, 0]
o_2 = [0, 1, 1, 1, 0,
      0, 1, 0, 1, 0,
      0, 1, 0, 1, 0,
      0, 1, 0, 1, 0,
      0, 1, 1, 1, 0]
o_3 = [0, 0, 0, 0, 0,
      0, 1, 1, 1, 0,
      0, 1, 0, 1, 0,
      0, 1, 1, 1, 0,
      0, 0, 0, 0, 0]

c_1 = [0, 1, 1, 1, 0,
       0, 1, 0, 0, 0,
       0, 1, 0, 0, 0,
       0, 1, 0, 0, 0,
       0, 1, 1, 1, 0]
c_2 = [0, 0, 1, 0, 0,
       0, 1, 0, 1, 0,
       0, 1, 0, 0, 0,
       0, 1, 0, 1, 0,
       0, 0, 1, 0, 0]
c_3 = [0, 0, 1, 0, 0,
       0, 1, 0, 1, 0,
       0, 1, 0, 0, 0,
       0, 1, 0, 0, 0,
       0, 0, 1, 1, 0]

x1 = [1, 0, 0, 0, 1,
      0, 1, 0, 1, 0,
      0, 0, 1, 0, 0,
      0, 1, 0, 1, 0,
      1, 0, 0, 0, 1]
x2 = [0, 1, 0, 1, 0,
      0, 1, 0, 1, 0,
      0, 0, 1, 0, 0,
      0, 1, 0, 1, 0,
      0, 1, 0, 1, 0]
x3 = [0, 0, 0, 0, 0,
      0, 1, 0, 1, 0,
      0, 0, 1, 0, 0,
      0, 1, 0, 1, 0,
      0, 0, 0, 0, 0]

def evklid(MY_CLASS):
    covar_MY_CLASS, ed_matrix, result_matrix = MY_CLASS.covar(), np.eye(25), np.zeros((25,25)) # матрица ковариаций для класса и создание диагональной матрицы с использованием модуря numpy as np, создание нулевой матрицы 25 на 25 с использованием модуря numpy as np
    for i in range(25):     # заполнение матрицы (матрица ковариации + единичная)
        for j in range(25):
            result_matrix[i][j] = covar_MY_CLASS[i][j] + ed_matrix[i][j]
    return result_matrix
def print_matrix(M): # вывод матрицы в столбик
    for i in M:
        print(i)
def find_distance(new_el, nucl): # поиск разности между новым элементом и ядром, где первое - элемент, второе - ядро
    d = np.zeros(25) # создание нулевого вектора из 25 элементов
    for i in range(5**2):
        d[i] = new_el[i] - nucl[i]
    return d
def t_v(vector):   # транспонирование вектора
    result = []
    for i in vector:
        result.append([i])
    return result
def m_d(d, obr_m_cov): # m_d((x-y), матрица обратная ковариац+единичная матрица)
    xy = t_v(d)  # (x-y)T транспонированная матрица расстояния
    mm = np.dot(obr_m_cov,xy)    # произведерние вектора на матрицу с помощью встроенного модуля numpy as np
    pp = np.dot(d, mm)       # умножение матрицы на вектор (эта и предыдущая строки - промежуточные вычисления)
    result = math.sqrt(pp)   # окончательно расстояние Махаланобиса по формуле (слайд 12 лекции)
    return result
def find_min(c, new_e):
    min_amount, class_min = 1000, ''
    for i in (c.keys()):
        if i == 'OSHKY':
            if min_amount > m_d(find_distance(new_e, O.nucleus), obr_matrix_O):
                min_amount = m_d(find_distance(new_e, O.nucleus), obr_matrix_O)
                class_min = i
        elif i == 'IKSY':
            if min_amount > m_d(find_distance(new_e, X.nucleus), obr_matrix_X):
                min_amount = m_d(find_distance(new_e, X.nucleus), obr_matrix_X)
                class_min = i
        elif i == 'CSHKI':
            if min_amount > m_d(find_distance(new_e, C.nucleus), obr_matrix_C):
                min_amount = m_d(find_distance(new_e, C.nucleus), obr_matrix_C)
                class_min = i
    if min_amount >= 2.5: #Если расстояние слишком велико
        return 0
    return {class_min: min_amount}
class CENTER_OF_LOGIC():  # класс содержить все элементы определенного класса
    def appenD (self, matrix_value):    # добавление элемента к классу
        self.value.append(matrix_value)
    def __init__(self):
        self.value = []                 # список элементов класса
        self.nucleus = np.zeros(25)  # ядро сначала нулевое, ниже - фуннкция поиска ядра класса
    def f_nucleus(self): # поиск ядра класса
        for i in range(5**2):   # получаем каждый из 25 элементов ядра
            tmp = 0             # обнуляем переменную, которая будет содержать искомый элемент ядра
            for k in range(len(self.value)):    # рассматриваем каждый элемент из класса
                tmp += self.value[k][i]         # добавляем в tmp i-тый элемент каждого элемента класса
            self.nucleus[i] = tmp/len(self.value)   # элементом ядра становится тмп деленое на кол-во элементов класса
    def covar(self):    # создание матрицы ковариации
        covar_matrix = np.zeros((25, 25)) #матрица ковариации из нулей размером 25x25
        N = len(self.value) # количество элементов класса
        for i in range(5**2): #по горизонтали
            for j in range(5**2):   # по вертикали
                tmp = 0 # части формулы
                for k in range(len(self.value)):
                    tmp += (self.value[k][i] - self.nucleus[i]) * (self.value[k][j] - self.nucleus[j])  # часть формулы
                covar_matrix[i][j] = (1/N-1) * tmp  # вся формула
        return covar_matrix

# Наполнение классов созданными элементами
O = CENTER_OF_LOGIC()
O.appenD(o_1)
O.appenD(o_2)
O.appenD(o_3)

C = CENTER_OF_LOGIC()
C.appenD(c_1)
C.appenD(c_2)
C.appenD(c_3)

X = CENTER_OF_LOGIC()
X.appenD(x1)
X.appenD(x2)
X.appenD(x3)

O.f_nucleus()    # нашли ядро для класса O
C.f_nucleus()
X.f_nucleus()

# Поиски обратных матриц от евклидовых (матрица ковариации + единичная матрица) для каждого из классов
obr_matrix_O = np.linalg.inv(evklid(O))   # обратная матрица с использованием модуря numpy as np
obr_matrix_C = np.linalg.inv(evklid(C))
obr_matrix_X = np.linalg.inv(evklid(X))

# словарь по ключу-названия класса хранит обратную от евклидовой матрицы для этого класса, буду использовать в функции поиска кратчайшего
classes = {'OSHKY': obr_matrix_O, 'IKSY': obr_matrix_X, 'CSHKI': obr_matrix_C}

# Создание нового элемента
new_x = [0, 0, 0, 0, 0,
         0, 1, 0, 1, 0,
         0, 1, 1, 1, 0,
         0, 1, 0, 1, 0,
         0, 0, 0, 0, 0]
if find_min(classes,new_x) == 0:
    print('Расстояние от new_x до существующих классов слишком велико, не можем отнести его ни к одному из них.')
else:
    print(f'Ваш список new_x ближе к классу {list(find_min(classes, new_x).keys())[0]}, расстояние до этого класса: {list(find_min(classes, new_x).values())[0]}')
new_c = [0, 0, 1, 1, 0,
         0, 1, 0, 0, 0,
         0, 1, 0, 0, 0,
         0, 1, 0, 0, 0,
         0, 0, 1, 1, 0]
if find_min(classes,new_c) == 0:
    print('Расстояние от new_c до существующих классов слишком велико, не можем отнести его ни к одному из них.')
else:
    print(f'Ваш список new_c ближе к классу {list(find_min(classes, new_c).keys())[0]}, расстояние до этого класса: {list(find_min(classes, new_c).values())[0]}')
new_z = [1, 1, 1, 1, 1,
         0, 0, 0, 1, 1,
         0, 0, 1, 0, 0,
         0, 1, 0, 0, 0,
         1, 1, 1, 1, 1]

if find_min(classes,new_z) == 0:
    print('Расстояние от new_z до существующих классов слишком велико, не можем отнести его ни к одному из них.')
else:
    print(f'Ваш список new_z ближе к классу {list(find_min(classes, new_z).keys())[0]}, расстояние до этого класса: {list(find_min(classes, new_z).values())[0]}')
