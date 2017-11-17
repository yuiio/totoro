import os
from random import randint
from bottle import route, static_file, run, debug, template, redirect, request, response, get, post
from markdown import markdown
from persistance import User

user = User() # for data persistance

def is_logged():
    if not user.logged:
        redirect('/login')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/')

@route('/download/<filename>')
def download(filename):
    return static_file(filename, root='./static/', download=filename)

@route('/txt/<filename>')
def just_txt(filename):
    path = './static/{}'.format(filename)
    if os.path.exists(path):
        with open(path, 'r') as txt_data:
            txt = txt_data.read()
    else:
        txt = path
    return template('raw', body=txt)

@route('/')
def index():
    if user.logged:
        attr = [
            'href="/challenge/question1" class="calendar-complete"',
            'href="/challenge/question2" class="calendar-complete"',
            'href="/challenge/ahautevoix" class="calendar-complete"',
            'href="/challenge/conway" class="calendar-complete"',
            'href="/challenge/vroum" class="calendar-complete"',
            'href="/challenge/vigenere" class="calendar-complete"',
            'href="/challenge/temps" class="calendar-complete"',
            'href="/challenge/final" class="calendar-complete"',
            'href="/page/congratulations" class="calendar-complete"'
            ]

        for i in range(user.level+1, len(attr)):
            attr[i] = 'href="#"'
        attr[user.level] = attr[user.level].split(' ')[0]

        txt = ['' for i in range(9)]
        if user.level >= 7:
            txt[6] = ' |----> o <a href="/map">[ MapPlaques ]</a> o'
        if user.level == 8:
            txt[user.level] = '<--{ !!! Congratulations !!! }'
        else:
            txt[user.level] = '<--{ unlocked }'

        return template('index0', attr=attr, txt=txt)
    else:
        redirect('/login')

@get('/login')
def login():
    login_form = '''
    <form action="/login" method="post">
        Username: <input name="username" type="text" />
        Password: <input name="password" type="password" />
        <input value="[Login]" type="submit" />
    </form>
    '''
    return template('page', title='Please connect', body=login_form)


@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username == user.name and password == user.password:
        user.logged = True
        user.save()
        redirect('/')
    else:
        html = '<p>Login failed. <a href="/login">[Back]</a></p>'
        return template('page', title='Please connect', body=html)

@get('/logout')
def do_logout():
    user.logged = False
    user.save()
    redirect('/login')

@get('/reset')
def reset():
    user.init()
    user.save()
    redirect('/login')

@route('/page/<page_name>')
def page(page_name):
    is_logged()
    metas, content = page_parser(page_name)
    title = metas['title']
    html = markdown(content)
    return template('page', title=title, body=html)

@get('/challenge/<page_name>')
def question(page_name):
    is_logged()

    answer = None
    if page_name in user.reps:
        answer = user.reps[page_name]

    metas, content = page_parser(page_name)
    title = metas['title']
    next_level = metas['next_level']
    solution = metas['reponse']
    html = markdown(content)
    return template(
        'question',
        page_name=page_name,
        title=title,
        body=html,
        solution=solution,
        answer=answer,
        feedback=do_feedback(answer, solution, next_level)
        )

@post('/challenge/<page_name>')
def check_answer(page_name):
    is_logged()

    answer = request.forms.get('reponse')

    metas, content = page_parser(page_name)
    title = metas['title']
    solution = metas['reponse']
    next_level = metas['next_level']
    html = markdown(content)

    user.reps[page_name] = answer
    if answer == solution:
        user.level += 1
        if user.level == 7:
            user.map_unlocked = True
    user.save()

    return template(
        'question',
        page_name=page_name,
        title=title,
        body=html,
        solution=solution,
        answer=answer,
        feedback=do_feedback(answer, solution, next_level)
        )

@get('/tips')
def tips():
    is_logged()
    return template('tips', level=user.level)

@get('/map')
def map():
    is_logged()
    title = '--- { La map des plaques } ---'
    plaques = make_plaques(10000)
    plaques[525] = 'EQ-323-EF' # [x:26, y:6]
    plaques[750] = 'DL-572-EQ' # [x:51, y:8]
    plaques[8156] = 'HE-007-RE' # [x:57, y:82]
    plaques[2222] = 'LO-010-OL'

    lignes = []
    ligne = []

    for i in range(10000):
        ligne.append('<a href="/plak/{pl}">[{pl}]</a>'.format(pl=plaques[i]))
        if i%100 == 99:
            lignes.append(' '.join(ligne))
            ligne = []

    body = '<pre>\n{}\n</pre>'.format('\n'.join(lignes))
    return template('page', title=title, body=body)

@get('/plak/<page_name>')
def is_tresor(page_name):
    body = 'Rien à signaler ici.'
    title = '--- { Bureau du renseignement des plaques } ---'
    if page_name == 'EQ-323-EF':
        body = 'La plaque recherchée est dans la 57<sup>ème</sup> colonne.'
    if page_name == 'DL-572-EQ':
        body = 'La plaque recherchée est sur la 82<sup>ème</sup> ligne.'
    if page_name == 'HE-007-RE':
        body = 'C\'est la <em>fête</em>... <a href="/page/bingo">Bingo !</a>'
    if user.level == 8 and page_name == 'LO-010-OL':
        redirect('/page/abracadabra')
    return template('page', title=title, body=body)

def make_plaques(n):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaques = []
    for i in range(n):
        c1 = alpha[randint(0,25)]
        c2 = alpha[randint(0,25)]
        c3 = alpha[randint(0,25)]
        c4 = alpha[randint(0,25)]
        num = randint(0, 999)
        plaque = '{}{}-{}-{}{}'.format(c1, c2, str(num).zfill(3), c3, c4)
        plaques.append(plaque)
    return plaques

def do_feedback(answer, solution, next_level):
    if answer == solution:
        if user.level < 8:
            # feedback = 'Yeah ! Go to the [\[next level\]](/challenge/{}).  \
            # Dont\'forget to check your [\5[tipsbox\]](/tips).'.format(next_level)
            feedback = 'Yeah ! Go to the [\[next level\]](/).  \
            Dont\'forget to check your [\5[tipsbox\]](/tips).'
        else:
            feedback = '_Congratulation_ ! Maintenant [\[allez chercher\]](/) votre récompense _:)_'
    else:
        feedback = 'Try again !'
    return markdown(feedback)


def page_parser(page_name):
    metas = {}
    contents = []
    filename = './{}.md'.format(page_name)
    if os.path.exists(filename):
        with open(filename, 'r') as md_data:
            is_meta = True
            for line in md_data.readlines():
                if is_meta and line.strip() == '':
                    is_meta = False
                if is_meta:
                    meta_elts = line.strip().split(': ')
                    metas[meta_elts[0]] = meta_elts[1]
                else:
                    contents.append(line)

        return metas, ''.join(contents)
    else:
        redirect('/')



debug(True)
run(reloader=True)