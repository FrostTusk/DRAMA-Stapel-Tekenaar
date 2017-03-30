[!] IMPORTANT [!]

I did not write the .exe version myself. I used cython to convert the python version into a c version.
This version was then compiled using the built in C compiler for VS2015. When doing so I had to
copy a lot of the built header files and other system files to the directory used for compilation.

However when compiling I received this error: 
	UpdatedFramework.c(959): fatal error C1083: Cannot open include file: 'structmember.h': No such file or directory
*Note* the name UpdatedFramework.c is the name of the C version.
To fix this I changed line 959 of the C Version, <structmember.h> to "structmember.h" .

When doing so, the program compiled, but I still received the following warnings:
	UpdatedFramework.c(25415): warning C4293: '<<': shift count negative or too big, undefined behavior
	UpdatedFramework.c(25425): warning C4293: '<<': shift count negative or too big, undefined behavior
	UpdatedFramework.c(25435): warning C4293: '<<': shift count negative or too big, undefined behavior
I do not know what they are, but it compiled and the .exe version SEEMS to work.
If you know what these warnings are, please let me know!

	
What I'm trying to get at is this: 
	[!][!][!] I CANNOT GUARANTEE THAT THE .EXE VERSION WORKS PROPERLY! [!][!][!]
	I AM 95% SURE IT DOES, BUT NOT 100% DUE TO THE ABOVE ERRORS.
	THERE SHOULD BE NO SIMILAR PROBLEM WITH THE .PY VERSION!