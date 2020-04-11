

def emojitotext(emoji):
    import emojis
    
    text=emojis.decode('{}'.format(emoji))
    text=text.replace(":"," ")
    return text


def texttoemoji(text):
    import emojis 
    texts=[]
    text=text.split()
    print(text)
    for i in text:
    	i=":{}:".format(i)
    	texts.append(i)
    	text=''.join(texts)
    	emoj=emojis.encode(text)
        
    return emoj



def texttoemojitag(text):
    import emojis
    #emoj=""
    if(text!=False): 
        finalemoj=""
        #text=text.split()
        #print(text)
        for i in text.split():
            try:
                emo=emojis.db.get_emojis_by_tag(i)
                emoj=emo[1]
                
            except StopIteration:
                emoj="null"
            if(emoj!="null"):
                finalemoj=finalemoj+emoj    
            
    return finalemoj
