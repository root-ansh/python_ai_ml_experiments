

```python
#1+2+3+4+5
```


```python
def myAdd(a,b):
    return a+b

#myAdd(21.5,3)
```


```python
def mySub(bigNo,smallNo):
    return bigNo-smallNo
#mySub(21,50)
```


```python
def myMul(a,b):
    return a*b
```


```python
def myExp(base,power):
    return base**power
#myExp(2,3)
```


```python
def myDiv(num,divider):
    return num/divider # 12/5 =2.4 exact
#myDiv(12,5)
```


```python
def myDivInteger(num,divider):
    return num//divider # 12//5 =2( just the quotent)
#myDivInteger(12,5)
```


```python
def myRemainder(num,divider):
    return num%divider #14%5 =4
#myRemainder(14,5)
```


```python
def concat(a,b):
    return a+b

print(concat("hello",'baby'))
print(concat("hello",'      1'))
print(concat("hello",1))#Error #concatination between different data types not possible only string + char/ string possible
```

    hellobaby
    hello1
    


```python
len("abc")#3
len((2,3))#2
len([111,"ansh",22.3,0,'a'])#5
#will show only the last len value
```




    5




```python
chr(244)
```




    'ô'




```python
ord('@')
```




    64




```python
print(type(123)) #int
print(type(1299999999999999999999999999993)) #still int , their is no long or big integer
print(type(True)) #boolean
print(type(2.41))#float
print(type(24.444444444444123488444444444)) #still float , ther is nodouble
print(type("ansh"))#string
print(type((1,"abc",24.6)))#tuple
print(type(123))#List
print(type({"a":1})) #dictionary

```

    <class 'int'>
    <class 'int'>
    <class 'bool'>
    <class 'float'>
    <class 'float'>
    <class 'str'>
    <class 'tuple'>
    <class 'int'>
    <class 'dict'>
    


```python
True==1 and False==0
```




    True




```python
print("Value is ", round(3.91919001 ,0),"Rounded to",0,"places")
print("Value is ", round(3.91919001 ,1),"Rounded to",1,"places")
print("Value is ", round(3.91919001 ,2),"Rounded to",2,"places")
print("Value is ", round(3.91919001 ,3),"Rounded to",3,"places")
print("Value is ", round(3.91919001 ,4),"Rounded to",4,"places")

```

    Value is  4.0 Rounded to 0 places
    Value is  3.9 Rounded to 1 places
    Value is  3.92 Rounded to 2 places
    Value is  3.919 Rounded to 3 places
    Value is  3.9192 Rounded to 4 places
    


```python
"stone"*3
```




    'stonestonestone'




```python
3*"Story"
```




    'StoryStoryStory'




```python
3*'stone'+'age'
```




    'stonestonestoneage'


