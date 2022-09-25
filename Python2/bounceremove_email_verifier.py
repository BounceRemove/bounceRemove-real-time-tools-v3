import sys
import requests


# !!!PUT YOUR API KEY HERE!!!
api_key="YOUR_API_KEY"


if len(sys.argv) != 2:
    print ("usage: ", sys.argv[0], " <email>")
    sys.exit(1)

email = sys.argv[1]
try:
    j = requests.get("http://dev.bounceremove.com/validation/single?api_key="+api_key+"&"+"email="+email).json()
    c = j['status']
    b = j['diagnosis']
    f = j['is_free']
    t = j['credits']

    print(
    """
    ======= [validation report ] =======
    EMAIL : %s
    STATUS : %s
    DIAGNOSIS : %s
    IS THIS EMAIL FREE  : %s
    ------------------------------------
    You still have %d credits left !
    ====================================
    """%(email,c,b,f,t)
    )
except Exception as e:
    print("an error happened, please try again or contact the admin")
    print(j)

