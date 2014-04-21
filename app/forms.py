#from flask.ext.wtf import Form
from wtforms import Form, TextField, BooleanField, IntegerField, SelectMultipleField, SelectField
from wtforms import RadioField, FieldList
from wtforms import widgets
from wtforms.validators import Required, NumberRange

class SpecConfigForm(Form):
    initial_load = IntegerField('Initial Load (IOPS)')
    #                                validators = [NumberRange(), Required()])
    load_increment = IntegerField('Load increment per test run (IOPS)')
    num_tests = IntegerField('Number of test runs')
    spec1 = BooleanField( "spec1" , default = False)
    spec2 = BooleanField( "spec2" , default = False)
    spec3 = BooleanField( "spec3" , default = False)
    spec4 = BooleanField( "spec4" , default = False)
    spec5 = BooleanField( "spec5" , default = False)
    spec6 = BooleanField( "spec6" , default = False)
    spec7 = BooleanField( "spec7" , default = False)
    spec8 = BooleanField( "spec8" , default = False)
    spec9 = BooleanField( "spec9" , default = False)
    spec10 = BooleanField( "spec10" ,default = False)

    speed = RadioField('speed', choices=[ ('1gig', '1 gig interface'), ('10gig', '10 gig interface') ] )
