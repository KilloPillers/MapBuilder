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
    if filename == '':
        return
    with open(filename, 'rb') as pickle_file:
        M.PickleLoad(pickle_file)

def PickleSaveMap():
    filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                            title="Save a File",
                                            defaultextension=".pickle",
                                            confirmoverwrite= False)
    if filename == '':
        return
    with open(filename, 'wb') as pickle_file:
        M.PickleSave(pickle_file)

class OutputCodeFrame(tk.Frame):
    def __init__(self, container, map_code, unit_code, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        map_code_label = tk.Label(self, text="Map Code")
        mv = ttk.Scrollbar(self, orient='vertical')
        map_code = MapCodeText(self, map_code)
        map_code.configure(yscrollcommand=mv.set)
        mv.configure(command=map_code.yview)
        unit_code_label = tk.Label(self, text="Unit Code")
        uv = ttk.Scrollbar(self, orient='vertical')
        unit_code = UnitCodeText(self, unit_code)
        unit_code.configure(yscrollcommand=uv.set)
        uv.configure(command=unit_code.yview)
        close = tk.Button(self, text="Hide Code Window", command=self.hide, bg="#f25a5a")
        map_code_label.grid(row=0, column=0, columnspan=2, sticky="we")
        unit_code_label.grid(row=0, column=2, columnspan=2, sticky="we")
        map_code.grid(row=1, column=0)
        mv.grid(row=1, column=1, sticky="ns")
        unit_code.grid(row=1, column=2)
        uv.grid(row=1, column=3, sticky="ns")
        close.grid(row=2, column=0, columnspan=4, sticky="we")

    def hide(self):
        self.grid_forget()
        self.destroy()

class MapCodeText(tk.Text):
    def __init__(self, container,   code, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(height=40)
        self.insert(tk.END, code)

class UnitCodeText(tk.Text):
    def __init__(self, container, code, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(height=40)
        self.insert(tk.END, code)


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
    unit_list = []
    map_code = "local newheights = {};\n"
    map_code += "local mapXSize = " + str(len(ButtonGrid)) + ';\n'
    map_code += "local mapYSize = " + str(len(ButtonGrid[0])) + ';\n'

    for count, ButtonList in enumerate(ButtonGrid):
        map_code += "newheights[" + str(count + 1) +  "] = {"
        for Button in ButtonList:
            if Button.tile.is_deploy_position:
                deploy_position_list.append(Button.tile)
            if Button.tile.is_action_tile:
                action_tile_list.append(Button.tile)
            if Button.tile.has_unit:
                unit_list.append(Button.tile)
            map_code += str(Button.tile.tile_height) + ','
        map_code = map_code[:-1]
        map_code += "}\n"
    map_code += "local newmap = GameMap.new(newheights, mapXSize, mapYSize)\n"
    for tile in deploy_position_list:
        map_code += "table.insert(newmap.deployPositions, Vector2.new" + str(tuple([x + 1 for x in tile.tile_position])) + ')\n'
    for tile in action_tile_list:
        map_code += "table.insert(newmap.actiontiles, ActionTile.new(" + "\"" + tile.tile_name + "\"," + str(tile.event_id) + ", " + "Vector2.new" + str(tuple([x + 1 for x in tile.tile_position])) + "))\n"

    unit_code = ""
    header = "local classid = nil;\nlocal currUnitIndex = 1;\nlocal unitid = nil;\nlocal personality = nil;\nlocal enemyUnit = nil;\nlocal position = nil;\n"
    unit_id_pos = "classid = {};\nunitid = {};\nposition = Vector2{};\n\nenemyUnit = Unit.new(position, 0,-1)\n"
    tablecode = "enemyUnit.classid = classid\nenemyUnit.weapon = ClassLookup[classid][\"WeaponType\"];\nenemyUnit.range = ClassLookup[classid][\"Move\"];\nenemyUnit.class = ClassLookup[classid][\"Name\"];\nenemyUnit.rawStats = ClassLookup[classid][\"StartingStats\"]\nenemyUnit.img = ClassLookup[classid][\"Image\"];\nenemyUnit.unitIndex = currUnitIndex;\ncurrUnitIndex+=1;\nfor i,v in pairs(ClassLookup[classid][\"ElementResists\"]) do\n    enemyUnit[i] = v;\nend\n\n"
    unit_stats = "enemyUnit.rawStats.maxhp = {}\nenemyUnit.hp = {};\nenemyUnit.rawStats.maxsp = {}\nenemyUnit.sp = {};\nenemyUnit.rawStats.atk = {}\nenemyUnit.rawStats.def = {}\nenemyUnit.rawStats.spd = {}\nenemyUnit.rawStats.hit = {}\nenemyUnit.rawStats.int = {}\nenemyUnit.rawStats.res = {}\nenemyUnit.id = {};\nenemyUnit.name = \"{}\"\n"
    footer = "personality = \"{}\"\nenemyUnit.personality = game:GetService(\"ServerStorage\").AIPersonalities:FindFirstChild(personality);\nenemyUnit.deathevent = {};\n\nnewmap:PlaceUnit(enemyUnit,position.x,position.y);\n\n\n"
    unit_code += header
    for count, tile in enumerate(unit_list):
        unit = tile.unit
        unit_code += unit_id_pos.format(unit.classID, unit.unitID, tuple(tile.tile_position))
        unit_code += tablecode
        unit_code += unit_stats.format(unit.maxHP, unit.maxHP, unit.maxSP, unit.maxSP, unit.Atk, unit.Def, unit.Spd, unit.Hit, unit.Int, unit.Res, unit.unitID, unit.unitName)
        for skill in [s for s in unit.skills if s != ""]:
            unit_code += "table.insert(enemyUnit.skills,{}\n".format(skill)
        unit_code += "\n"
        for passive in [p for p in unit.passives if p != ""]:
            unit_code += "table.insert(enemyUnit.passives,{})\n".format(passive)
        unit_code += "\n"
        unit_code += footer.format(unit.personality, unit.deathEvent)

    generated_code = OutputCodeFrame(root, map_code, unit_code, width=int(root.winfo_width() / 10), height=int(root.winfo_height() / 10))
    generated_code.grid(row=0, column=0, columnspan=2, sticky="nswe")

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
