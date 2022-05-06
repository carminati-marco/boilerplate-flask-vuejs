import mongoengine as me
from bson.objectid import ObjectId


class ToldYou(me.Document):
    name = me.StringField()
    users = me.ListField(me.ReferenceField('User'))
    
class User(me.Document):
    name = me.StringField()