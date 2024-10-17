from flask import *
from database import *


admin=Blueprint("admin",__name__)

@admin.route("/adminhome")
def adminhome():
    return render_template("adminhome.html")

@admin.route("/verifyshop",methods=['get','post'])
def verifyshop():
    data={}
    qry="select * from shop"
    res=select(qry)
    data['view']=res

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None

    if action=='accept':
        qry1="update login set usertype='shop' where login_id='%s'"%(id)
        update(qry1) 
        return ("<script>alert('Accept successfull');window.location='/verifyshop'</script>")

    if action=='reject':
        qry2="delete from login where login_id='%s'"%(id)
        delete(qry2)
        qry3="delete from shop where login_id='%s'"%(id)
        delete(qry3)

        return ("<script>alert('Reject successfull');window.location='/verifyshop'</script>")

    return render_template("admin_verify_shop.html",data=data)


@admin.route("/viewcomplaint",methods=['get','post'])
def viewcomp():
    data={}
    qry="select * from complaint"
    res=select(qry)
    data['view']=res

    return render_template("admin_view_complaint.html",data=data)


@admin.route("/admin_send_reply",methods=['get','post'])
def sendreply():
    if 'id' in request.args:
        id=request.args['id']
        
    if 'sed' in request.form:
        reply=request.form['rep']
        
        qry="update complaint set reply='%s'where complaint_id='%s'"%(reply,id)
        update(qry)
        return ("<script>alert('Send successfull');window.location='/viewcomplaint'</script>")

    return render_template("admin_send_comp_reply.html")

@admin.route("/manageservice",methods=['get','post'])
def manageservice():
    data={}
    qry="select * from service_center"
    res=select(qry)
    data['view']=res

    if 'reg' in request.form:
        name=request.form['name']
        latt=request.form['latitude']
        long=request.form['longitude']
        phone=request.form['ph']
        email=request.form['mail']
       
        qry="insert into service_center values(null,'%s','%s','%s','%s','%s')"%(name,latt,long,phone,email)
        insert(qry)
        return ("<script>alert('Register successfull');window.location='/manageservice'</script>")

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        
    else:
        action=None

    if action=='update':
        qry1="select * from service_center where service_center_id='%s'"%(id)
        res=select(qry1)
        data['up']=res

    if 'up' in request.form:
        name=request.form['name']
        latt=request.form['latitude']
        long=request.form['longitude']
        phone=request.form['ph']
        email=request.form['mail']

        qry2="update service_center set name='%s',latitude='%s',longitude='%s',phone='%s',email='%s' where service_center_id='%s'"%(name,latt,long,phone,email,id)
        update(qry2)
        return ("<script>alert('Update successfull');window.location='/manageservice'</script>")

    if action=='delete':
        qry3="delete from service_center where service_center_id='%s'"%(id)
        delete(qry3)
        return ("<script>alert('Delete successfull');window.location='/manageservice'</script>")

    return render_template("admin_manage_service_center.html",data=data)
@admin.route("/managemechanic",methods=['get','post'])
def managemech():
    data={}
    qry="select * from mechanic"
    res=select(qry)
    data['view']=res

    if 'reg' in request.form:
        name=request.form['name']
        latt=request.form['latitude']
        long=request.form['longitude']
        phone=request.form['ph']
        email=request.form['mail']
       

        qry="insert into mechanic values(null,'%s','%s','%s','%s','%s')"%(name,latt,long,phone,email)
        insert(qry)
        return ("<script>alert('Register successfull');window.location='/managemechanic'</script>")
    
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None

    if action=='update':
        qry1="select * from mechanic where mechanic_id='%s'"%(id)
        res=select(qry1)
        data['up']=res
    if 'up' in request.form:
        name=request.form['name']
        latt=request.form['latitude']
        long=request.form['longitude']
        phone=request.form['ph']
        email=request.form['mail']

        qry2="update mechanic set name='%s',latitude='%s',longitude='%s',phone='%s',email='%s' where mechanic_id='%s'"%(name,latt,long,phone,email,id)
        update(qry2)
        return ("<script>alert('Update successfull');window.location='/managemechanic'</script>")

    if action=='delete':
        qry3="delete from mechanic where mechanic_id='%s'"%(id)
        delete(qry3)
        return ("<script>alert('Delete successfull');window.location='/managemechanic'</script>")

    return render_template("admin_manage_mechanic.html",data=data)


@admin.route("/managevechtype",methods=['get','post'])
def mangvechtype():
    data={}
    qry="select * from vehicle_type"
    res=select(qry)
    data['view']=res

    if 'add' in request.form:
        vechty=request.form['tyname']
        qry="insert into vehicle_type values(null,'%s')"%(vechty)
        insert(qry)
        return ("<script>alert('Add successfull');window.location='/managevechtype'</script>")

   
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None

    if action=='update':
        qry1="select * from vehicle_type where vehicle_type_id='%s'"%(id)
        res=select(qry1)
        data['up']=res
        

    if 'up' in request.form:
        vechty=request.form['tyname']
        qry2="update vehicle_type set type_name='%s' where vehicle_type_id='%s'"%(vechty,id)
        update(qry2)
        return ("<script>alert('Update successfull');window.location='/managevechtype'</script>")

    if action=='delete':
        qry3="delete from vehicle_type where vehicle_type_id='%s'"%(id)
        delete(qry3)
        return ("<script>alert('Delete successfull');window.location='/managevechtype'</script>")
    return render_template("admin_manage_vehicle_type.html",data=data)