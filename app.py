from flask import Flask,render_template,url_for,redirect,session,flash,request,blueprints
from tasklists import TaskList,Task,Status,Priority
from functools import wraps
from data import generate_tasklists,Task,generate_lists
from enum import Enum
from lists import List
from sigup import RegistrationForm
from login import LoginForm

#Generate Dummy data
tasks_list = generate_tasklists() #it contain the tasks for the list
lists_ = generate_lists() # it contain the lists of tasks

# define class for users
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'
# add the users to list of users
users = []
users.append(User(id=1, username='Fiddah', password='1234'))
users.append(User(id=2, username= 'areej',password='131314'))


    # create the Flask
app = Flask(__name__)
app.secret_key = '&*&*15DFDJ'

    #define route to home page
@app.route('/')
def home():
    return render_template('base.html')

@app.route('/profile')
def profile():
    form = LoginForm()
    username= form.name.data
    return render_template('profile.html',form=form,username=username)

@app.route('/login', methods =['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # read values from the login form
        username= form.name.data
        password = form.password.data
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('lists'))

        return redirect(url_for('login'))
  
    return render_template('login.html',form=form,title=login)
    


@app.route('/session')
def show_session():
    return dict(session)

@app.route('/logout')
def logout():
    session.clear()

    # redirect to index
    return redirect("/")

@app.route('/register',methods=['POST','GET'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('register.html',form=form)


#define log in required function
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
    return wrap


#define tasks route to show the tasks
@app.route('/tasks')
def tasks_():
    return render_template('tasks.html',taskslists = tasks_list.get_taskslists())

#define add_task route to add tasks
@app.route('/add_task',methods =['GET','POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        # status = request.form['status']
        # priority = request.form['priority']
        description = request.form['description']

        task = Task(name,1,1,description)
        tasks_list.add_task(task)

        return render_template('tasks.html',taskslists = tasks_list.get_taskslists())
    else:
        return render_template('addtask.html')

# define delete route to delete task
@app.route('/delete/<int:id>',methods = ['GET','POST'])
def delete(id):
    id =int(id)
    tasks_list.remove_task(id)
    return redirect(url_for('tasks_'))

#define edit route to edit the task
@app.route('/edit/<int:id>' , methods = ["POST", "GET"])
def edit(id):
    if request.method == "POST":
        task = tasks_list.get_task_by_id(id)

        name = request.form['name'] 
        # status = request.form['status'] #it make error the value of status undefined
        # priority = request.form['priority']
        description= request.form['description']

        task.set_task_name(name)
        # task.set_status(status)
        # task.set_priority(priority)
        task.set_description(description)

        return redirect(url_for('tasks_'))

    else:
        task = tasks_list.get_task_by_id(id)
        return render_template('edit.html',task = task)


#define lists route to show the lists
@app.route('/lists')
def lists():
    return render_template('lists.html',todolist= lists_.get_todolist())


@app.route('/deletelist/<int:id>',methods = ['GET','POST'])
def deletelist(id):
    id =int(id)
    lists_.remove_list(id)
    return redirect(url_for('lists'))


@app.route('/editlist/<int:id>' , methods = ["POST", "GET"])
def editlist(id):
    if request.method == "POST":
        list_ = lists_.get_list_by_id(id)
        listname = request.form['listname'] 
        list_.set_listname(listname)
        return redirect(url_for('lists'))
    else:
        list_ = lists_.get_list_by_id(id)
        return render_template('editlist.html',list_=list_)


@app.route('/add_list',methods =['GET','POST'])
def add_list_():
    if request.method == 'POST':
        listname = request.form['listname']
        list_ = List(listname)
        lists_.add_list(list_)
        return render_template('lists.html',todolist= lists_.get_todolist())
    else:
        return render_template('addlist.html')


# # @app.route('/veiwlist/<int:id>',methods = ['GET','POST'])
# # def veiw_lists(id):
# #     id =int(id)
# #     lists_.get_list_by_id(id)
# #     list_=lists_.value_of_list(id)
# #     return render_template('viewlist.html',taskslists= list_.get_taskslists())


