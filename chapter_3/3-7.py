# coding: utf-8
invite=['saber', 'rin', 'auther']
invite.remove('auther')
invite.append('alexander')
invite.insert(0, 'zhangzhe')
invite.insert(2, 'renfei')
invite.append('xiao chao')
invite[2]='ren fei'
invite[0]='zhang zhe'
for invitee in invite:
    print (invitee.title() + ", I would like to invite you to dinner")
    
name=invite.pop()
print (name.title() + ", I'm regreted to tell you that dinner is cancelled.")
name=invite.pop()
print (name.title() + ", I'm regreted to tell you that dinner is cancelled.")
name=invite.pop()
print (name.title() + ", I'm regreted to tell you that dinner is cancelled.")
name=invite.pop()
print (name.title() + ", I'm regreted to tell you that dinner is cancelled.")
nname= invite.pop()
print (nname.title() + ", you're still invited. cheers.")
