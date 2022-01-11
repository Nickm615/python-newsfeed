from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt
# Generates salt to hash passwords against
salt = bcrypt.gensalt()

class User(Base):

  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)
  # We use the validates decorator to create a new 'validate email' method. This method checks that the entered value contains '@' and then returns the value of the email column. The validates decorator does the rest.
  @validates('email')
  def validate_email(self, key, email):
    assert '@' in email
    # The assert keyword throws an error if the given entry does not contain the given character.
    return email
  def verify_password(self, password):
    return bcrypt.checkpw(
      password.encode('utf-8'),
      self.password.encode('utf-8')
  )

  @validates('password')
  def validate_password(self, key, password):
    assert len(password) > 4

    return bcrypt.hashpw(password.encode('utf-8'), salt)

  