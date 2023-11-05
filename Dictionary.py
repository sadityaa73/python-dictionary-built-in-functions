#creating a dictonary:

fruitname={"a":"apple","b":"ball","c":"cat","d":"dog"};
#execute some buit-in-funciton:

#1.copy():
duplicateDictionary = fruitname.copy();
print("printing after copying dictionary",duplicateDictionary);
print("printng original dictionary",fruitname);

#2.clear():
duplicateDictionary.clear();
print("print duplicateDictonary after using clear() built-in funciton",duplicateDictionary);

#3.formkeys():
seq = ('a','b','c','d');
list1 = [1,2,4,3];
dict1= dict.fromkeys(seq);
print("print formKeys() when only sequence passed as parameter",dict1);
print("printing formkeys() when squence and val both are passed as an parameter",dict1.fromkeys(seq,1));
print("print fromkeys() when val pased as list in parameter",dict1.fromkeys(seq,list1));

#4.get('dictionary'):
test_dict = {'Gfg' : {'is' : 'best'}}
print("print fruitname in get() using from above",fruitname.get("a"));
res = test_dict.get('Gfg');
print("when accessed data from nested dictionary ",res);
print("when accessed data from nested dictionary ",res.get('is'));

#5.items():
number ={"a":1,"b":2,"c":3,"d":4};
print("using items() built-in-function",number.items());

#6.keys():
print("using keys() built-in-function",number.keys());

#7.pop():
print("print dictionary before using pop() built-in-function",number);
print("using pop() buit-in-funciton",number.pop("b"));
print(" printing after using pop() buit-in-funciton",number);

#8.popitem():
print("print numbers before using popitem",number);
print("using popitem() buit-in-funciton",number.popitem())
print("print number after using popitem() built-in-function",number);

#9.setdefault('key',value(optional)):
dict2 ={'a':1,'b':2};
print("printing dict2 before using setdefault()",dict2);
print("using setdefault() built-in-funciton ",dict2.setdefault('c',3));
print('after using setdefault() bilt-in-funciton',dict2);

#10.values():
print("using values() built-in-function",dict2.values());

#11.update('dictionary'):

originalDict ={'a':"aditya",'b':"aashu"};
updateDict ={'a':"aashu",'b':"aditya"};

print("before using update()",originalDict,"and",updateDict);
print(originalDict.update(updateDict));
print("after using update() built-in-funciton",originalDict,"and",updateDict);