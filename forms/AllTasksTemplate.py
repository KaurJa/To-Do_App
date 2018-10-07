from anvil import *
import anvil.tables as tables
from anvil.tables import app_tables
from TaskEdit import TaskEdit
from datetime import datetime

class AllTasksTemplate(AllTasksTemplateTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def delete_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    #this line delete item but not showing right away
    self.item.delete()
    #adding this line would delete item right away
    self.remove_from_parent()

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert(TaskEdit(item=self.item), title= "edit", Large=True)
    self.refresh_data_bindings()

  def task_link_click(self, **event_args):
    """This method is called when the link is clicked"""
#    alert('hello how are you?')
#this line pops up a description when task link is clicked
    description_task = self.item['description']
  
    if self.item['completed on']:
      #this line pops up when the task was completed on(including date and time)
      current_time = self.item['completed on'].strftime('%b' ' %d' ' %y')
      #alert() is what makes description_task and current_time pops up together
      alert(description_task + '\n' 'Task completed on:' + current_time)
      
    else:
      alert(description_task)
      

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.item['Done'] == True:
      self.item['completed on'] = datetime.now()
      print(self.item['completed on'] . strftime('%b'' %d'' %y'))
        
        
    





