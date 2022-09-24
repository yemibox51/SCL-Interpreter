# Concepts of Programming Languages 1st Deliverable
###### tags: `Concepts-of-Programming-Languages`

## Task
- Analyze text file and return the tokens of the .scl 
    - Tokens
        - Keywords
        - Identifiers
        - Values
        - Operators
        - Constants
        - Special Characters

### Understanding the output
```scl
/*
 Program     : welcome.scl
 Author      : J M Garrido, November 17, 2016.
 Description : Display welcome message on the screen
    and the value of variable x.
 */
import "scl.h"
implementations
function  main is
variables
    define x of type double   // a variable declaration 
	define t of type double   // time of the second event
	define  pt pointer of type double
begin      
    display "Welcome to the world of SCL"
    set x = 45.95             // assigns a value to variable x 
    display "Value of x: ", x
	input "type value of t: ", t
	display "The value of t is: ", t
	if x >= t then
	   display t
	else 
	   display x
	endif
	if  not x greater or equal t then
	  display x
	endif
    return 0                  // execution terminates OK 
endfun main
```

#### Identifiers
- `main`
- `x`
#### Keywords (ALL CAPS)(Tokens)
- `import`


## Example Work
### Report
![](https://i.imgur.com/3AxpMmN.png)
![](https://i.imgur.com/Sl6FF5i.png)
![](https://i.imgur.com/qR0NbSM.png)
![](https://i.imgur.com/38xQJEI.png)
![](https://i.imgur.com/S5AdQjP.png)
![](https://i.imgur.com/sBwNWXr.png)
Must be in APA format

### Code
![](https://i.imgur.com/rUr6vBo.png)
---
![](https://i.imgur.com/GnWKV0m.png)

### Output
![](https://i.imgur.com/C9dz3tS.png)
---
![](https://i.imgur.com/Fk5aQxs.png)


