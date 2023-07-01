# DND Translator (v.1)
I made this translator for a dnd spell book, but I guess it works for any kind of CSV, and with some refactoring maybe any table. Currently I'm using LibreTranslate, which has a couple of requirements and was kind of hard for me to run, notice that I have had many troubles with AI installations before, some of its dependencies are quite sensible so make sure you are using a virtual environment. 

The choice of LibreTranslate was made after the first commit, when troubles around the uses of third-party APIs was clear for a tabulation traduction of large data sets.

Its a simple program, you input a csv file, you get a csv file translated. Right now you must pre-select the language in the code, so make sure you are selecting the correct language and that you have that language installed within LibreTranslate.