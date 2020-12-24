punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            

def get_neg(str2):
    str2 = strip_punctuation(str2).split()
    
    sum = 0
    for i in str2:
        if i in negative_words:
            sum = sum + 1
    return sum

def get_pos(str1):
    str1 = strip_punctuation(str1).split()

    sum = 0
    for i in str1:
        if i in positive_words :
            sum = sum + 1        
    return sum



def strip_punctuation(str_1):
    for i in str_1:
        if i in punctuation_chars:
            str_1 = str_1.replace(i,"")
    return(str_1) 

   
def listtostring(s):
  str1 = ""

  for ele in s:
    str1 += ele
  return str1     

def writeInDataFile(File):
    file = open(File,"r") 
    lines = file.readlines()
    print(lines)
    
    wrd_lst = []
    for i in lines:
        i = i.strip()
        i = i.split(",")[0]
        wrd_lst.append(i)
        
        print(wrd_lst)
    
    pos_char = []
    neg_char = []
    
    for i_1 in wrd_lst:
        pos_char.append(get_pos(i_1))
        neg_char.append(get_neg(i_1))
        print(pos_char)
        print(neg_char)
        
    lst_char = ["Retweet_count,Replay_count,Pos_count,Neg_count,Net_score"]
    
    lst = []
    
    for i in lines:
        i = i.strip()
        i = i.split(",")[1:]
        lst_char.append(i)
        print(lst_char)
        
    lst_t = []
    for i in lst:
        i = list(map(int,i))
        lst_t.append(i)
    
    lst_char = lst_t
    
    for i in range(len(lst_char)):
        lst_char[i].append(pos_char[i])
        lst_char[i].append(neg_char[i])
        lst_char[i].append(pos_char[i] - neg_char[i])

    lst_ch0 = []

    for i in lst_char:
        lst_ch0.append(str(i_0) for i_0 in  i)
    lst_char = lst_ch0  


    lst_ch0.insert(0, "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    print(lst_char)

    lst_ch0 = '\n'.join(str(char) for char in lst_char)
  
    with open("resulting_data.csv", 'w') as cs_File:
        write = cs_File.write(lst_ch0)


if __name__ == '__main__':
    writeInDataFile('project_twitter_data.csv')   
        
    

