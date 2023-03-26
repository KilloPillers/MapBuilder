import tkinter as tk
from MapGridClass import MapGrid, ConfigurationFrame

def ExportToLuaCode():
    ButtonGrid = M.ButtonGrid
    deploy_position_list = []
    action_tile_list = []
    code = "local newheights = {};\n"
    code += "local mapXSize = " + str(len(ButtonGrid[0])) + ';\n'
    code += "local mapYSize = " + str(len(ButtonGrid)) + ';\n'
    for ButtonList in ButtonGrid:
        code += "newheights[" + str(ButtonList[0].tile_position[1] + 1) + "] = {"
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
        code += "table.insert(newmap.deployPositions, Vector2.new" + str(tuple(tile.tile_position)) + ')\n'
    for tile in action_tile_list:
        code += "table.insert(newmap.actiontiles, ActionTile.new(" + "\"" + tile.tile_name + "\"," + str(tile.event_id) + ", " + "Vector2.new" + str(tuple(tile.tile_position)) + "))\n"
    f = open("LuaFile.txt", 'w')
    f.write(code)
    f.close()

def BuildMap():
    pass

root = tk.Tk()
root.resizable(False, False) #resizing is for screenlits
O = ConfigurationFrame(text="Tile Configuration")
M = MapGrid(root, 50, 50, 500, 500, O)
ExportButton = tk.Button(root, text="Export To Lua Code", command=ExportToLuaCode)
ExportButton.grid(row=0, column=1, sticky="se")
M.grid(row=0, column=0)
O.grid(row=0, column=1)

root.mainloop()
