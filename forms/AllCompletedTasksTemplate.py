from anvil import *
import anvil.tables as tables
from anvil.tables import app_tables

class AllCompletedTasksTemplate(AllCompletedTasksTemplateTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    store_description = str(self.item['description'])
    if self.item['completed on']:
      store_description = str(self.item['description'])
      store_time = self.item['completed on'].strftime('%b' ' %d' ' %y')
      alert(store_description + '\n' 'Task completed on:' + store_time)
    else:
      alert(store_description)
     
      

