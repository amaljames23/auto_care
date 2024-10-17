from flask import *
from database import *
import uuid

shop=Blueprint("shop",__name__)

@shop.route("/shophome")
def shopshomee():
    return render_template("shophome.html")

@shop.route("/sendcomplaint",methods=['get','post'])
def sendcompl():
    data={}
    qry="select * from complaint where sender_id='%s'"%(session['lid'])
    res=select(qry)
    data['view']=res

    if 'sed' in request.form:
        complaint=request.form['cmp']
        qry="insert into complaint values(null,'%s','%s','pending',curdate())"%(session['lid'],complaint)
        insert(qry)
        return ("<script>alert('Send successfull');window.location='/sendcomplaint'</script>")
    return render_template("shop_send_complaint.html",data=data)

@shop.route("/viewvehicletype",methods=['get','post'])
def viewvchtype():
    data={}
    qry="select * from vehicle_type"
    res=select(qry)
    data['view']=res

    return render_template("shop_view_vechicle_type.html",data=data)

@shop.route("/manage_spareparts",methods=['get','post'])
def managespareparts():
    data={}
    qry1="select * from spare_parts inner join vehicle_type using(vehicle_type_id) where shop_id='%s'"%(session['shpid'])
    res=select(qry1)
    data['view']=res

    if 'id' in request.args:
        id=request.args['id']

    if 'add' in request.form:
        spare=request.form['spare']
        quant=request.form['qua']
        price=request.form['price']
        des=request.form['des']
        image=request.files['images']

        path='static/'+str(uuid.uuid4())+image.filename
        image.save(path)

        qry="insert into spare_parts values(null,'%s','%s','%s','%s','%s','%s','%s')"%(session['shpid'],id,spare,quant,price,des,path)
        insert(qry)
        return ("<script>alert('Add successfull');window.location='/manage_spareparts'</script>")

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None

    if action=='delete':
        qry2="delete from spare_parts where spare_parts_id='%s'"%(id)
        delete(qry2)
        return ("<script>alert('Delete successfull');window.location='/manage_spareparts'</script>")
    
    if action=='update':
        qry3="select * from spare_parts where spare_parts_id='%s'"%(id)
        select(qry3)
        res=select(qry3)
        data['up']=res
                         
    if 'up' in request.form:
        spareparts=request.form['spare']
        quant=request.form['qua']
        price=request.form['price'] 
        des=request.form['des']
        image=request.files['images']

        path='static/'+str(uuid.uuid4())+image.filename
        image.save(path)

        qry4="update spare_parts set spare_part_name='%s',quan_tity='%s',price='%s',description='%s',image='%s' where spare_parts_id='%s'"%(spareparts,quant,price,des,path,id)
        update(qry4)
        return ("<script>alert('Update successfull');window.location='/manage_spareparts'</script>")

    return render_template("shop_manage_spare_parts.html",data=data)


@shop.route("/vieworders",methods=['get','post'])
def vieworder():
    data={}
    qry="select * from order_master inner join oreder_details using(order_master_id) where shop_id='%s'"%(session['shpid'])
    res=select(qry)
    data['view']=res
    
    return render_template("shop_view_orders.html",data=data)
@shop.route("/viewuserdetails",methods=['get','post'])
def viewuserdet():
    id=request.args['id']
    data={}
    qry="select * from user where user_id='%s'"%(id)
    res=select(qry)
    data['view']=res

    return render_template("shop_view_user_details.html",data=data)
@shop.route("/viewpayments",methods=['get','post'])
def viewpayment():
    id=request.args['id']
    data={}
    qry="select * from payments where order_master_id='%s'"%(id)
    res=select(qry)
    data['view']=res

    return render_template("shop_view_payments.html",data=data)
@shop.route("/updateprofile",methods=['get','post'])
def updateprofileshop():
    data={}
    qry="select * from shop where shop_id='%s'"%(session['shpid'])
    res=select(qry)
    data['view']=res
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None

    if action=='update':
        qry1="select * from shop where login_id='%s'"%(id)
        res=select(qry1)
        data['up']=res
    if 'up' in request.form:
        shopname=request.form['sname']
        latt=request.form['latitude']
        long=request.form['longitude']
        phone=request.form['ph']
        email=request.form['mail']

        qry2="update shop set shop_name='%s',latitude='%s',longitude='%s',phone='%s',email='%s' where login_id='%s'"%(shopname,latt,long,phone,email,id)
        update(qry2)
        return ("<script>alert('Update successfull');window.location='/updateprofile'</script>")

    return render_template("shop_update_profile.html",data=data)

@shop.route("/changepassword",methods=['get','post'])
def changepass():
    if 'up' in request.form:
        newpass=request.form['pwd']
        repass=request.form['pass']
        if newpass==repass:
            qry="update login set password='%s' where login_id='%s'"%(repass,session['lid'])
            update(qry)   
        else:
            return ("<script>alert('reenter password is not matching');window.location='/changepassword'</script>")

    return render_template("shop_change_password.html")