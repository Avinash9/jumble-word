
import sys

'''
*Approach Applied
1.Put all th words from txt file into a list
2.construct a python dictionary from list of words 
    eg: given word 'ateh'
        calculate length 4
        sort the word 'aeht'
        now dict is
        key is sorted word and values are in list with
        words from list
        {'aeth':['hate','thae',heat','eath']
        },{'....':['....','....']}
3.now sort the given word and search for the key
    equal to the sorted word
4.print all the values of the desired key
'''

def get_list_of_words(filepath):
    '''
    This method after reading all the words from 
    dictionary.txt , returning all words into a list 
    '''
    open_file=open(filepath, "r").read()
    list_of_all_words=open_file.split('\r\n')
    list_of_words_without_null=filter(lambda x: len(x)>0, list_of_all_words)
    return list_of_words_without_null

def get_words_dict(length_of_word,list_of_all_words):
    '''
    This methods takes two parameters length of
    word for which we are are looking possible words
    and list of all words from dictionary.txt
    and returns a python dictionary of all the words
    having same length as of given word
    
    '''
    dict_of_possible_outcomes={}
    for word in list_of_all_words:
        if len(word)==length_of_word:
            s_word=list(word)
            s_word.sort()
            sorted_word=''.join(s_word)
            if len(dict_of_possible_outcomes)==0:
                dict_of_possible_outcomes[sorted_word]=[word]
            else:
                count=0
                if sorted_word in dict_of_possible_outcomes.keys():
                    count=1
                for k,v in dict_of_possible_outcomes.iteritems():
                    if k==sorted_word and count==1:
                        v.append(word)
                    elif count==0:
                        dict_of_possible_outcomes[sorted_word]=[word]
                        break;
    return dict_of_possible_outcomes

def find_possible_words(word,list_of_all_words):
    '''
        This method after getting dict of possible outcomes 
        searches for desired key and return all the possible
        words is non empty other wise return "".
    '''
    list_of_possible_words=[]
    s_word=list(word)
    s_word.sort()
    sorted_word=''.join(s_word)
    length_sorted_word=len(sorted_word)
    dict_of_possible_words=get_words_dict(length_sorted_word, list_of_all_words)
    for k,v in dict_of_possible_words.iteritems():
        if k==sorted_word:
            list_of_possible_words= v
    if len(list_of_possible_words)==0:
        return ""
    else:
        return list_of_possible_words


def main():
    filepath="Data/dictionary.txt";
    print "Enter the word or type '*' to exit"
    word = raw_input("input: ")
    
    if word != ("*"):
        print "searching for words......................."
        list_of_words_from_text_file=get_list_of_words(filepath)
        list_of_possible_words=find_possible_words(word,list_of_words_from_text_file)
        if list_of_possible_words=='':
            print "Sorry no matching words found"
        else:
            print "--------matched words are-------------- "
            for value in list_of_possible_words:
                print "    ",value
            print "----------------------------------"
        main()
    else:
        print "Exit from application"
        sys.exit(0)
        
if __name__ == "__main__":
    main()