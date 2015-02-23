#!/usr/bin/env python
#-*- coding: utf-8 -*-

import hashlib, uuid
from random import choice
# import re
import time
import json
import tornado
import tornado.web
import httplib
import datetime
from email.mime.text import MIMEText
from model import *
from config import *
import traceback

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("name")

    def get_login_url(self):
        return "/login"

def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

def generate_password(passwd_length, passwd_seed):
    passwd = []
    while len(passwd) < passwd_length:
        passwd.append(choice(passwd_seed))
    return ''.join(passwd)

def get_json(domain, url):
    try:
        httpClient = httplib.HTTPConnection(domain, 8000, timeout=2000)
        httpClient.request('GET', url) 

        response = httpClient.getresponse()
        # print response.status
        response.reason
        return response.read()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
    #return raw_news

def get_latest_news_id():
    maxid = CalendarDatabase.query("""SELECT MAX(id) AS mid FROM newsTable""")
    if maxid[0]['mid']:
        maxid = int(maxid[0]['mid'])
    else:
        maxid = 0 
    return maxid       

def get_latest_news_nid():
    maxnid = CalendarDatabase.query("""SELECT MAX(nid) AS mnid FROM newsTable""")
    if maxnid[0]['mnid']:
        maxnid = int(maxnid[0]['mnid'])
    else:
        maxnid = 0
    return maxnid

def get_total_news_num():
    total = CalendarDatabase.query("""SELECT COUNT(id) AS total FROM newsTable""")
    total = int(total[0]['total'])
    return total

def get_oldest_news_id():
    minid = CalendarDatabase.query("""SELECT MIN(id) AS mid FROM newsTable""")
    if minid[0]['mid']:
        minid = int(minid[0]['mid'])
    else:
        minid = 0
    return minid

def get_a_news(nid):
    news = CalendarDatabase.query("""SELECT * FROM newsTable WHERE id=%s""",
            nid)
    if len(news):
        return news[0]
    else:
        return {} 


def get_news_list(min_id, max_id):
    newsList = CalendarDatabase.query("""SELECT * FROM newsTable WHERE id<=%s
            and id>=%s ORDER BY id DESC""", max_id, min_id)
    if len(newsList):
        return newsList
    else:
        return {}

def get_password_by_email(email):
    password = CalendarDatabase.query("""SELECT password FROM usersTable WHERE
        email=%s""", email)[0]['password']
    return password

def get_email_by_name(name):
    user_email = CalendarDatabase.query("""SELECT email FROM usersTable WHERE
            name=%s""", name) 
    if len(user_email):
        user_email = user_email[0]['email']
    else:
        user_email = ''
    return user_email

def get_id_by_name(name):
    user_id = CalendarDatabase.query("""SELECT id FROM usersTable WHERE
            name=%s""", name)
    if len(user_id):
        user_id = int(user_id[0]['id'])
    else:
        user_id = -1 
    return user_id

def get_name_by_email(email):
    name = CalendarDatabase.query("""SELECT name FROM usersTable WHERE
            email=%s""", email)
    if len(name):
        name = name[0]['name']
    else:
        name = ''
    return name

def get_name_by_id(user_id):
    name = CalendarDatabase.query("""SELECT name FROM usersTable WHERE
            id=%s""", user_id)
    if len(name):
        name = name[0]['name']
    else:
        name = ''
    return name

def get_user_by_id(user_id):
    user = CalendarDatabase.query("""SELECT id, name, email FROM usersTable
            WHERE id=%s""", user_id)
    if len(user):
        user = user[0]
    else:
        user = ''
    return user

def get_user_by_name(user_name):
    user = CalendarDatabase.query("""SELECT id, name, email FROM usersTable
            WHERE name=%s""", user_name)
    if len(user):
        user = user[0]
    else:
        user = ''
    return user

def get_salt_by_email(email):
    salt = CalendarDatabase.query("""SELECT salt FROM saltTable WHERE
        email=%s""", email)
    if len(salt):
        salt = salt[0]['salt']
    else:
        salt = ''
    return salt

def get_avatar_ext_by_email(email):
    ext = CalendarDatabase.query("""SELECT ext FROM usersTable WHERE
        email=%s""", email)
    if len(ext):
        ext = ext[0]['ext']
    else:
        ext = ''
    return ext 

def get_avatar_ext_by_id(id):
    ext = CalendarDatabase.query("""SELECT ext FROM usersTable WHERE
        id=%s""", id)
    if len(ext):
        ext = ext[0]['ext']
    else:
        ext = ''
    return ext 

def send_mail(to_email, sub, context):
    #if re.findall(re_email, to_email)[0][1] == 'qq':
    #    poster = 'qq'
    #else:
    #    poster = '163'
    poster = '163'

    me = mail_poster[poster]['user'] + "<" + mail_poster[poster]['user'] + "@" + mail_poster[poster]['postfix'] + ">"
    msg = MIMEText(context, 'html', 'utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = to_email[0]
    #print msg
    print mail_poster[poster]
    #try:
    send_smtp = smtplib.SMTP()
    send_smtp.connect(mail_poster[poster]['host'])
    send_smtp.login(mail_poster[poster]['user'], mail_poster[poster]['pass'])
    send_smtp.sendmail(me, to_email, msg.as_string())
    send_smtp.close()
    return True
    #except (Exception, e):
    #    print(str(e))
    #    return False

def update_check(email, code):
    record = CalendarDatabase.query("""SELECT * FROM checkTable WHERE
            email=%s""", email)
    if len(record):
        CalendarDatabase.execute("""UPDATE checkTable SET code=%s,
                check_time=%s, checked=%s WHERE email=%s""", code,
                now()[0], '0', email)
    else:
        CalendarDatabase.execute("""INSERT checkTable(email, code, checked) VALUES(%s,
                %s, %s)""", email, code, '0')

def send_check_email(email):
    passwd_seed = string.digits + string.ascii_letters + string.punctuation
    code = generate_password(30, passwd_seed)
    name = get_name_by_email(email)
    update_check(email, code)
    subject = '%s您好' % name
    
    code = tornado.escape.url_escape(code)
    context = 'http://www.pedestal.cn/api/check?email=%s&code=%s' % (email,
            code)
    print context

    name = get_name_by_email(email)
    if (True == send_mail(email, subject, context)):
        print 'success to ', name
        return True
    else:
        print 'fail to ', name
        return False

def check_email(email, code):
    ccode = CalendarDatabase.query("""SELECT code, checked FROM checkTable WHERE
        email=%s""", email)
    if len(ccode):
        checked = ccode[0]['checked']
        ccode = ccode[0]['code']
        print 'code: ', code
        print 'ccode: ', ccode
        if ccode == code and checked == 0: 
            CalendarDatabase.execute("""UPDATE usersTable SET checked=1 WHERE
                    email=%s""", email)
            CalendarDatabase.execute("""UPDATE checkTable SET checked=1 WHERE
                    email=%s""", email)
            return True
    return False

def add_news(id): 
    url = "/id/%s" % id
    raw_news = get_json(ali_page, url)

    if raw_news:
        json_dic = json.loads(raw_news)

        print now(), ':', id, 'insert'
        CalendarDatabase.execute("""INSERT newsTable
            (nid,publisher,sha1,date,title,source,
            link,source_link,clean_body,body)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" \
            ,json_dic['id'],\
             json_dic['publisher'],\
             json_dic['sha1'],\
             json_dic['date'],\
             json_dic['title'],\
             json_dic['source'],\
             json_dic['link'],\
             json_dic['source_link'],\
             json_dic['clean_body'],\
             json_dic['body'])
        return True
    else:
        print now(), ':', id, 'nothing'
        #NewsDatabase.execute("""INSERT newsTable(nid) VALUES(%s)""", 9999)
        return False


def request_info(httprequest):
    print "-----------------------------one request-----------------------------"
    print "method: %s" % httprequest.request.method
    print "uri: %s" % httprequest.request.uri
    print "remote_ip: %s" % httprequest.request.remote_ip
    print "body: %s" % httprequest.request.body
    print "time: %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print "-----------------------------one request-----------------------------"
    return False

def post_once(httprequest):
    ip = httprequest.request.remote_ip
    ENV_DICT['restrict'][ip][1] += 1
    ENV_DICT['restrict'][ip][0] = time.time()
    print ("Insert comm")
    print ENV_DICT['restrict'][ip][1]
   

def is_email_exist(email):
    re_email = r'^([[a-zA-Z0-9]+[_|\_|\.]?]*[a-zA-Z0-9]+)@([[a-zA-Z0-9]+[_|\_|\.]?]*[a-zA-Z0-9]+)\.[a-zA-Z]{2,4}$'
    isEmail = bool(re.match(re_email, email, re.VERBOSE))
    email_sql = CalendarDatabase.query("""SELECT email FROM usersTable WHERE
        email=%s""", email)
    if len(email_sql) or not isEmail:
        return False
    else:
        return True

def is_name_exist(name):
    name_sql = CalendarDatabase.query("""SELECT name FROM usersTable WHERE
        name=%s""", name)
    if len(name_sql):
        return True 
    else:
        return False 

def is_user_checked(email):
    checked = CalendarDatabase.query("""SELECT checked FROM usersTable WHERE
        email=%s""", email)
    if len(checked):
        return checked[0]['checked']
    else:
        return False 

def insert_a_user(user):
    '''
    user = {
        'email': 'xxx@xx.xx',
        'name': 'xxxx',
        'password': 'xxxx',
        }
    '''
    passwd = user['password']
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(passwd + salt).hexdigest()

    try:
        user['password'] = hashed_password
        UserCollection.insert(user)
        salt_dict = {}
        salt_dict['email'] = user['email']
        salt_dict['salt'] = salt
        SaltCollection.insert(salt_dict)
        return True
    except Exception, e:
        print traceback.print_exc()
        return False

def get_current_user(request):
    user = {}
    name = request.get_current_user()
    if name:
        user['vip'] = {}
        user['vip']['name'] = name
        user['vip']['id'] = get_id_by_name(name)
    name = request.get_secure_cookie('guest')
    if name:
        user['guest'] = {}
        user['guest']['name'] = name
        user['guest']['id']  = get_id_by_name(name)
    return user
    
def login(email, password):
    if not is_email_exist(email):
        check = get_password_by_email(email) 
        salt = get_salt_by_email(email)
        hashed_password = hashlib.sha512(password+salt).hexdigest()
        if hashed_password == check:
            CalendarDatabase.execute("""UPDATE usersTable SET last_login=%s
                    WHERE email=%s""",
                    now()[0],
                    email)
            name = get_name_by_email(email)
            print "email: ", email
            print "name", name
            print "password: ", password
            return True
    return False
    
def follow(pid, fname):
    fid = CalendarDatabase.query("""SELECT id FROM usersTable WHERE name=%s""",
            fname)
    pname = CalendarDatabase.query("""SELECT name FROM usersTable WHERE
            id=%s""", pid)
    if len(fid) and len(pname):
        fid = fid[0]['id']
        record = CalendarDatabase.query("""SELECT id FROM fllwTable WHERE pid=%s
            and fid=%s""", pid, fid)
        if not len(record): 
            CalendarDatabase.execute("""INSERT fllwTable(pid, fid) VALUES(%s, %s)""", pid, fid)
            return True
    return False

def subscribe(name, subscribed):
    user = CalendarDatabase.query("""SELECT id, subscribed FROM usersTale WHERE
        name=%s""", name)

    if len(user):
        user = user[0]
        if int(user['subscribed']) != subscribed:
            CalendarDatabase.execute("""UPDATE usersTable SET subscribed=%s
                    WHERE name=%s""", subscribed, name)
            return True
    return False

def change_passwd(email, passwd, new_passwd, re_new_passwd):
    if login(email, passwd) and new_passwd==re_new_passwd:
        name = get_name_by_email(email)
        passwd = new_passwd
        salt = uuid.uuid4().hex
        hashed_passwd = hashlib.sha512(passwd + salt).hexdigest()

        CalendarDatabase.execute("""UPDATE usersTable SET password=%s WHERE
                email=%s""", hashed_passwd, email)
        CalendarDatabase.execute("""UPDATE saltTable SET salt=%s WHERE
                email=%s""", salt, email)
        return True
    else:
        return False

def change_name(name, new_name):
    print 'name: ', name
    print 'new_name: ', new_name
    if new_name and not is_name_exist(new_name):
        print 'hehe'
        CalendarDatabase.execute("""UPDATE usersTable SET name=%s WHERE
            name=%s""", new_name, name)
        return True
    return False
        
