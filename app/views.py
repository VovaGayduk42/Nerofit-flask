from flask import session, render_template, request, flash
from Other.sqlAlchemy_insert import user_add
from app import app, db
from app.models import User, user_info, Training
from tables import Results
from datetime import datetime, timedelta

poll_data = {
    'question': 'Ваш пол?',
    'fields': ['Мужчина', 'Женщина']
}


exp_var_data = {
    'question': 'Был ли опыт похудения?',
    'fields': ['Да, не удачный. Вес вернулся \n', 'Да, удачный. Удалось сохранить достигнутый вес \n','Нет, люблю жирок']
}

eating_var_data = {
    'question': 'Как вы питаетесь?',
    'fields': ['Ем что хочу. Не ограничиваю себя', 'Стараюсь исключать вредные продукты, а в остальном не сильно слежу','Стараюсь придерживаться правильного питания, но получается с переменным успехом','Постоянно пробую новые диеты', 'Веду дневник питания и считаю всё съеденное']
}


training_var_data = {
    'question': 'А как дела с тренировками?',
    'fields': ['Нет опыта тренировок', 'Был опыт, но давно. Более года не тренируюсь','Перодически начинаю тренироваться','Регулярно тренируюсь дома', 'Регулярно тренируюсь в зале']
}


activity_data = {
    'question_activity': 'Ваша активность?',
    'fields_activity': ['Низкая', 'Средняя', 'Высокая']
}




@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        global USER_ID
        print("identif" + str(db.session.query(User.id).first()))
        user = User.query.get(USER_ID)
        auth = user.auth
        print('Authentification=', auth)
        if auth:
            print('if auth CONTROL')
            return home_render()
        else:
            return welcome()
@app.route('/testpage')
def test_page_render():
    return render_template('voronka/walletone.html')



@app.route('/reg', methods=['POST'])
def do_register():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    user_add(POST_USERNAME, POST_PASSWORD)
    return "<h1>Register successful! <a href='/logout'>Logout</a><h1>"


@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    query = db.session.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:
        global USER_ID
        USER_ID = result.id
        session ['logged_in'] = True
    else:
         flash('wrong password!')
    return home()

@app.route('/login', methods=['POST'])
def login_page():
    return home()

@app.route('/welcome')
def welcome():
    return render_template('pages/start/welcome.html')



@app.route('/test/1', methods=['POST'])
def root():
    return render_template('pages/start/gender.html', data=poll_data)


@app.route('/poll')
def poll():
    global USER_ID
    vote = request.args.get('gender')
    if (vote == "Мужчина"):
        value = 1
    elif (vote == "Женщина"):
        value = 2
    else:
        value = 3
    user = User.query.get(USER_ID)
    user.gender = value
    db.session.commit()
    return data_render()

@app.route('/activity', methods=['POST'])
def activity_root():
    return render_template('pages/start/activity.html', data=activity_data)

@app.route('/activity')
def activity_poll():
    global USER_ID
    res = request.args.get('activity')
    if(res == "Низкая"):
        act = 1
    elif(res =="Средняя"):
        act = 2
    else:
        act = 3
    user = User.query.get(USER_ID)
    user.activity = act
    db.session.commit()
    return userinfo_render()


@app.route('/datainfo')
def data_render():
    return render_template('pages/start/data.html')


@app.route('/datainfo', methods=['POST'])
def date():
    text = request.form['date']
    global USER_ID
    user = User.query.get(USER_ID)
    user.data = text
    db.session.commit()
    return height_render()


@app.route('/heightinfo')
def height_render():
    return render_template('pages/start/height.html')


@app.route('/heightinfo', methods=['POST'])
def height():
    global USER_ID
    height = request.form['height']
    user = User.query.get(USER_ID)
    user.height = height
    db.session.commit()
    return activity_root()


@app.route('/userinfo')
def userinfo_render():
    return render_template('pages/start/user_info.html')


@app.route('/userinfo', methods=['POST'])
def userinfo():
    global USER_ID
    mass = request.form['mass']
    chest = request.form['chest']
    left_hand = request.form['left_hand']
    left_bedro = request.form['left_bedro']
    left_golen = request.form['left_golen']
    waist = request.form['waist']
    buttock = request.form['buttock']
    right_hand = request.form['right_hand']
    right_bedro = request.form['right_bedro']
    right_golen = request.form['right_golen']

    # print('parametrs:', mass,chest,left_hand,left_golen,left_bedro)
    # print('userinfo INFO=', mass)
    user = User.query.get(USER_ID)
    user.massuser = mass
    user.user_info = [
        user_info(mass=mass,
                  chest=chest,
                  left_hand=left_hand,
                  left_bedro=left_bedro,
                  left_golen=left_golen,
                  waist=waist,
                  buttock=buttock,
                  right_hand=right_hand,
                  right_bedro=right_bedro,
                  right_golen=right_golen,
                  user_id_helper=USER_ID)
    ]
    user.auth = True
    db.session.commit()
    return instruction_render()


@app.route('/useraddinfo')
def userinfo_add_render():
    return render_template('pages/start/user_add_info.html')


@app.route('/useradding', methods=['POST'])
def user_add_info():
    global USER_ID
    mass = request.form['mass']
    chest = request.form['chest']
    left_hand = request.form['left_hand']
    left_bedro = request.form['left_bedro']
    left_golen = request.form['left_golen']
    waist = request.form['waist']
    buttock = request.form['buttock']
    right_hand = request.form['right_hand']
    right_bedro = request.form['right_bedro']
    right_golen = request.form['right_golen']

    # print('parametrs:', mass,chest,left_hand,left_golen,left_bedro)
    # print('userinfo INFO=', mass)
    user = User.query.get(USER_ID)
    user.massuser = mass
    user.user_info = [
        user_info(mass=mass,
                  chest=chest,
                  left_hand=left_hand,
                  left_bedro=left_bedro,
                  left_golen=left_golen,
                  waist=waist,
                  buttock=buttock,
                  right_hand=right_hand,
                  right_bedro=right_bedro,
                  right_golen=right_golen,
                  user_id_helper=USER_ID)
    ]
    db.session.commit()
    return progress_render()


@app.route('/instruction')
def instruction_render():
    return render_template('pages/start/instruction.html')


@app.route('/home')
def home_render():
    user = User.query.get(USER_ID)
    username = user.username
    print(username)
    return render_template('pages/lk/home.html', username=username)


@app.route('/eat')
def eat_render():
    user = User.query.get(USER_ID)
    if user.massuser is None:
        return render_template('pages/start/gender.html', data=poll_data)
    else:
        kkal_norma = int(calculator())
        belki = int(belki_calc())
        giry = int(giry_calc())
        ugl = int(ugl_cal())

        return render_template('pages/lk/eat.html',
                               kkal_norma=kkal_norma,
                               belki=belki,
                               giry=giry,
                               ugl=ugl)

@app.route('/eatrender', methods=['POST'])
def eat_add_render():
    return eat_render()
@app.route('/eatadd', methods=['POST'])
def eat_add():
    return render_template('pages/lk/eat_add.html')

@app.route('/train')
def train_render():
    a = datetime.now()
    b = timedelta(days=1)
    c = datetime(2018,10,10,0,0,0)
    str(a)
    tomorrow_data = a + b
    now_data = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
    current_data = datetime.strftime(tomorrow_data, "%Y-%m-%d %H:%M:%S")

    time_now = datetime.strftime(datetime.now(), "%H:%M:%S")
    time_zero = datetime.strftime(c, "%H:%M:%S")
    # if time_now == time_zero:
    return render_template('pages/lk/train.html')


@app.route('/home', methods=['POST'])
def start_home():
    user = User.query.get(USER_ID)
    username = user.username
    print(username)
    return render_template('pages/lk/home.html', username=username)


@app.route('/progress')
def progress_render():
    global USER_ID
    # query = db_session.query(user_info)
    results = user_info.query.filter(user_info.user_id_helper == USER_ID)
    # results = query.all()
    print('Hueg', results)
    table = Results(results, classes=['yellowTable'])
    table.border = True

    return render_template('pages/lk/progress.html', table=table)


@app.route('/progress', methods=['POST'])
def progress_btn():
    return userinfo_add_render()


#
# # Error handlers.
#
#
# @nerofit.errorhandler(500)
# def internal_error(error):
#     db_session.rollback()
#     return render_template('errors/500.html'), 500
#
#
# @nerofit.errorhandler(404)
# def not_found_error(error):
#     return render_template('errors/404.html'), 404


@app.route('/testpopup')
def popup_render():
    return render_template('another/test.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/article')
def article_render():
    return render_template('another/article.html')

@app.route('/video')
def video_render():
    return render_template('another/template.html')


def calculator():
    global USER_ID
    user = User.query.get(USER_ID)
    print('metatag usera', user.username)
    mass = int(user.massuser)
    gender = int(user.gender)

    r = r_calc()
    l = l_calc()

    m=mass

    if (gender == 1):
        Dn = (6.83 * m + 7 * (m * 26.67 * r * (1 + l))) * 0.13
        return Dn
    elif (gender == 2):
        Dn = (5.94 * m + 7 * (m * 24.44 * r * (1 + l))) * 0.13
        return Dn
    else:
        return


def belki_calc():
    Dn = calculator()
    return 0.075*Dn

def giry_calc():
    Dn = calculator()
    return 0.04*Dn

def ugl_cal():
    Dn = calculator()
    return 0.088*Dn

def r_calc():
    global USER_ID
    user = User.query.get(USER_ID)
    age = int(user.data)
    r=1
    if age<=25:
        r=1
    elif 25<age<=35:
        r=0.95
    elif 35<age<=45:
        r=0.9
    elif 45<age<=55:
        r=0.85
    elif age>55:
        r=0.8
    return float(r)

def l_calc():
    global USER_ID
    user = User.query.get(USER_ID)
    activity = 1
    activity = int(user.activity)
    l =0.06
    if (activity == 1):
        l=0.05
    elif(activity == 2):
        l = 0.06
    elif(activity == 3):
        l=0.07
    else:
        l=0.06
    return float(l)



@app.route('/test')
def start_test_var():
    return start_var_render()

@app.route('/test/start_var')
def start_var():
    return start_var_render()

@app.route('/test', methods=['POST'])
def start_var_render():
    return render_template('voronka/start_voronka.html')


@app.route('/test/gender_var')
def gender_var():
    return gender_var_render()

@app.route('/test/gender_var', methods=['POST'])
def gender_var_render():
    return render_template('voronka/gender_var.html', data=poll_data)

@app.route('/test/age_var')
def date_var():
    return data_var_render()

@app.route('/test/age_var', methods=['POST'])
def data_var_render():
    return render_template('voronka/age_var.html')

@app.route('/test/height_var')
def height_var():
    return height_var_render()

@app.route('/test/height_var', methods=['POST'])
def height_var_render():
    return render_template('voronka/height_var.html')

@app.route('/test/mass_var')
def mass_var():
    return mass_var_render()

@app.route('/test/mass_var', methods=['POST'])
def mass_var_render():
    return render_template('voronka/mass_var.html')

@app.route('/test/exp_var')
def exp_var():
    return exp_var_render()

@app.route('/test/exp_var', methods=['POST'])
def exp_var_render():
    return render_template('voronka/exp_var.html', data=exp_var_data)

@app.route('/test/eating_var')
def eating_var():
    return eating_var_render()

@app.route('/test/eating_var', methods=['POST'])
def eating_var_render():
    return render_template('voronka/eating_var.html', data=eating_var_data)

@app.route('/test/training_var')
def training_var():
    return training_var_render()

@app.route('/test/training_var', methods=['POST'])
def training_var_render():
    return render_template('voronka/training_var.html', data=training_var_data)

@app.route('/test/email_var')
def email_var():
    return email_var_render()

@app.route('/test/email_var_var', methods=['POST'])
def email_var_render():
    return render_template('voronka/email_var.html')

