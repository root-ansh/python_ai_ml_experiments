
**01**  
Regex to replace every uppercase character in a string with  some value x.  
language: **python3**  

```python
import re
string = "'I AM NOT YELLING 1234 !', she said. Though we knew it 441 to be not true. 'listen to yourself', 101 Ram said monotonically. 999"
res = re.sub("[A-Z]", "#", string)
print(res)
```

output :   
```
'# ## ### ####### 1234 !', she said. #hough we knew it 441 to be not true. 'listen to yourself', 101 #am said monotonically. 999
```

---  
