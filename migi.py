import pyautogui
import time
import pyjokes
from ai import AI
from todo import Todo , Item

migi = AI()
todo = Todo()
item = Item()

def joke():
    funny = pyjokes.get_joke()
    print(funny)
    migi.say(funny)

def add_todo()->bool:
    migi.say("Tell me what do you wanna add in the list")
    try:
        item.title = migi.listen()
        todo.new_item(item)
        message = "Added " + item.title
        migi.say(message)
        return True
    except:
        print("Oops there was an error")
        return False

def list_todos():
    if len(todo)>0:
        migi.say("So this is your to do's list")
        for item in todo:
            migi.say(item.title)
    else:
        migi.say("the list empty for now")

def remove_todo()->bool:
    migi.say("Tell me which stuff to remove")
    try:
        item_title = migi.listen()
        todo.remove_item(title=item_title)
        message = "Removed" + item_title
        migi.say(message)
        return True
    except:
        print("oops there was an error")
        return False


command = ""
migi.say("hello")
while True and command != "goodbye" :
    try:
        command = migi.listen()
        command = command.lower()
    except:
        print("Oops there was an error")
        command = ""
    print("command was:",command)

    if command=="tell me a joke":
        joke()
        command = ""
    if command in ["add to-do","add to do","add item","add task","add a task"]:
        add_todo()
        command  = ""
    if command in ["list my task","show my task","what is my task","list my item","list items"]:
        list_todos()
        command  =""
    if command in ["remove todo","remove item","remove task","delete item"]:
        remove_todo()
        command=""
    if command in ["minimise the terminal","minimise terminal","open the terminal","open terminal"]:
        pyautogui.click(167,743,1)
        
    
migi.say("Goodbye for now ,my firend")