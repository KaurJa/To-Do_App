from anvil import *
import anvil.tables as tables
from anvil.tables import app_tables
from TaskEdit import TaskEdit

class ItemTemplate1(ItemTemplate1Template):

  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def delete_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.item.delete()
    self.remove_from_parent()

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    alert(TaskEdit(item=self.item), title= "edit task details", Large=True)
    self.refresh_data_bindings()



