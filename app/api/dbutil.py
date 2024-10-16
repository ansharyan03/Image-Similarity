import sqlite3
from api.s3util import S3Uploader
from model.model import SimilarityModel
from io import BytesIO
from PIL import Image


user_query = "SELECT * FROM users WHERE username=?"

class UserImageDB:
    
    def __init__(self):
        self.db = sqlite3.connect('deez.sqlite', check_same_thread=False)
        self.s3 = S3Uploader()
        self.model = SimilarityModel()
        cur = self.db.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS users(username VARCHAR(32) UNIQUE, password VARCHAR(32), image VARCHAR(32))')
        
    def sign_up(self, user, password, image):
        # process image
        cur = self.db.cursor()
        cur.execute(user_query, (user,))
        registered = cur.fetchall()
        if len(registered) == 0:
            #put image to s3
            #put image url in database along with username
            self.s3.put_s3_image(image)
            cur.execute('INSERT INTO users VALUES (?, ?, ?)', (user, password, image.filename))
            self.db.commit()
            return True
        return False       
    
    def get_user(self, user):
        cur = self.db.cursor()
        cur.execute(user_query, (user,))
        print(user_query)
        user = cur.fetchone()
        cur.fetchall()
        return user
    
    def get_all_users(self):
        cur = self.db.cursor()
        cur.execute('SELECT * FROM users')
        users = cur.fetchall()
        return users

    def get_similarity(self, user1, user2):
        user1 = self.get_user(user1)
        user2 = self.get_user(user2)
        if user1 and user2:
            file1 = self.s3.get_s3_image(user1[2])['Body'].read()
            file2 = self.s3.get_s3_image(user2[2])['Body'].read()
            self.model.add_input_PIL(file1)
            self.model.add_input_PIL(file2)
            sim = self.model.get_similarity()
            self.model.inputs.clear()
            return sim
        else:
            print('error: no two users found with usernames %s, %s' % (user1, user2))
