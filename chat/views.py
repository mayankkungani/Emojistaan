from django.shortcuts import render
from django.contrib.auth.models import User
from accounts.models import UserProfiles
from .models import chatmsgs,chatemojiss
from functions import emojitotext,texttoemoji,texttoemojitag





#def getmsg()

#def getemojimsg():
#   emojmessg=chatemojiss.message











# Create your views here.
def chathome(request):
    #from django.contrib.auth import authenticate
    #user = authenticate(username='john', password='secret')
    user=request.user
    finallist=[]
    userlist=User.objects.values('username')
    
    print(userlist[0])
    chatmsg ='chat' in request.POST and request.POST['chat']
    print(chatmsg)
    if(chatmsg!=False):
        chatmg=emojitotext(chatmsg)
        c=chatmsgs(user=user,message=chatmg)
        #print(chatmsg)
        #if chatmsg !='':
        c.save()
            
        chatemoj=texttoemojitag(chatmsg)
        print(chatemoj)
        d=chatemojiss(user=user,message=chatemoj)
        #if chatemoj !='':
        d.save()
    #u = User.objects.get(special=True)
    main_id=user.id
    print(main_id)
    userpf=UserProfiles.objects.filter(user_id=main_id).values('deaf')
    result=userpf[0]['deaf']
    print("ans")
    print(result)
    if(result==True):
        emojimessg=chatemojiss.objects.values('message','user_id')
        print(emojimessg)
        try:
            i = 0
            while(emojimessg[i]['message'] != ""):
                msg=emojimessg[i]['message']
                user_id=emojimessg[i]['user_id']
                userobj=User.objects.filter(id=user_id).values('username')
                print(userobj)
                finallist.append([userobj[0]['username'],msg])
                i = i + 1
        except IndexError:
            pass    
    else:
        try:
            emojimessg=chatmsgs.objects.values('message','user_id')
            j = 0
            while(emojimessg[j]['message'] !=" "):
                msg=emojimessg[j]['message']
                user_id=emojimessg[j]['user_id']
                userobj=User.objects.filter(id=user_id).values('username')
                finallist.append([userobj[0]['username'],msg])
                j = j+1
            print(finallist)        
        except IndexError:
            pass


    #print(userpf.id)
    #if (user.special in User==False):
    #    print("kaam bhari bhari kaam")

    return render(request,"chat/chathome.html",{'user':user,'finallist':finallist,'userlist':userlist})