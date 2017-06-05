x=Mcqquestion.objects.filter(category='C',difficulty=2).values_list('question','option1','option2','option3','option4','answer')
i=1
f=open("new.txt","w")
for r in x:
	f.write("Q.%d %s \r\n" % (i,r[0]))
	f.write("a.)%s\r\n" % (r[1]))
	f.write("b.)%s\r\n" % (r[2]))
	f.write("c.)%s\r\n" % (r[3]))
	f.write("d.)%s\r\n\n" % (r[4]))
	i=i+1
f.close()



