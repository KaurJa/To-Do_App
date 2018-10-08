from anvil import *
import anvil.tables as tables
from anvil.tables import app_tables

class AllCompletedTasks(AllCompletedTasksTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
    self.repeating_panel_1.items = app_tables.reminders.search(Done=True)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('AllTasks')
    

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    #would refresh a page right away
    open_form('AllCompletedTasks')


