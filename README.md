# DRAMA-Stapel-Tekenaar
Generates DRAMA stacks given DRAMA function tables.

**Example:**<br/>
* **Input:**

```
Tabellen van 2. Test2:

Test2:
PAR | ADRES
PARA3 | 1(R8)
PARA2 | 2(R8)
PARA1 | 3(R8)


Test2:
VAR | ADRES
VARA1 | -4(R8)
VARA2 | -2(R8)


Test2:
RES | ADRES
RES1 | 4(R8)
```

* **Output:**

```
Stapel van 2. Test2:

+------------+
|   VARA1   |
+------------+
|           |
+------------+
|   VARA2   |
+------------+
|    TKA    |
+------------+
| VORIGE R8 |  <-- R8
+------------+
|   PARA3   |
+------------+
|   PARA2   |
+------------+
|   PARA1   |
+------------+
|   RES1    |
+------------+
```


## Getting Started

### Prerequisites

* [Python 3.*](https://www.python.org/download/releases/3.0/)

### Installing
```
1. Right click DRAMA-Stapel-Tekenaar.py
2. Click save link as...
3. Save as .py in your preferred destination
```

## Running

* **Running ID3-Automator:**

```
1. Navigate to the directory where you saved DRAMA-Stapel-Tekenaar.py
2. Open the terminal
3. Type python DRAMA-Stapel-Tekenaar.py
4. Follow the on-screen prompt
```


## Contributing

Everyone can contribute.


## Authors

* **Mathijs Hubrechtsen** - *Majority Contributor*


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Acknowledgments

* <a href="https://nl.wikipedia.org/wiki/Drama_(assembleertaal)">DRAMA Assembly</a>: The assembly language that made this project possible.
