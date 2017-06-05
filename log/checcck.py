from log.models import Subquestion,Mcqquestion

x=Subquestion.objects.filter(category='C',difficulty=2).values_list('question')
i=1
f=open("sub/new.txt","w")
for r in x:
	f.write("Q.%d %s \r\n" % (i,r[0]))
	i=i+1
f.close()
