#   Alex Dulac

import cmd
import os,sys
import textwrap
import json

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')   

class Scene():
    def __init__(self, id=0, name="", description="", next={}, npc="", inventory=""):
        self.id = id
        self.name = name
        self.description = description
        self.next = next
        self.npc = npc
        self.inventory = inventory
        
    def _next(self, direction):
        if direction in self.next:
            return self.next[direction]
        else:
            return None    
            
def get_scene(id):
    pathname = os.path.join("scenes", str(id)+".json")
    with open(pathname) as fh:
        jsontext = fh.read()
        d = json.loads(jsontext)
        d['id'] = id
        s = Scene(**d)
    return s

class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        
        self.loc = get_scene(1)
        self.look()
        
    def move (self, dir):
        newscene = self.loc._next(dir)
        if newscene is None:
            print("This is not a valid action in the current environment. Try again.")
        else:
            self.loc = get_scene(newscene)
            self.look()

    def look(self):
        clear_screen()
        print(self.loc.name)
        print("")
        for line in textwrap.wrap(self.loc.description, 80):
            print(line)
        print("")
        for line in textwrap.wrap(self.loc.npc, 80):
            print(line)
        print("")
        for line in textwrap.wrap(self.loc.inventory, 80):
            print(line)
        
    def do_n(self, args):
        """Go north"""
        self.move("n")
        
    def do_s(self, args):
        """Go south"""
        self.move("s")

    def do_e(self, args):
        """Go east"""
        self.move("e")
        
    def do_w(self, args):
        """Go west"""
        self.move("w")
        
    def do_start(self, args):
        """Starts the game"""
        self.move("start")
        
    def do_restart(self, args):
        """Restarts the game"""
        self.move("restart")
        
    def do_yes(self, args):
        """yes"""
        self.move("yes")
        
    def do_no(self, args):
        """no"""
        self.move("no")
        
    def do_i(self, args):
        """Interact"""
        self.move("i")    
        
    def do_quit(self, args):
        """Quits the game"""
        print ("You have quit the game. Thank you for playing.")
        return True
        
if __name__ == "__main__":
    g = Game()
    g.cmdloop()
