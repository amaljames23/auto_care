from flask import *
from database import *

public=Blueprint("public",__name__)

@public.route("/")
def publichome():
    return render_template("publichome.html")

@public.route("/log",methods=['get','post'])
def login():
    if 'log' in request.form:
        username=request.form['uname']
        passw=request.form['pwd']

        qry="select * from login where username='%s'and password='%s'"%(username,passw)
        res=select(qry)

        if res:
            session['lid']=res[0]['login_id']

            if res[0]['usertype']=='admin':
                flash("login successfull")

                return redirect(url_for("admin.adminhome"))

                # return ("<script>alert('login successfull');window.location='/adminhome'</script>")

            elif res[0]['usertype']=='shop':
                qry1="select * from shop where login_id='%s'"%(session['lid'])
                res2=select(qry1)
                session['shpid']=res2[0]['shop_id']

                return ("<script>alert('login successfull');window.location='/shophome'</script>")
            

            elif res[0]['usertype']=='user':

                return ("<script>alert('login successfull');window.location='/userhome'</script>")
            
        else:
            return ("<script>alert('invalid password or user name');window.location='/log'</script>")
        
    return render_template("login.html")



@public.route("/reg",methods=['get','post'])
def registration():
    if 'reg' in request.form:
        shopname=request.form['sname']
        latt=request.form['latitude']
        long=request.form['longitude']
        phone=request.form['ph']
        email=request.form['mail']
        username=request.form['uname']
        passw=request.form['pwd']

        qry="insert into login values(null,'%s','%s','pending')"%(username,passw)
        loginid=insert(qry)

        qry1="insert into shop values(null,'%s','%s','%s','%s','%s','%s')"%(loginid,shopname,latt,long,phone,email)
        insert(qry1)

    return render_template("registration_shop.html")