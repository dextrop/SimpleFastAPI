import hashlib
import os
def password_hashing(password, salt=None):
    """
    Password hashing method, Return hash_password and salt
    :param password: password to be hashed,
    :param salt: Default is none, If salt is not passed new salt will be generated
    :return: password_hash, salt
    """
    if not salt:
        # create salt based on urandom
        salt = os.urandom(8).hex()
    hash = hashlib.sha512()
    # TODO: shouldn't this update function use password, salt??
    hash.update(('%s%s' % (password, salt)).encode('utf-8'))
    password_hash = hash.hexdigest()
    return (password_hash, salt)
