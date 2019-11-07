from flask import Flask, redirect, url_for, request , render_template
app = Flask(__name__)

users = {}
idcollect={}
buffer = {} 

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'GET':
        user = request.args.get('name')
        mima = request.args.get('password')
        bb = open('used.txt')
        for i in bb.readlines():
            x = i.split(':' , 1)
            k = x[0].strip()
            l = x[1].strip()
            buffer[k] = l
        t = buffer.__contains__(user)
        if t == False:
            return '您未注册，请先注册后使用'
        else:
            t = buffer[user]
            if t == mima:
                return '欢迎登陆'
            else:
                return '密码错误'

@app.route('/registration',methods = ['POST'])
def registration():
    newuser = request.form['newname']
    newmima = request.form['newpassword']
    again = request.form['againpassword']
    idnum = request.form['idnumber']
    if again == newmima:
        users[newuser] = newmima
        idcollect[newuser] = idnum
        out=open('usertext.txt','w')
        for key in users:
            out.write(key)
        out.write(':')
        o=' '
        for key2 in users[key]:
            o=o+key2
        out.write(o)
        out.write('\n')
        out.write('\n')
        out.close()
        out=open('userid.txt','w')
        for key in idcollect:
            out.write(key)
        out.write(':')
        o=' '
        for key2 in idcollect[key]:
            o=o+key2
        out.write(o)
        out.write('\n')
        out.write('\n')
        return '注册成功,欢迎你 %s' %newuser

    else:
        return '密码不一致'



if __name__ == '__main__':
   app.run(debug = True)