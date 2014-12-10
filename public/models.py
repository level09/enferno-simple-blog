from extensions import db

class Post(db.Document):
    title = db.StringField()
    body = db.StringField()
    created_at = db.DateTimeField()

    def __unicode__(self):
        return '%s' % self.title


