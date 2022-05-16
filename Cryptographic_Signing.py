from django.core.management.utils import get_random_secret_key
from django.core.signing import Signer, TimestampSigner
'need to get this secret key from our django projec settings.py secret key'
SECRET_KEY = get_random_secret_key()
signer = Signer()
timestampsigner = TimestampSigner()
x=signer.sign("HelloWorld")
print(x)
y=signer.unsign(x)
print(y)
x=signer.sign_object({'user_id':'1'})
print(x)
y=signer.unsign_object(x)
print(y)

x=timestampsigner.sign_object({'name':'hemangi'})
print(x)
y=timestampsigner.unsign_object(x, max_age=5)
print(y)