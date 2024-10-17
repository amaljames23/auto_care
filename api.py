from flask import *
from database import *
import uuid

# from datetime import date
# from pytz import timezone
# from datetime import datetime


api=Blueprint("api",__name__)




@api.route("/login")
def login():
    data={}

    username=request.args['uname']
    pwd=request.args['pwd']
    print(username,pwd)

    qry="select * from login where username='%s' and password='%s'"%(username,pwd)
    res=select(qry)

    
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
 

    return str(data)


@api.route("/userreg")
def reg():
    data={}
    firstname=request.args['fname']
    lastname=request.args['lname']
    place=request.args['place']
    phone=request.args['phone']
    email=request.args['mail']
    username=request.args['uname']
    passw=request.args['pwd']

    qry="insert into login values(null,'%s','%s','user')"%(username,passw)
    id=insert(qry)
    print(id)

    qry1="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,firstname,lastname,place,phone,email)
    insert(qry1)

    data['status']='success'

    return str(data)



@api.route('/viewprofile')
def viewuserprofile():
    data={}
    
    logid = request.args['logid']

    qry="select * from user inner join login using(login_id) where login_id='%s'"%(logid)
    res=select(qry)
    print(res)

    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']='failed'
    data['method']="viewprofile"

    return str(data)

@api.route("/changepass")
def changepassw():
    data={}
    log_id = request.args['log_id']
    newpassw=request.args['newpass']
    
    qry="update login set password='%s' where login_id='%s'"%(newpassw,log_id)
    update(qry)
        
    data['status']='success'
    return str(data)

@api.route('/sendcomp')
def sendcomplaint():
    data={}
    lid=request.args['log_id']
    complaints=request.args['complaints']
    q="insert into complaint values(null,(select user_id from user where login_id='%s'),'%s','pending',curdate())"%(lid,complaints)
    print(q)
    res=insert(q)
    if res:
        data['status']='success'
    else:
        data['status']='failed'
    data['method']='User_Complaint'
        
    return str(data)
    
@api.route('/viewcomp')
def viewcompl():
    data={}
    lid=request.args['log_id']
    q="select * from complaint where sender_id=(select user_id from user where login_id='%s')"%(lid)
    print(q)
    res=select(q)
    data['status']='success'
    data['method']='User_feedbak'
    data['data']=res
    return str(data)

@api.route("/viewvechicletype")
def viewvechtype():
    data={}
    qry="SELECT * FROM vehicle_type "
    res=select(qry)
    if res:
        data['status']='success'
        data['data']=res
    return str(data)
@api.route("/viewmyvechicle")
def viewmyvechicle():
    data={}
    lid=request.args['log_id']
    qry="select * from  my_vehicle where user_id=(select user_id from user where login_id='%s')"%(lid)
    print(qry)
    res=select(qry)
    data['status']='success'
    data['method']='user_vehicle'
    data['data']=res
    return str(data)
@api.route('/addvechicle')
def addvech():
    data={}
    lid=request.args['login_id']
    vechicle_type_id=request.args['vid']
    vechiclename=request.args['addve']
    
    q="insert into my_vehicle values(null,(select user_id from user where login_id='%s'),'%s','%s')"%(lid,vechicle_type_id,vechiclename)
    res=insert(q)
    print(q)
    if res:
        data['status']='success'
    else:
        data['status']='failed'
    data['method']='add_vehicle'

    return  str(data)
@api.route("/viewservicecenter")
def viewservice():
    data={}
    qry="select * from service_center"
    res=select(qry)
    if res:
        data['status']='success'
        data['data']=res
        
    return str(data)
@api.route('/addreview')
def addreviews():
    data={}
    lid=request.args['login_id']
    servicenterid=request.args['sercenid']
    addreview=request.args['addriew']

    qry="insert into reviews values(null,(select user_id from user where login_id='%s'),'%s','service_center','%s',curdate())"%(lid,servicenterid,addreview)
    res=insert(qry)
    print(qry)
    if res:
        data['status']='success'
    else:
        data['status']='failed'
    data['method']='add_review'

    return str(data)
@api.route("/viewmechanic")
def viewmech():
    data={}
    qry="select * from  mechanic"
    res=select(qry)
    if res:
        data['status']='success'
        data['data']=res
        
    return str(data)

@api.route('/addreviewmech')
def addreviewsmech():
    data={}
    lid=request.args['login_id']
    mechanicid=request.args['mechid']
    addreview=request.args['addriew']

    qry="insert into reviews values(null,(select user_id from user where login_id='%s'),'%s','mechanic','%s',curdate())"%(lid,mechanicid,addreview)
    res=insert(qry)
    print(qry)
    if res:
        data['status']='success'
    else:
        data['status']='failed'
    data['method']='add_review'

    return str(data)
@api.route('/adddetails')
def adddetail():
    data={}
    my_vehicle_id=request.args['myvehid']
    addservicedetails=request.args['servdet']

    qry="insert into service_details values(null,'%s','%s',curdate())"%(my_vehicle_id,addservicedetails)
    insert(qry)
    print(qry)

    data['status']='success'
    
    return str(data)
@api.route('/viewreview')
def viewreviews():
    data={}
    sercenid=request.args['sercenid']
    qry="select * from reviews r inner join service_center m on r.review_for_id=m.service_center_id  where review_for_id='%s' and  review_for_type='service_center'"%(sercenid)
    res=select(qry)
    data['status']='success'
    data['method']='view_review'
    data['data']=res
    return str(data)


@api.route('/viewreviewmech')
def viewreviewsmechanic():
    data={}
    mechid=request.args['mechid']
    qry="select * from reviews r inner join mechanic m on r.review_for_id=m.mechanic_id where review_for_id='%s' and  review_for_type='mechanic' "%(mechid)
    res=select(qry)
    data['status']='success'
    data['method']='view_review'
    data['data']=res

    return str(data)


@api.route('/view_shops')
def viewshops():
    data={}
    lati=request.args['lati']
    logi=request.args['logi']
    qry="SELECT *, (3959 * ACOS(COS(RADIANS(%s)) * COS(RADIANS(latitude)) * COS(RADIANS(longitude) - RADIANS(%s)) + SIN(RADIANS(%s)) * SIN(RADIANS(latitude)))) AS user_distance FROM shop HAVING user_distance < 11.068 ORDER BY user_distance" % (lati,logi,lati)

    res=select(qry)
    if res:
        data['status']='success'
        data['data']=res
    return str(data)


@api.route('/searchspareparts')
def searchsparepart():
    data={}
    shop_id=request.args['shopid']
    qry="select * from spare_parts where shop_id='%s'"%(shop_id)
    res=select(qry)
    print(res)
    if res:
        data['status']='success'
        data['data']=res
    return str(data)


@api.route('/spareviewsearch')
def spareviewsearchs():
    data={}
    shop_id=request.args['shopid']
    search=request.args['search']+'%'
    q="select * from spare_parts inner join vehicle_type using (vehicle_type_id) where shop_id='%s' and spare_part_name like '%s'"%(shop_id,search)
    res=select(q)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    return str(data)

@api.route('/viewbookedspare')
def viewbookedspareparts():
    data={}
    log_id=request.args['log_id']
    quantity=request.args['booking']
    sparepartsid=request.args['spareid']
    shopid=request.args['shop_id']
    qry="select * from spare_parts where spare_parts_id='%s'"%(sparepartsid)
    res=select(qry)
    print(res)
    

    total=int(res[0]['price'])*int(quantity)
    
    q="update spare_parts set quan_tity=quan_tity-'%s' where spare_parts_id='%s'"%(quantity,sparepartsid)
    update(q)

    qry1="select * from order_master where status='pending' and user_id=(select user_id from user where login_id='%s')"%(log_id)
    val=select(qry1) 
    if val:
        oid=val[0]['order_master_id']
    else:
        qry2="insert into order_master values(null,(select user_id from user where login_id='%s'),'%s','0',curdate(),'pending')"%(log_id,shopid)
        oid=insert(qry2)
    qry3="select * from oreder_details where spare_parts_id='%s' and order_master_id='%s'"%(sparepartsid,oid)
    v=select(qry3)
    if v:
        qry4="update oreder_details set quantity=quantity+'%s',amount=amount+'%s' where order_master_id='%s'"%(quantity,total,v[0]['order_master_id'])
        update(qry4)
    else:
        qry5="insert into oreder_details values(null,'%s','%s','%s','%s')"%(oid,sparepartsid,quantity,total)
        insert(qry5)
    qry6="update order_master set total_amount=total_amount+'%s' where order_master_id='%s'"%(total,oid)
    m=update(qry6)

    if m:
        data['status']='success'
    else:
        data['data']=res
        
    return str(data)
    

@api.route('/myorders')
def myorders():
    data={}
    log_id=request.args['log_id']
    q="select * from order_master inner join oreder_details using(order_master_id) inner join spare_parts using(spare_parts_id) where user_id=(select user_id from user where login_id='%s') and order_master.status='pending'"%(log_id)
    res=select(q)
    if res:
        data['data']=res
        data['status']='success'
    else:
        data['status']='failed'
    return str(data)


@api.route('/makepayment')
def makepayment():
    data={}
    oid=request.args['omid']
    amount=request.args['amount']
    q="update order_master set status='Payment completed' where order_master_id='%s'"%(oid)
    print(q)
    update(q)
    qry="insert into payments values(null,'%s','%s',curdate(),'payment finshed')"%(oid,amount)
    insert(qry)
    data['status']='success'
    return str(data)


@api.route("/viewmy_vechicle")
def viewmyvechicles():
    data={}
    lid=request.args['log_id']
    qry="SELECT * FROM  my_vehicle INNER JOIN vehicle_type USING(vehicle_type_id) WHERE user_id=(SELECT user_id FROM USER WHERE login_id='%s')"%(lid)
    print(qry)
    res=select(qry)
    data['status']='success'
    data['method']='user_vehicle'
    data['data']=res
    return str(data)


@api.route("/addreminder")
def addreminders():
    data={}
    myvehicleid=request.args['myvehicle_id']
    title=request.args['title']
    des=request.args['desc']
    expriydat=request.args['expda']
    qry="insert into reminder values(null,'%s','%s','%s','%s',curdate(),'pending')"%(myvehicleid,title,des,expriydat)
    res=insert(qry)
    if res:
        data['status']='success'
    else:
        data['status']='failed'
    data['method']='add_reminder'
    return str(data)

@api.route('/viewreminder')
def viewreminders():
    data={}
    lid=request.args['log_id']
    qry="SELECT * FROM `reminder` INNER JOIN my_vehicle USING(my_vehicle_id) WHERE user_id=(select user_id from user where login_id='%s')"%(lid)
    res=select(qry)
    print(res)
    data['status']='success'
    data['method']='viewreminder'
    data['data']=res
    return str(data)



@api.route('/notification')
def notificationalert():
    data={}
    lid=request.args['log_id']
    qry="SELECT * FROM `reminder` INNER JOIN my_vehicle USING(my_vehicle_id) WHERE user_id=(select user_id from user where login_id='%s')"%(lid)
    res=select(qry)
    print(res)
    if res:
        data['status']='success'
        data['data']=res
    return str(data)



@api.route("/upreminder")
def updatereminders():
    data={}
    reminderid=request.args['reminderid']
    title=request.args['title']
    des=request.args['desc']
    expriydat=request.args['expda']
    qry="update reminder set title='%s',description='%s',exp_date='%s',date=curdate(),status='updated' where reminder_id='%s' "%(title,des,expriydat,reminderid)
    res=update(qry)
    if res:
        data['status']='success'
    else:
        data['status']='failed'
    data['method']='add_reminder'
    return str(data)

