import tkinter as tk
from MapGridClass import MapGrid, ConfigurationFrame, UnitFrame
from Graph import MapGraph
from tkinter import ttk, filedialog
import os

def PickleLoadMap():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select a File",
                                          filetypes=(("Pickle Files",
                                                      "*.pickle*"),))
    with open(filename, 'rb') as pickle_file:
        M.PickleLoad(pickle_file)

def PickleSaveMap():
    filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                            title="Save a File",
                                            defaultextension=".pickle",
                                            confirmoverwrite= False)
    with open(filename, 'wb') as pickle_file:
        M.PickleSave(pickle_file)

class CodeText(tk.Text):
    def __init__(self, container, code, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.insert(tk.END, code)
        self.text = tk.Text(container, kwargs)
        self.bind("<Escape>", lambda e: self.hide(e), add="+")
    def hide(self, e):
        self.grid_forget()
        self.destroy()

def ShowGraph():
    heights = []
    for y in range(len(M.ButtonGrid)):
        for x in range(len(M.ButtonGrid[y])):
            heights.append(float(M.ButtonGrid[y][x].tile.tile_height))
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
            if Button.tile.is_deploy_position:
                deploy_position_list.append(Button)
            if Button.tile.is_action_tile:
                action_tile_list.append(Button)
            code += str(Button.tile.tile_height) + ','
        code = code[:-1]
        code += "}\n"
    code += "local newmap = GameMap.new(newheights, mapXSize, mapYSize)\n"
    for Button in deploy_position_list:
        code += "table.insert(newmap.deployPositions, Vector2.new" + str(tuple([x + 1 for x in Button.tile.tile_position])) + ')\n'
    for Button in action_tile_list:
        code += "table.insert(newmap.actiontiles, ActionTile.new(" + "\"" + Button.tile.tile_name + "\"," + str(Button.tile.event_id) + ", " + "Vector2.new" + str(tuple([x + 1 for x in Button.tile.tile_position])) + "))\n"

    code_text = CodeText(root, code, width=int(root.winfo_width()/10), height=int(root.winfo_height()/10))
    code_text.grid(row=0, column=0, sticky="we")
    #f = open("LuaFile.txt", 'w')
    #f.write(code)
    #f.close()

filename = None

root = tk.Tk()
root.title("Map Building Tool")
root.resizable(False, False) #resizing is for screenlits
RightFrame = tk.Frame(root)
OutPutFrame = tk.Frame(RightFrame)
TabControl = ttk.Notebook(RightFrame)
TileConfigTabFrame = tk.Frame(TabControl)
UnitConfigTabFrame = tk.Frame(TabControl)
TabControl.add(TileConfigTabFrame, text="Tile Configuration")
TabControl.add(UnitConfigTabFrame, text="Unit Configuration")
TileConfigurations = ConfigurationFrame(TileConfigTabFrame)
M = MapGrid(root, 50, 50, 500, 500, TileConfigurations)
UnitConfigurations = UnitFrame(UnitConfigTabFrame, M)
ExportButton = tk.Button(OutPutFrame, text="Export To Lua Code", command=ExportToLuaCode)
ShowGraph = tk.Button(OutPutFrame, text="Show Graph", command=ShowGraph)
M.SetUnitFrame(UnitConfigurations)

SaveButton = tk.Button(OutPutFrame, command=PickleSaveMap, text="Save Map Data")
LoadButton = tk.Button(OutPutFrame, command=PickleLoadMap, text="Load Map Data")

M.grid(row=0, column=0)
RightFrame.grid(row=0, column=1, sticky="nw")
TabControl.grid(row=0, column=1, sticky="n")
OutPutFrame.grid(row=1, column=1, sticky="s")
ExportButton.grid(row=0, column=0, sticky="s", pady=5, padx=5)
ShowGraph.grid(row=1, column=0, sticky="s", pady=5, padx=5)
SaveButton.grid(row=2, column=0, sticky="s", pady=5, padx=5)
LoadButton.grid(row=3, column=0, sticky="s", pady=5, padx=5)

root.mainloop()
