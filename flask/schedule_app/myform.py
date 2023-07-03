from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.fields.html5 import DateTimeLocalField, DateField,EmailField 
from wtforms.validators import DataRequired,InputRequired, Email, Length 

class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators = [InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=4, max=50)])

class RegisterForm(FlaskForm):
    username = StringField("Имя пользователя", validators = [InputRequired(), Length(min=4, max=15)])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    surname = StringField('Фамилия', validators = [InputRequired(), Length(min=4, max=15)])
    name = StringField("Имя", validators = [InputRequired(), Length(min=4, max=15)])
    ochestvo = StringField("Отчество", validators = [InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=4, max=50)])

class DateForm(FlaskForm):
    dateFrom = DateField("С", format='%Y-%m-%d', validators = [InputRequired()])
    dateTo   = DateField("До", format='%Y-%m-%d', validators = [InputRequired()])

class ILessonsForm(FlaskForm):
      teacher  = StringField('Выберите Препода', validators = [InputRequired()], render_kw={"list" : "t"})
      groups   = StringField('Выберите группу', validators = [InputRequired()],   render_kw={"list" : "g"})
      subject  = StringField('Выберите предмет', validators = [InputRequired()], render_kw={"list" : "s"})
      classroom  = StringField('Выберите аудиторию', validators = [InputRequired()], render_kw={"list" : "c"})
      dateFrom = DateField("Дата начала", format='%Y-%m-%d', validators = [InputRequired()])
      dateTo   = DateField("Дата окончания", format='%Y-%m-%d', validators = [InputRequired()])

class ITeachersForm(FlaskForm):
    surname = StringField('Фамилия', validators = [InputRequired(), Length(min=4, max=15)])
    name = StringField("Имя", validators = [InputRequired(), Length(min=4, max=15)])
    ochestvo = StringField("Отчество", validators = [InputRequired(), Length(min=4, max=15)])

class IStudensForm(FlaskForm):
    surname = StringField('Фамилия', validators = [InputRequired(), Length(min=4, max=15)])
    name = StringField("Имя", validators = [InputRequired(), Length(min=4, max=15)])
    ochestvo = StringField("Отчество", validators = [InputRequired(), Length(min=1, max=15)])
    idGroup = StringField("Выберите группу", validators = [InputRequired(), Length(min=1, max=15)], render_kw={"list" : "ig"})

class ISubjectsForm(FlaskForm):
    subject = StringField('Название предмета', validators = [InputRequired(), Length(min=1, max=15)])

class IGroupsForm(FlaskForm):
    groups = StringField('Номер группы', validators = [InputRequired(), Length(min=1, max=15)])
    facult = StringField('Номер факультета', validators = [InputRequired(), Length(min=1, max=15)]
                                                           , render_kw={"list" : "f"})

class IClassroomsForm(FlaskForm):
    corpus  =  StringField('Выберите корпус', render_kw={"list" : "ik"})
    icorpus =  StringField('Номер корпуса')
    ncalss  =  StringField("Номер аудитории")

class IDepartmentForm(FlaskForm):
    facult = StringField('Номер факультета', validators = [InputRequired(), Length(min=1, max=15)])

class UClassroomsForm(FlaskForm):
    icorpus  =  StringField('Выберите корпус', validators = [InputRequired(), Length(min=1, max=15)],  render_kw={"list" : "ik"})
    corpus =   StringField('Введите новое название корпуса', validators = [InputRequired(), Length(min=1, max=15)])
   
class UStudensForm(FlaskForm):
    surname = StringField('Фамилия', validators = [Length(min=4, max=15)])
    name = StringField("Имя", validators = [Length(min=4, max=15)])
    ochestvo = StringField("Отчество", validators = [Length(min=1, max=15)])
    idGroup = StringField("Выберите группу", validators = [Length(min=1, max=15)], render_kw={"list" : "ig"})
    idStudents = StringField("Выберите студента", validators = [Length(min=1, max=15)], render_kw={"list" : "is"})


class ULessonsForm(FlaskForm):
      idL      = StringField('Выберите занятие, для изменения', validators = [InputRequired()], render_kw={"list" : "il"})
      teacher  = StringField('Выберите Препода',   render_kw={"list" : "t"})
      groups   = StringField('Выберите группу',       render_kw={"list" : "g"})
      subject  = StringField('Выберите предмет',     render_kw={"list" : "s"})
      classroom  = StringField('Выберите аудиторию', render_kw={"list" : "c"})
      dateFrom = DateField("Дата начала", format='%Y-%m-%d')
      dateTo   = DateField("Дата окончания", format='%Y-%m-%d')

class UTeachersForm(FlaskForm):
    idT     =  StringField('Выберите Препода, для изменения', validators = [InputRequired()], render_kw={"list" : "it"})
    surname = StringField('Фамилия',  validators = [Length(min=4, max=25)])
    name = StringField("Имя",  validators = [Length(min=4, max=25)])
    ochestvo = StringField("Отчество",  validators = [Length(min=4, max=25)])

class USubjectsForm(FlaskForm):
    idS     = StringField('Выберите предмет, для изменения', validators = [InputRequired()], render_kw={"list" : "is"})
    subject = StringField('Номер предмета', validators = [InputRequired(), Length(min=1, max=15)])

class UGroupsForm(FlaskForm):
    idG    = StringField('Выберите группу, для изменения', validators = [InputRequired()], render_kw={"list" : "ig"})
    groups = StringField('Номер группы', validators = [Length(min=1, max=15)])
    facult = StringField('Номер факультета', validators = [Length(min=1, max=15)]
                                                           , render_kw={"list" : "f"})

class UDepartmentForm(FlaskForm):
    idF    = StringField('Выберите факультет, для изменения', validators = [InputRequired()], render_kw={"list" : "if"})
    facult = StringField('Номер факультета', validators = [InputRequired(), Length(min=1, max=15)])

class DLessonsForm(FlaskForm):
      idL      = StringField('Выберите занятие, для удаления', validators = [InputRequired()], render_kw={"list" : "il"})

class DSubjectsForm(FlaskForm):
    idS     = StringField('Выберите предмет, для удаления', validators = [InputRequired()], render_kw={"list" : "is"})

class DTeachersForm(FlaskForm):
    idT     =  StringField('Выберите Препода, для удаления', validators = [InputRequired()], render_kw={"list" : "it"})
   
class DGroupsForm(FlaskForm):
    idG    = StringField('Выберите группу, для удаления', validators = [InputRequired()], render_kw={"list" : "ig"})
   
class DDepartmentForm(FlaskForm):
    idF    = StringField('Выберите факультет, для удаления', validators = [InputRequired()], render_kw={"list" : "if"})
    
class DStudensForm(FlaskForm):
    idStudents = StringField("Выберите студента, для удаления", validators = [Length(min=1, max=15)], render_kw={"list" : "is"})

class DateSubjects(FlaskForm):
    dateFrom = DateField("Дата начала", format='%Y-%m-%d', validators = [InputRequired()])
    dateTo   = DateField("Дата окончания", format='%Y-%m-%d', validators = [InputRequired()])

class DClassroomsForm(FlaskForm):
    a = StringField("Выберите аудиторию", validators = [Length(min=1, max=15)], render_kw={"list" : "ia"})
    c = StringField("Выберите корпус",    validators = [Length(min=1, max=15)], render_kw={"list" : "ic"})

class MyEmail(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email()])

class ChangePassword(FlaskForm):
      password = PasswordField('Введите новий пароль', validators=[InputRequired(), Length(min=4, max=50)])

class DayClassroomsForm(FlaskForm):
    d = StringField("Выберите аудиторию", validators = [InputRequired(), Length(min=1, max=15)], render_kw={"list" : "id"})