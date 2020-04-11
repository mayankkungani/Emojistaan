from django.shortcuts import render
import emojis

from django.utils.datastructures import MultiValueDictKeyError



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




# Create your views here.
def test(request):
    user=request.user
    #if request.method=='POST':
    print(request.method)
    #maintext=request.POST['text']
    text = 'text' in request.POST and request.POST['text']

    print(text)
    result=""
    if(text!=False):
    #text = request.GET['text']
    #initial = request.POST.get('text', False)
    
    #if (emojis.count(text)>=1):
        result=texttoemojitag(text)
    #else:
        #result=texttoemoji(text)

    

    #if request.method =='POST':
        #text=request.POST.get('msgbox','None')
        #print(text)

    return render(request,'index.html',{'name':result,'text':text,'user':user})


def tutorial(request):
    return render(request,'emoji_table.html')