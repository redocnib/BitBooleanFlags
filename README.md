# BitBooleanFlags - Wrapper Syntax'ed [#](https://github.com/redocnib/BitBooleanFlags)

Bit boolean flag wrapper, allows you to store flags inside a single number. 
Each flag uses powers of two, and the number of flags you can store depends on the capacity of the numeric data type.
You can do combined and or operations on the flag as per your requirement, refer examples.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/).

```bash
pip install bit-boolean-flags
```

## Sample

```python
from BitBooleanFlags import BitBooleanFlags
#initialize with a set of static flags which are available to set
BBF = BitBooleanFlags("CREATE_FOLDER","CREATE_FILE","DELETE_FILE","DELETE_FOLDER","KILL_PROCESS","ROOT_ACCESS")
#For example's sake
process1 = 0;
process2 = 0;
process3 = 0;
#add Permissions
process1 = BBF(process1).add("CREATE_FILE","DELETE_FILE")
#Inherit process1 flags and add new ones
process2 = BBF(process2).add("DELETE_FOLDER","CREATE_FOLDER")
#in addition to process 1 and two flags
process3 = BBF(process1,process2).add("KILL_PROCESS","ROOT_ACCESS","ROOT_ACCESS")

print("Permission List with Basic has: ")
for flag in BBF.mappedFlags():
    print("Process 1 => " + flag + " : " + str(BBF(process1).has(flag)))


for flag in BBF.mappedFlags():
    print("Process 2 => "  + flag + " : " + str(BBF(process2).has(flag)))

for flag in BBF.mappedFlags():
    print("Process 3 => "  + flag + " : " + str(BBF(process3).has(flag)))


print("orHas(): ")
print("Process 1 =>  ROOT_ACCESS or CREATE_FILE : "+ str(BBF(process1).orHas("ROOT_ACCESS","CREATE_FILE")))

print("has(): and operation")
print("Process 2 =>  DELETE_FOLDER and CREATE_FOLDER : "+ str(BBF(process2).has("DELETE_FOLDER","CREATE_FOLDER")))

#store process1,process2,process3 in db or another storage medium as it is a number.
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contributors
[Vysakh](https://github.com/vyshuks)

## License
[MIT](https://choosealicense.com/licenses/mit/)
