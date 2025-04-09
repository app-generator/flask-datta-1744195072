# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Ambiente(db.Model):

    __tablename__ = 'Ambiente'

    id = db.Column(db.Integer, primary_key=True)

    #__Ambiente_FIELDS__
    name = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)

    #__Ambiente_FIELDS__END

    def __init__(self, **kwargs):
        super(Ambiente, self).__init__(**kwargs)


class Projecto(db.Model):

    __tablename__ = 'Projecto'

    id = db.Column(db.Integer, primary_key=True)

    #__Projecto_FIELDS__
    name = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)

    #__Projecto_FIELDS__END

    def __init__(self, **kwargs):
        super(Projecto, self).__init__(**kwargs)


class Hosts(db.Model):

    __tablename__ = 'Hosts'

    id = db.Column(db.Integer, primary_key=True)

    #__Hosts_FIELDS__
    ip_address = db.Column(db.Text, nullable=True)
    last_seen = db.Column(db.DateTime, default=db.func.current_timestamp())
    cpu_usage = db.Column(db.Integer, nullable=True)
    memory_usage = db.Column(db.Integer, nullable=True)
    disk_usage = db.Column(db.Integer, nullable=True)

    #__Hosts_FIELDS__END

    def __init__(self, **kwargs):
        super(Hosts, self).__init__(**kwargs)


class Endpoint(db.Model):

    __tablename__ = 'Endpoint'

    id = db.Column(db.Integer, primary_key=True)

    #__Endpoint_FIELDS__
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.Text, nullable=True)
    last_checked = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Endpoint_FIELDS__END

    def __init__(self, **kwargs):
        super(Endpoint, self).__init__(**kwargs)


class Ansibleexecution(db.Model):

    __tablename__ = 'Ansibleexecution'

    id = db.Column(db.Integer, primary_key=True)

    #__Ansibleexecution_FIELDS__
    output = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Ansibleexecution_FIELDS__END

    def __init__(self, **kwargs):
        super(Ansibleexecution, self).__init__(**kwargs)



#__MODELS__END
