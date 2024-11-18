import json #importar json para manejar la informacion

txt_arch = "arch.txt" #se le asigna una variable al archivo txt para poder invocarlo
json_arch = "arch.json" #se le asigna una variable al archivo json para poder invocarlo

def obtain_soup_info(txt_arch): 
    """
    Obtain information that is in the txt file
    """

    with open(txt_arch) as t: #abre archivo txt en modo lectura
        soup_info = t.read().split("---") #se separa en una lista la sopa de letras y las palabras que se van a buscar en la sopa
    return soup_info

def obtain_letters():
    """
    Function that gets the letters from letters soup in txt file
    by splitting them from each row and culumn into a list
    """

    info = obtain_soup_info(txt_arch) #se le asigna una variable la informacion de la soup_info para las letras
    splitted_letters = [] #una lista vacia para que se alamcene posteriormente las letras separadas de la sopa de letras
    all_letters = info[0].splitlines() #se separan las letras de la sopa por lineas
    for lines in all_letters:
        splitted_letters.append(lines.split(" ")) #cada linea se almacena en la lista de splitted_letters
    return splitted_letters

def obtain_correct_words():
    """
    Function that gets the words that the algoritm is 
    going to check is they are or not in the letter soup
    """

    soup_info = obtain_soup_info(txt_arch) #se le asigna una variable la informacion de la soup_info para las palabras que se van a chekear
    words_to_check = soup_info[1].strip().splitlines() #se separan por lineas pero tambien se eliminan los caracteres especiales para que el algoritmo solo tome las palabras
    return words_to_check



def horizontal_lines(all_letters):
    """
    Function that splits the grid by rows
    (left to right and rigth to left) and
    puts them in a list that holds the 
    posible horizontal words
    """

    posible_horizontal = [] #lista vacia que luego va a almacenar las posibles palabras horizontales en ambas dirwcciones
    for letters in all_letters: 
        posible_horizontal.append("".join(letters))  #normal options; toma todas las posibilidades de la lista de all_letters y las mete en la lista de posible horizontal
        letters.reverse()
        posible_horizontal.append("".join(letters))  #reversed options; ; toma todas las posibilidades de la lista de all_letters y las pone al reves y luego las mete en la lista de posible horizontal
    return posible_horizontal



def vertical_lines(all_letters, num_all_letters): #num_all_letters is the number of rows in the grid        
    """
    function that forms words with each column of the grid
    and holds it in a list
    """
    vertical_options = [] #lista vacia que luego va a almacenar las posibles palabras verticales en ambas dirwcciones
    for column in range(num_all_letters):
        vertical_word = "" #string vacia que luego va a tener cada posibilidad vertical de arriba para abajo
        reversed_word = "" ##string vacia que luego va a tener cada posibilidad vertical de abajo para arriba
        for row in all_letters: #loop que itera por cada row
            vertical_word += row[column]  #el + concatena la posicion indicada de cada row para formar la columna de arriba para abajo
            reversed_word = row[column] + reversed_word #coge la primera posicion de la row pero al sumarla luego, se va al final
        vertical_options.append(vertical_word) #pone las opciones normales en la lista que antes estaba en la lista vacia
        vertical_options.append(reversed_word) #pone las opciones reversiadas en la lista que antes estaba en la lista vacia
    return vertical_options



def possible_lines():
    """
    function that convines all posible 
    horizontal and verticall words in a variable
    """
    all_letters = obtain_letters()
    num_all_letters = len(all_letters[0]) #se saca el numero de elementos en la lista de all letters para usarlo luego en el range de la funcion de vertical_lines
 
    horizontal_words = horizontal_lines(all_letters) 
    vertical_words = vertical_lines(all_letters, num_all_letters)


    total_to_check = horizontal_words + vertical_words #capta todas las posibilidades de palabras en cada columna y row y las junta
    return total_to_check



def check_word(total_to_check, words_to_check):
    """
    function that checks if the correct words 
    are in all the possible words list
    """

    results = {} #diccionario vacio que luego se va a llenar para poner en el archivo json
    for word in words_to_check: #se toma la lista de palabras que se van a buscar en la sopa de eltras
        flag = False #flag que sirva para asignarle a la palabra en caso de no estar en la sopa
        for p_word in total_to_check: 
            if word in p_word: #si la palabra hace parte de las posibles palabras cambia la flag a True y se le asigna la flag a la palabra en el diccionario
                flag = True
                results[word] = flag
        if not flag: 
            results[word] = flag #si la palabra que se esta checkeando de la lista de words_to check no esta en la sopa, se le asigna la bandera de False a la palabra en el diccionario
    return results



def write_in_json_file():
    """
    funtion that writes in the json file  if the
    words form the txt are in the letters soup or not
    """
    results = check_word(possible_lines(), obtain_correct_words()) #a results se le asigna la funcion para poner la informacion en el archivo json posteriormente
    with open(json_arch, "w") as f: #se abre el archivo json en modo escritura ("w")
        json.dump(results, f, indent=4)  #dump hace que se convierta results a formato json y lo indenta 4 espacios

write_in_json_file()