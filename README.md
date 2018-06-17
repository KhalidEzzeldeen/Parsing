CYK Parsing Implementation


Programming Language- Python 3.6.1


Overview:


CKY.py
* Class ConverCNF()
   * startSymbolAdd() - function adds a new start symbol if existing symbol already on the right hand side of the rules
   * eliminateEpsilon() - if rule contains any ‘ε’ in the right hand side, it removes and restructure the grammar accordingly
   * eliminateVariableUnit() - This function removes single production non-terminal from the right hand side
   * moveTerminalToUnits() - this function add unit non-terminal for terminals
   * replaceLongProd() - replace any non-terminal production more than 2 are adjusted in the form of A -> B C
* Class CYK()
   * readGrammar() - read input grammar, add the rules as dictionary, where key goes the left-hand side rule and value contains right hand-side rules in a list
   * readString() - read input string from the text files
   * readOutput() - print the modified grammar & CKY table
   * parser() - CKY parser algorithm




Dependencies:


re - should be included with python by default
NLTK-
* Pip3 install nltk


Usage:


* On terminal where the files exist, write command
	Python3 CYK.py <grammar_file_.txt> <string_file_.txt>
* Sample grammar file as included
   * First line contains the start symbol
   * Epsilon defines with ‘ε’ symbol
   * Terminals are separated by single-quote (‘’) e.g. ‘John’, ‘man’
   * Multiple terminals and non-terminals are separated by whitespace
* Sample string file as included- each line contains separate string