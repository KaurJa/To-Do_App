from anvil import *
import anvil.tables as tables
from anvil.tables import app_tables

class AllTasks(AllTasksTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    #this line of code display all the tasks from reminder data table(if manually type a task in data table)
    #this line detects a row with task from reminder data table
    self.repeating_panel_1.items = app_tables.reminders.search()
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    #This line add a new task to our reminder data table at the backend(when type a new task in new_reminder_box)
    app_tables.reminders.add_row(task=self.new_reminder_box.text, Done=False )
    
    #this line display task right away at frontend(when add/type a new task in new_reminder_box)
    self.repeating_panel_1.items = app_tables.reminders.search()
    
    #this line make the new_reminder_box empty as soon done writing a task
    self.new_reminder_box.text = ''
    
#    existing = list(self.repeating_panel_1.items) + [new_row]
#    self.repeating_panel_1.items = existing

