from werkzeug.security import generate_password_hash
from models.users import   Users
from models import db
class AddAccounts:
    @staticmethod
    def encrypting_password(password):
        """
        Hashes the given password using PBKDF2 + SHA256.
        :param password: Plaintext password string
        :return: Hashed password string
        """
        return generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
    @staticmethod
    def add(email,firstname,lastname,username,password):
        print('created')
        new_password = AddAccounts.encrypting_password(password)
        user = Users(firstname=firstname,lastname=lastname,username=username,email=email,password=new_password,roleid=2)
        db.session.add(user)
        db.session.commit()
        print('done')