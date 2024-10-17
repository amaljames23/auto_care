from flask import *

user=Blueprint("user",__name__)

@user.route("/userhome",methods=['get','post'])
def usershome():
    
    return render_template("userhome.html")
