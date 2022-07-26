from flask import Flask,render_template, request,redirect,url_for,session,g
import mysql.connector
from mysql.connector import Error,connect
from datetime import timedelta
import os
import re
import random
import nltk
from gensim import corpora,models,similarities
import numpy as np
import gensim as gen
from urllib.request import urlopen
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity as sims
#import pandas as pd

app=Flask(__name__)
app.secret_key="vineeth"
app.permanent_session_lifetime = timedelta(minutes=10)

d={'k1':4323545,'k2':0}
#home space**********************************************************************************************************************************************************
@app.route('/home',methods=['GET','POST'])
def home():
	return render_template('home.html')

#admin space----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#****************************************************************************************************************************************************************************************
@app.route('/admin',methods=['GET','POST'])
def admin():
	if request.method == 'POST':
		us=request.form['name']
		ps=request.form['pass']
		session.permanent=True
		session["us"]=us
		p=conn_admin(us)
		if(ps==p):
			return render_template("adminnav.html")
		else:
			return render_template("admin.html",message="username and password doesnot match")
	else:
		if "us" in session:
			return render_template("adminnav.html")

	return render_template('admin.html')

def conn_admin(u):
	myresult1=[]
	try:
		connection = mysql.connector.connect(host='localhost',database='nlp',user='admin',password='admin123')
		cursor = connection.cursor()
		squery="SELECT password FROM admin where username= '%s' " %u
		cursor.execute(squery)
		myresult1= cursor.fetchall()
		cursor.close()
	except mysql.connector.Error as error:
			print("Failed to conn {}\n".format(error))
	finally:
		if (connection.is_connected()):
			connection.close()
			print("MySQL connection is closed\n")
	a=myresult1[0][0]
	return a

@app.route('/logut')
def logut():
	session.pop('us',None)
	return render_template('home.html')

@app.route('/adduser',methods=['GET','POST'])
def adduser():
	if "us" in session:
		if request.method == 'POST':
			us=request.form['nm']
			ps=request.form['pass']
			br=request.form['br']
			conn_adduser(us,ps,br)
			return render_template('adminnav.html')

		return render_template('adduser.html')
	else:
		return redirect(url_for('admin'))

def conn_adduser(us,ps,br):
	try:
		connection = mysql.connector.connect(host='localhost',database='nlp',user='admin',password='admin123')
		cursor = connection.cursor()
		query = "INSERT INTO staff_login (username,password,branch) VALUES ('%s','%s','%s')" % (us,ps,br)
		display(query)
		cursor.execute(query)
		connection.commit()
		display("successfully executed query")
		cursor.close()
	except mysql.connector.Error as error:
		print("Failed to insert record into  table {}\n".format(error))

	finally:
		if (connection.is_connected()):
			connection.close()
			display("MySQL connection is closed")

@app.route("/manage",methods=['GET','POST'])
def manage():
	if "us" in session:
		if request.method =='POST':
			rl=request.form['roll']
			res=conn_details(rl)
			print("this is picked database")
			display(res)
			return render_template("manage.html",name=res[0],email=res[3],branch=res[1],password=res[4])

		return render_template("manage.html")
	else:
		return redirect(url_for('admin'))


def conn_details(rl):
	result=[]
	try:
		connection = mysql.connector.connect(host='localhost',database='nlp',user='admin',password='admin123')
		cursor = connection.cursor(buffered=True)
		display("cursor created")
		query = "select * from student_register  where student_id ='%s'" % (rl)
		display(query)
		cursor.execute(query)
		result=cursor.fetchone()
		connection.commit()
		display("successfully executed query")
		cursor.close()
	except mysql.connector.Error as error:
		print("Failed search {}\n".format(error))

	finally:
		if (connection.is_connected()):
			connection.close()
			display("MySQL connection is closed")
	return result

@app.route("/remove",methods=['GET','POST'])
def remove():
	if "us" in session:
		if request.method =='POST':
			rl=request.form['roll']
			res=conn_remove(rl)
			return render_template("remove.html",message="removed successfully")
		return render_template("remove.html")
	else:
		return redirect(url_for('admin'))


def conn_remove(rl):
	try:
		connection = mysql.connector.connect(host='localhost',database='nlp',user='admin',password='admin123')
		cursor = connection.cursor(buffered=True)
		display("cursor created")
		query = "delete from student_register  where student_id ='%s'" % (rl)
		display(query)
		cursor.execute(query)
		connection.commit()
		display("successfully executed query")
		cursor.close()
	except mysql.connector.Error as error:
		print("Failed search {}\n".format(error))
	finally:
		if (connection.is_connected()):
			connection.close()
			display("MySQL connection is closed")

@app.route("/removestaff",methods=['GET','POST'])
def removestaff():
	if "us" in session:
		if request.method=='POST':
			us=request.form['usr']
			conn_removestaff(us)
			return render_template('removestaff.html',message='successfully removed')
		return render_template('removestaff.html')
	else:
		return redirect(url_for('admin'))

def conn_removestaff(us):
	try:
		connection = mysql.connector.connect(host='localhost',database='nlp',user='admin',password='admin123')
		cursor = connection.cursor(buffered=True)
		display("cursor created")
		query = "delete from staff_login  where username ='%s'" % (us)
		display(query)
		cursor.execute(query)
		connection.commit()
		display("successfully executed query")
		cursor.close()
	except mysql.connector.Error as error:
		print("Failed search {}\n".format(error))

	finally:
		if (connection.is_connected()):
			connection.close()
			display("MySQL connection is closed")


#**********************************************************************************************************************************************************************
#staff space-----------------------------------------------------------------------------------------------------------------------------------------------------------
#**********************************************************************************************************************************************************************
@app.route('/stafflgn',methods=['GET','POST'])
def stafflgn():
	if request.method == 'POST':
		us=request.form['name']
		ps=request.form['pass']

		p=conn_lgn(us)
		display(p)

		if (ps==p):
			return render_template('staffnav.html')
		else:
			return render_template('stafflgn.html',vindex="username and password doesnot matched")
	return render_template('stafflgn.html')

def conn_lgn(u):
	try:
		connection = mysql.connector.connect(host='localhost',database='nlp',user='admin',password='admin123')
		cursor = connection.cursor()
		squery="SELECT password FROM staff_login where username= '%s' " %u
		print("\n",squery)
		cursor.execute(squery)
		myresult1= cursor.fetchall()
		cursor.close()
	except mysql.connector.Error as error:
			print("Failed to conn {}\n".format(error))
	finally:
		if (connection.is_connected()):
			connection.close()
			print("MySQL connection is closed\n")
	a=myresult1[0][0]
	display(a)
	return a


@app.route('/fl',methods=['GET','POST'])
def fl():
	if request.method == 'POST':
		table=request.form["sub"]
		lv=request.form["lvl"]
		if lv=='NO':
			if request.files['qfl'] and request.files['afl']:
				print('file page found\n')
				qfile=request.files['qfl']
				qfile.save(os.path.join("uploaded_files", qfile.filename))
				qfl=open("uploaded_files/"+qfile.filename,'r')
				afile=request.files['afl']
				afile.save(os.path.join("uploaded_files", afile.filename))
				afl=open("uploaded_files/"+afile.filename,'r')
				qrd=qfl.read().splitlines()
				ard=afl.read().splitlines()
				if '' in qrd:
					qrd.remove('')
				if '' in ard:
					ard.remove('')
				if len(qrd) != len(ard):
					display(len(qrd),len(ard))
					print("questions")
					display(qrd)
					print('answers')
					display(ard)
					return render_template('file.html',message="In given files no of questions and answers does not match,upload again :)")
				else:
					display("successful")
					flag=0
					f=conn_qsn(table,qrd,ard,flag)

				if (f==0):
					return render_template('file.html',message="database conflict,may be table redundent")
				return render_template('file.html',message="questions uploaded successfully")
		if lv=='YES':
			qls=[]
			if request.files['qfl'] and request.files['afl']:
				print('file page found\n')
				qfile=request.files['qfl']
				qfile.save(os.path.join("uploaded_files", qfile.filename))
				qfl=open("uploaded_files/"+qfile.filename,'r')
				qrd=qfl.read().splitlines()
				afile=request.files['afl']
				afile.save(os.path.join("uploaded_files", afile.filename))
				afl=open("uploaded_files/"+afile.filename,'r')
				ard=afl.read().splitlines()
				if (len(qrd)-2)!= (len(ard)-1):
					print((len(qrd)-2),len(ard))
					print("questions")
					display(qrd)
					print('answers')
					display(ard)
					return render_template('file.html',message="In given files no of questions and answers does not match,upload again :)")
				else:
					flag=1
					f=conn_qsn(table,qrd,ard,flag)
				if (f==0):
					return render_template('file.html',message="database conflict,may be table redundent")
				return render_template('exam.html',message=lv)
	return render_template('file.html')

def conn_qsn(table,qls,als,flag):
	try:
		connection = mysql.connector.connect(host='localhost',database='questions',user='admin',password='admin123')
		cursor = connection.cursor()
		query = "create table %s (sino int(11),questions varchar(255),answers varchar(255),level int(11))" %(table)
		cursor.execute(query)
		display("TABLE CREATED SUCCESSFULLYY!!")
		if flag==0:
			level=0
			for x in range(len(qls)):
				query = "INSERT INTO %s (sino,questions,answers,level) VALUES ('%s','%s','%s','%s')" % (table,x,qls[x],als[x],level)
				print(query)
				cursor.execute(query)
				connection.commit()
			print(cursor.rowcount, "Record inserted successfully into student_register table\n")
		if flag==1:
			level=1
			sino=0
			for x in range(len(qls)):
				if qls[x] == 'level':
					level+=1
				else:
					sino=sino+1
					query = "INSERT INTO %s (sino,questions,answers,level) VALUES ('%s','%s','%s','%s')" % (table,sino,qls[x],"uploading..",level)
					print(query)
					cursor.execute(query)
					connection.commit()
			print(cursor.rowcount, "Record inserted successfully into student_register table\n")
			sino=0
			for x in range(len(als)):
				sino=sino+1
				query="update %s set answers='%s' where sino=%s" % (table,als[x],sino)
				print(query)
				cursor.execute(query)
				connection.commit()
				print(cursor.rowcount, "Record inserted successfully into student_register table\n")
		cursor.close()
		flag=1
	except mysql.connector.Error as error:
		print("Failed to insert record into  table {}\n".format(error))
		flag=0

	finally:
		if (connection.is_connected()):
			connection.close()
			print("MySQL connection is closed\n")
	return flag

@app.route('/showbase')
def showbase():
	ls=[]
	db=conn_base()
	for x in range(len(db)):
		ls.append(db[x][0])
	return render_template('showbase.html',message=ls)

def conn_base():
	try:
		connection = mysql.connector.connect(host='localhost',database='questions',user='admin',password='admin123')
		cursor = connection.cursor()
		squery="show tables"
		print("\n",squery)
		cursor.execute(squery)
		myresult1= cursor.fetchall()
		cursor.close()
	except mysql.connector.Error as error:
			print("Failed to conn {}\n".format(error))
	finally:
		if (connection.is_connected()):
			connection.close()
			print("MySQL connection is closed\n")
	return myresult1
#**********************************************************************************************************************************************************************
#student space
#**********************************************************************************************************************************************************************

@app.route('/send',methods=['GET','POST'])
def send():
	if request.method == 'POST':
		pass2=request.form['pass2']
		pass1 = request.form['pass1']
		pn=request.form['phone']
		email=request.form['email']
		name=request.form['nm']
		roll=request.form['rl']
		br=request.form['br']
		display(roll)

		if not re.match("^([a-zA-Z]+\s+[a-zA-Z]+(\s?)+([a-zA-Z]?)$)",name):
			return render_template("rgister.html",message='enter your name properly')
		if not re.match('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',email):
			return render_template("rgister.html",message='enter your email correctly')
		if not re.match('^[0-9]{10}$',pn):
			return render_template("rgister.html",message='enter your phone number correctly')
		if not re.match("[0-9]{12}$",roll):
			return render_template("rgister.html",message=' enter rollnumber in the format 245116xxxxx')
		if not re.match("^[a-z]{3,4}$",br):
			return render_template("rgister.html",message='enter only cse,ece,eee,mech,auto,cvl,mba')
		if(len(pass1) <= 6):
			return render_template("rgister.html",message='password should be above 6 chars')
		if(pass1 != pass2):
			render_template("rgister.html",message='passwords doesnot match')
		conn_rgstr(name,br,roll,email,pn,pass1)
		return render_template('index.html')
	return render_template('rgister.html')

def conn_rgstr(name,br,roll,email,pn,pas):
	try:
		connection = mysql.connector.connect(host='localhost',database='nlp',user='admin',password='admin123')
		cursor = connection.cursor()
		print('passing roll')
		display(roll)
		query = "insert into student_register (student_name,student_branch,student_id,student_email,student_password) values ('%s','%s','%s','%s','%s')" %(name,br,roll,email,pas)
		display(query)
		print(query)
		cursor.execute(query)
		connection.commit()
		print(cursor.rowcount, "Record inserted successfully into student_register table\n")
		cursor.close()
	except mysql.connector.Error as error:
		print("Failed to insert record into  table {}\n".format(error))

	finally:
		if (connection.is_connected()):
			connection.close()
			print("MySQL connection is closed\n")

@app.route('/log',methods=['GET','POST'])
def log():
	if request.method == 'POST':
		rl=request.form['roll']
		ps=request.form['pass']
		sub=request.form['sub']
		session.permanent=True
		session["rl"]=rl
		p=conn_slgn(rl)
		if(ps==p):
			return redirect(url_for('exam',roll=rl,sub=sub))
		else:
			return render_template("index.html",message="username and password doesnot match")
	else:
		if "rl" in session:
			return redirect(url_for('age'))

	return render_template('index.html')

def conn_slgn(rl):
	a=[]
	try:
		connection = mysql.connector.connect(host='localhost',database='nlp',user='admin',password='admin123')
		cursor = connection.cursor()
		squery="SELECT student_password FROM student_register where student_id= '%s' " %rl
		print("\n",squery)
		cursor.execute(squery)
		a=cursor.fetchone()
		display(a)
		cursor.close()
	except mysql.connector.Error as error:
			print("Failed to conn {}\n".format(error))
	finally:
		if (connection.is_connected()):
			connection.close()
			print("MySQL connection is closed\n")

	return a[0]

@app.route('/exam/<roll>/<sub>',methods=['GET','POST'])
def exam(roll,sub):
	alst=[]
	if 'rl' in session:
		if request.method=='POST':
			alst.append(request.form['q1'])
			alst.append(request.form['q2'])
			alst.append(request.form['q3'])
			alst.append(request.form['q4'])
			alst.append(request.form['q5'])
			alst.append(request.form['q6'])
			alst.append(request.form['q7'])
			flag=1
			conn_match(alst,alst,flag,d['k1'])
			return redirect(url_for('evaluate'))
		qlst,nlst,plst=conn_rtrv(sub)
		flag=0
		conn_match(qlst,plst,flag,roll)
		d['k1']=roll
		d['k2']=len(qlst)
		return render_template('exam.html',message=qlst)
	else:
		render_template("index.html")

def conn_match(qlst,lst,flag,roll):
	if flag==0:
		try:
			connection = mysql.connector.connect(host='localhost',database='temp',user='admin',password='admin123')
			cursor = connection.cursor()
			query = "create table %s (sino int,questions varchar(255),original_answers varchar(255),written_answers varchar(255))" % ('roll_'+roll)
			print("\n",query)
			cursor.execute(query)
			print("int's")
			display(roll)
			str(roll)
			print("string's")
			display(roll)
			for x in range(len(lst)):
				query = "INSERT INTO %s (sino,questions,original_answers,written_answers) VALUES ('%s','%s','%s','%s')" % ('roll_'+roll,x,qlst[x],lst[x],'after_exam')
				cursor.execute(query)
			connection.commit()
			cursor.close()

		except mysql.connector.Error as error:
			print("Failed to create  table because {}\n".format(error))
		finally:
			if (connection.is_connected()):
				connection.close()
				print("MySQL connection is closed\n")
	if flag==1:
		try:
			connection = mysql.connector.connect(host='localhost',database='temp',user='admin',password='admin123')
			cursor = connection.cursor()
			for x in range(len(lst)):
				query = "UPDATE  %s SET written_answers='%s' WHERE sino=%s " %('roll_'+roll,lst[x],x)
				print(query)
				cursor.execute(query)
			connection.commit()
			cursor.close()

		except mysql.connector.Error as error:
			print("Failed to create  table because {}\n".format(error))
		finally:
			if (connection.is_connected()):
				connection.close()
				print("MySQL connection is closed\n")



def conn_rtrv(table):
	try:
		connection = mysql.connector.connect(host='localhost',database='questions',user='admin',password='admin123')
		cursor = connection.cursor()
		lst= random.sample(range(0,10), 7)
		r=[]
		r1=[]
		for items in lst:
			squery="SELECT questions FROM %s where sino='%s' " %(table,items)
			print('\n',squery,'\n')
			cursor.execute(squery)
			temp=cursor.fetchone()
			display(temp)
			r.append(temp[0])
		for items in lst:
			squery="SELECT answers FROM %s where sino='%s' " %(table,items)
			print('\n',squery,'\n')
			cursor.execute(squery)
			temp=cursor.fetchone()
			display(temp)
			r1.append(temp[0])
		cursor.close()
	except mysql.connector.Error as error:
			print("Failed to conn {}\n".format(error))
	finally:
		if (connection.is_connected()):
			connection.close()
			print("MySQL connection is closed\n")
	return r,lst,r1

@app.route('/evaluate')
def evaluate():
	res=conn_pick()
	res=res * 100
	if res > 100:
		res = 100 * 0.7
	else:
		res=res * 0.7
	res = round(res,2)
	return render_template('age.html',message=res)

def conn_pick():
	try:
		connection = mysql.connector.connect(host='localhost',database='temp',user='admin',password='admin123')
		cursor = connection.cursor()
		n=d['k2']
		display(n)
		total=[]
		for x in range(0,n):
			query = "select original_answers,written_answers from %s where sino=%s" %('roll_'+d['k1'],x)
			display(query)
			cursor.execute(query)
			rs=cursor.fetchall()
			display(rs[0][0],rs[0][1])
			a=rs[0][0]
			b=rs[0][1]
			lf=score(a,b)
			print('it is lf')
			display(lf)
			total.append(lf)
			connection.commit()
		cursor.close()
		print('it is total')
		display(total)
		print("result is ")
		res = sum(total) / len(total)
		display(res)
	except mysql.connector.Error as error:
		print("Failed to create  table because {}\n".format(error))
	finally:
		if (connection.is_connected()):
			connection.close()
			print("MySQL connection is closed\n")
	return res

def score(original,written):
	ip = []
	ip.append(written)
	avg_sims=[]
	file_docs = []
	file_docs.append(original)
	checker=[]
	mx=[]
	tokens = sent_tokenize(file_docs[0])
	for line in tokens:
		checker.append(line)
	length_doc1 = len(checker)
	gen_docs = [[w.lower() for w in word_tokenize(text)]
				for text in checker]
	print(gen_docs)

	file2_docs=[]
	dictionary = gen.corpora.Dictionary(gen_docs)
	corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
	tf_idf = gen.models.TfidfModel(corpus)
	#find similarity module arguments, before there was a dirctory name
	sims = gen.similarities.Similarity(None,tf_idf[corpus],num_features=len(dictionary))
	tokens = sent_tokenize(ip[0])
	for line in tokens:
		file2_docs.append(line)
	for line in file2_docs:
		query_doc = [w.lower() for w in word_tokenize(line)]
		query_doc_bow = dictionary.doc2bow(query_doc)
		query_doc_tf_idf = tf_idf[query_doc_bow]
		m=max(sims[query_doc_tf_idf])
		mx.append(m)

#print('Comparing Result:\n', sims[query_doc_tf_idf])
		sum_of_sims =(np.sum(sims[query_doc_tf_idf], dtype=np.float32))
		avg = sum_of_sims / len(file_docs)
		#print(f'\n avg: {sum_of_sims / len(file_docs)}')
		avg_sims.append(avg)
	print(mx)
	ag=sum(mx)/len(mx)
	return avg

@app.route('/logout')
def logout():
	session.pop('rl',None)
	return redirect(url_for('log'))
#*********************************************************************************************************************************************************************************************************


def cr_db(db):
	try:
		connection = mysql.connector.connect(host='localhost',user='admin',password='admin123')
		cursor = connection.cursor()
		cr_db(table)
		query = "create database %S" %(db)
		print(query)
		cursor.execute(query)
		connection.commit()
		cursor.close()
	except mysql.connector.Error as error:
		print("Failed to insert record into  table {}\n".format(error))

	finally:
		if (connection.is_connected()):
			connection.close()
			print("MySQL connection is closed\n")

def cr_table(table):
	try:
		connection = mysql.connector.connect(host='localhost',database='questions',user='admin',password='admin123')
		cursor = connection.cursor()
		query = "create table %s (si.no int,question varchar(255),answers varchar(255))" %(table)
		print("\n",query)
		cursor.execute(query)
		connection.commit()
		print("\ntable created successful")
		cursor.close()
	except mysql.connector.Error as error:
		print("Failed to create  table because {}\n".format(error))

	finally:
		if (connection.is_connected()):
			connection.close()
			print("MySQL connection is closed\n")





def display(*args):
	print("\n-----------------------------------------------------------")
	print("\n",args)
	print("\n-----------------------------------------------------------")




if __name__=="__main__":
	
	app.run(port="8000",debug="true")
