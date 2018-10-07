from anvil import *
import anvil.tables as tables
from anvil.tables import app_tables

class Form1(Form1Template):

  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    #this line of code display all the tasks from reminder data table
    #this line detects a row with task from reminder data table
    self.repeating_panel_1.items = app_tables.reminders.search()
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_row = app_tables.reminders.add_row(task=self.new_reminder_box.text, Done=False )
    existing = list(self.repeating_panel_1.items) + [new_row]
    self.repeating_panel_1.items = existing

