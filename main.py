import tkinter as tk
from MapGridClass import MapGrid, ConfigurationFrame
from Graph import MapGraph

class CodeText(tk.Text):
    def __init__(self, container, code, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.insert(tk.END, code)
        self.text = tk.Text(container, kwargs)
        self.bind("<Escape>", lambda e: self.hide(e), add="+")
    def hide(self, e):
        self.grid_forget()

def ShowGraph():
    heights = []
    for y in range(len(M.ButtonGrid)):
        for x in range(len(M.ButtonGrid[y])):
            heights.append(float(M.ButtonGrid[y][x].tile_height))
    graph_widget = MapGraph(root, heights, len(M.ButtonGrid), len(M.ButtonGrid[y]))

def ExportToLuaCode():
    if M.ButtonGrid == [[]]:
        return
    ButtonGrid = list(zip(*M.ButtonGrid))
    deploy_position_list = []
    action_tile_list = []
    code = "local newheights = {};\n"
    code += "local mapXSize = " + str(len(ButtonGrid)) + ';\n'
    code += "local mapYSize = " + str(len(ButtonGrid[0])) + ';\n'

    for count, ButtonList in enumerate(ButtonGrid):
        code += "newheights[" + str(count + 1) +  "] = {"
        for Button in ButtonList:
            if Button.is_deploy_position:
                deploy_position_list.append(Button)
            if Button.is_action_tile:
                action_tile_list.append(Button)
            code += str(Button.tile_height) + ','
        code = code[:-1]
        code += "}\n"
    code += "local newmap = GameMap.new(newheights, mapXSize, mapYSize)\n"
    for tile in deploy_position_list:
        code += "table.insert(newmap.deployPositions, Vector2.new" + str(tuple([x + 1 for x in tile.tile_position])) + ')\n'
    for tile in action_tile_list:
        code += "table.insert(newmap.actiontiles, ActionTile.new(" + "\"" + tile.tile_name + "\"," + str(tile.event_id) + ", " + "Vector2.new" + str(tuple([x + 1 for x in tile.tile_position])) + "))\n"

    code_text = CodeText(root, code, width=int(root.winfo_width()/10), height=int(root.winfo_height()/10))
    code_text.grid(row=0, column=0, sticky="we")
    #f = open("LuaFile.txt", 'w')
    #f.write(code)
    #f.close()

root = tk.Tk()
root.title("Map Building Tool")
root.resizable(False, False) #resizing is for screenlits
right_frame = tk.Frame(root)
O = ConfigurationFrame(right_frame, text="Tile Configuration")
M = MapGrid(root, 50, 50, 500, 500, O)
ExportButton = tk.Button(right_frame, text="Export To Lua Code", command=ExportToLuaCode)
ShowGraph = tk.Button(right_frame, text="Show Graph", command=ShowGraph)
M.grid(row=0, column=0)
right_frame.grid(row=0, column=1)
O.grid(row=0, column=0)
ExportButton.grid(row=1, column=0, pady=5, padx=5)
ShowGraph.grid(row=2, column=0, pady=5, padx=5)

root.mainloop()
