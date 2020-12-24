def hello2(s):
    print("Hello " + s)
    print("Glad to meet you")

hello2("Iman" + " and Jackie")
hello2("Class " * 3)

print()
print()

def hello3(s, n):
  greeting = "Hello {} ".format(s)
  print(greeting*n)

hello3("Wei", 4)
hello3("", 1)
hello3("Kitty", 11)
print()
print()

def total(num):
    c = 0
    for n in num:
        c = c + n
    return c
    
lst = [1,2]
print(total(lst))
        
print()
print()


def count(n):
    cou = 0
    for num in n:
        cou = cou + 1
    return  cou

lst = [1,2,3]
n_1 = count(lst)
print(n_1)
print()
print()


def square(x):
  y=x*x 
  return y


def sum_of_squares(x,y,z):
  a = square(x)
  b = square(y)
  c = square(z)


  return a+b+c


a = -5
b = 2
c = 10

result  = sum_of_squares(a,b,c)
print(result)
print()
print()


def most_common_letter(s):
  frequencies = count_freqs(s)
  frequencies_1 = best_key(frequencies)
  return frequencies_1


def count_freqs(st):
  d = {}

  for ch  in st:
     if ch not in d:
       d[ch] = 1
     d[ch] = d[ch] + 1

  return d    

def best_key(st_1):
  key = list(st_1.keys())
  key_0 = key[0]

  for ch_1 in key:
    if st_1[ch_1] > st_1[key_0]:
      key_0 = ch_1
  return key_0



k = most_common_letter("sfhgsdbvdjvuhfsdhfkdshhkjjjjjjjjjjjjjjjhfdvh bs")


print(k)
print()
print()



def addit(n_0):
  n = n_0 + 5
  return n


def mult(n_1):
  n = n_1 * addit(n_1)
  return n


number = mult(10) 
print(number) 
print()
print()


def double(y):
    y = 2 * y

def changeit(lst):
    lst[0] = "Michigan"
    lst[1] = "Wolverines"

y = 5
double(y)
print(y)

mylst = ['our', 'students', 'are', 'awesome']
changeit(mylst)
print(mylst)
print()
print()


def information(txt1,txt2,txt3,txt4):
    return txt1,txt2,txt3,txt4

txt_1 = input("Enter Your Name")
txt_2 = input("Enter Your Birth_year")
txt_3 = input("Enter Your Fav_Color")
txt_4 = input("Enter Hometown")

func = information(txt_1,txt_2,txt_3,txt_4)
print(func)

