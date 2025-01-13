from cfg import modal_name, modal_short_name, my_name, my_short_name
from typing import Literal


t_my_name = Literal[my_name, my_short_name]
t_modal_name = Literal[modal_name, modal_short_name]
