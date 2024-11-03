import bcrypt

def verify_hash(plain_username, hashed_username):
    """Verifies a plain username against a hashed username."""
    return bcrypt.checkpw(plain_username.encode('utf-8'), hashed_username)


def hash_username(username):
    """Hashes a username using bcrypt."""
    return bcrypt.hashpw(username.encode('utf-8'), bcrypt.gensalt())
