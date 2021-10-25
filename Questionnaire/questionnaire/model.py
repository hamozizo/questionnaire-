from datetime import datetime
from flask_login import UserMixin
import jwt 
from questionnaire import db, app
from sqlalchemy.inspection import inspect

import datetime

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    def serialize_list(l):
        return [m.serialize() for m in l]

#creating class for db table
class questionnaire(db.Model,UserMixin):

    ques_id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    ques_title =  db.Column(db.String(300) , nullable=False)
    ques_type = db.Column(db.String(50), nullable=False)
    ques_sort_order =  db.Column(db.Integer,nullable=False)
    ques_updated_at = db.Column(db.DateTime, nullable=False)
    ques_created_at =  db.Column(db.DateTime, nullable=False)
    org_id = db.Column(db.Integer, db.ForeignKey('players.ply_id'),nullable=True)
    
    ply_questionnaire = db.relationship('ply_questionnaire',backref='questionnaire',lazy=True, uselist=False)

    def __getitem__(self):
        return self

    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
    def serialize_list(self):
        d = Serializer.serialize_list(self)
        return d

class players (db.Model,UserMixin):
  ply_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  ply_fname = db.Column(db.String(250),nullable=True) 
  ply_lname = db.Column(db.String(250),nullable=True)
  ply_email =  db.Column(db.String(100) ,nullable=True)
  ply_email_alternative = db.Column(db.String(100) ,nullable=True)
  ply_email_sett = db.Column(db.String(1) , default = 'y')
  ply_password = db.Column(db.String(100) ,nullable=True)
  ply_brithdate = db.Column(db.String(10) ,nullable=True)
  ply_brithdate_sett = db.Column(db.String(1) , default = 'y')
  ply_gender = db.Column(db.String(1) ,nullable=True)
  # ply_gende_sett = db.Column(db.String(1) , default = 'y')
  ply_height =  db.Column(db.Integer,  nullable=True)
  ply_height_sett = db.Column(db.String(1) ,nullable=True)
  ply_h_unit = db.Column(db.String(2) ,nullable=True)
  ply_weight =  db.Column(db.Integer, nullable=True)
  ply_weight_sett= db.Column(db.String(1) ,nullable=True)
  ply_w_unit = db.Column(db.String(2) ,nullable=True)
  ply_country_id = db.Column(db.Integer, nullable=True)
  ply_city_id = db.Column(db.Integer,nullable=True)
  ply_city_sett = db.Column(db.String(1) , default = 'y')
  ply_address = db.Column(db.String(34) ,nullable=True)
  ply_bio = db.Column(db.Text)
  ply_business = db.Column(db.String(100) ,nullable=True)
  ply_website = db.Column(db.String(200) ,nullable=True)
  ply_img = db.Column(db.String(150) ,nullable=True)
  ply_header_img = db.Column(db.String(150) ,nullable=True)
  s3_cover = db.Column(db.Integer, nullable=False , default = '0')
  s3_profile = db.Column(db.Integer, nullable=False , default = '0')
  ply_qcode = db.Column(db.String(59) ,nullable=True)
  ply_status = db.Column(db.String(10) ,nullable=True)
  ply_gc_token = db.Column(db.String(48) ,nullable=True)
  ply_gc_oid = db.Column(db.String(14) ,nullable=True)
  ply_paypal_email = db.Column(db.String(34) ,nullable=True)
  ply_setting = db.Column(db.String(1) , default = 'y')
  ply_state = db.Column(db.Integer, nullable=False , default = '0')
  ply_view_as = db.Column(db.String(10) ,nullable=True)
  ply_mobile_phone = db.Column(db.String(30) ,nullable=True)
  ply_pid = db.Column(db.Integer, nullable=False , default = '1')
  ply_created = db.Column(db.DateTime, nullable=True , default=datetime.datetime.utcnow)
  s3_status = db.Column(db.Integer,nullable=True)

  questionnaire = db.relationship('questionnaire',backref='players',lazy=True, uselist=False)
  ply_questionnaire = db.relationship('ply_questionnaire',backref='players',lazy=True, uselist=False)


  def __getitem__(self, players):
        return self

  def serialize(self):
        d = Serializer.serialize(self)
        return d


class gm_questionnaire (db.Model,UserMixin):
  gm_ques_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  gm_ques_stype_id =  db.Column(db.Integer, nullable=False)
  gm_ques_gm_id =  db.Column(db.Integer, nullable=False)
  gm_ques_ques_id =  db.Column(db.Integer, nullable=False)
  gm_ques_updated_at =  db.Column(db.DateTime, nullable=True )
  gm_ques_created_at =  db.Column(db.DateTime, nullable=True , default=datetime.datetime.utcnow)

  def __getitem__(self):
        return self

  def serialize(self):
        d = Serializer.serialize(self)
        return d

class ply_questionnaire (db.Model,UserMixin):
  ply_ques_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  ply_ques_ply_id =  db.Column(db.Integer, db.ForeignKey('players.ply_id'),nullable=True)
  ply_ques_ques_id = db.Column(db.Integer, db.ForeignKey('questionnaire.ques_id'),nullable=True)
  ply_ques_ques_answer = db.Column(db.String(150) ,nullable=False, default = '1')
  ply_ques_updated_at =  db.Column(db.DateTime, nullable=True )
  ply_ques_created_at = db.Column(db.DateTime, nullable=True , default=datetime.datetime.utcnow)

  def __getitem__(self):
        return self

  def serialize(self):
        d = Serializer.serialize(self)
        return d



