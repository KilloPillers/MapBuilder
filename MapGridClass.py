import pickle
import tkinter as tk
from tkinter import ttk

class Unit():
    def __init__(self,
            unitLevel="",
            unitName="",
            classID="",
            unitID="",
            personality="RandomAction",
            deathEvent="nil",
            maxHP="",
            maxSP="",
            Atk="",
            Def="",
            Spd="",
            Hit="",
            Int="",
            Res="",
            skills=["","","",""],
            passives=["","",""]
        ):
        self.unitLevel = unitLevel
        self.unitName = unitName
        self.classID = classID
        self.unitID = unitID
        self.personality = personality
        self.deathEvent = deathEvent

        self.maxHP = maxHP
        self.maxSP = maxSP
        self.Atk = Atk
        self.Def = Def
        self.Spd = Spd
        self.Hit = Hit
        self.Int = Int
        self.Res = Res

        self.skills = skills
        self.passives = passives

class UnitFrame(tk.Frame):
    def __init__(self, container, MapGrid, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.grid(row=0, column=0)

        self.MapGrid = MapGrid

        MiscLabelFrame = tk.LabelFrame(self, text="Misc")
        MiscLabelFrame.grid(row=0,column=0, columnspan=2)

        UnitNameLabel = tk.Label(MiscLabelFrame, text="Name: ")
        self.UnitNameEntry = tk.Entry(MiscLabelFrame, width=15, justify='center')
        self.UnitNameEntry.insert(0, "")
        UnitNameLabel.grid(row=1, column=0, sticky="we", padx=1)
        self.UnitNameEntry.grid(row=1, column=1)
        
        UnitLevelLabel = tk.Label(MiscLabelFrame, text="Level: ")
        self.UnitLevelEntry = tk.Entry(MiscLabelFrame, width=15, justify='center')
        self.UnitLevelEntry.insert(0, "")
        UnitLevelLabel.grid(row=2, column=0, sticky="we", padx=1)
        self.UnitLevelEntry.grid(row=2, column=1)

        ClassIDLabel = tk.Label(MiscLabelFrame, text="Class ID: ")
        self.ClassIDEntry = tk.Entry(MiscLabelFrame, width=5, justify='center')
        self.ClassIDEntry.insert(0, "")
        ClassIDLabel.grid(row=3, column=0, sticky="we", padx=1)
        self.ClassIDEntry.grid(row=3, column=1)

        UnitIDLabel = tk.Label(MiscLabelFrame, text="Unit ID: ")
        self.UnitIDEntry = tk.Entry(MiscLabelFrame, width=5, justify='center')
        self.UnitIDEntry.insert(0, "")
        UnitIDLabel.grid(row=4, column=0, sticky="we", padx=1)
        self.UnitIDEntry.grid(row=4, column=1)

        PersonalityLabel = tk.Label(MiscLabelFrame, text="Personality: ")
        self.PersonalityEntry = tk.Entry(MiscLabelFrame, width=20, justify='center')
        self.PersonalityEntry.insert(0, "RandomAction")
        PersonalityLabel.grid(row=5, column=0, sticky="we", padx=1)
        self.PersonalityEntry.grid(row=5, column=1)

        DeathEventLabel = tk.Label(MiscLabelFrame, text="Death Event: ")
        self.DeathEventEntry = tk.Entry(MiscLabelFrame, width=5, justify='center')
        self.DeathEventEntry.insert(0, "nil")
        DeathEventLabel.grid(row=6, column=0, sticky="we", padx=1)
        self.DeathEventEntry.grid(row=6, column=1)


        #rawStats LabelFrame
        rawStatsLabelFrame = tk.LabelFrame(self, text="Unit Stats")
        rawStatsLabelFrame.grid(row=1, column=0, rowspan=2, sticky="n")

        maxHPLabel = tk.Label(rawStatsLabelFrame, text="Max HP: ")#, bg="#fc2403", fg="#ffffff")
        self.maxHPEntry = tk.Entry(rawStatsLabelFrame, width=5, justify='center')
        self.maxHPEntry.insert(0, "")
        maxHPLabel.grid(row=1, column=0, sticky="we", padx=1)
        self.maxHPEntry.grid(row=1, column=1, padx=1)

        maxSPLabel = tk.Label(rawStatsLabelFrame, text="Max SP: ")#, bg="#0703fc", fg="#ffffff")
        self.maxSPEntry = tk.Entry(rawStatsLabelFrame, width=5, justify='center')
        self.maxSPEntry.insert(0, "")
        maxSPLabel.grid(row=2, column=0, sticky="we", padx=1)
        self.maxSPEntry.grid(row=2, column=1, padx=1)

        AtkLabel = tk.Label(rawStatsLabelFrame, text="Atk: ")#, bg="#000000", fg="#ff0000")
        self.AtkEntry = tk.Entry(rawStatsLabelFrame, width=5, justify='center')
        self.AtkEntry.insert(0, "")
        AtkLabel.grid(row=3, column=0, sticky="we", padx=1)
        self.AtkEntry.grid(row=3, column=1, padx=1)

        DefLabel = tk.Label(rawStatsLabelFrame, text="Def: ")#, bg="#000000", fg="#00ff00")
        self.DefEntry = tk.Entry(rawStatsLabelFrame, width=5, justify='center')
        self.DefEntry.insert(0, "")
        DefLabel.grid(row=4, column=0, sticky="we", padx=1)
        self.DefEntry.grid(row=4, column=1, padx=1)

        SpdLabel = tk.Label(rawStatsLabelFrame, text="Spd: ")#, bg="#000000", fg="#fffb00")
        self.SpdEntry = tk.Entry(rawStatsLabelFrame, width=5, justify='center')
        self.SpdEntry.insert(0, "")
        SpdLabel.grid(row=5, column=0, sticky="we", padx=1)
        self.SpdEntry.grid(row=5, column=1, padx=1)

        HitLabel = tk.Label(rawStatsLabelFrame, text="Hit: ")#, bg="#000000", fg="#fff200")
        self.HitEntry = tk.Entry(rawStatsLabelFrame, width=5, justify='center')
        self.HitEntry.insert(0, "")
        HitLabel.grid(row=6, column=0, sticky="we", padx=1)
        self.HitEntry.grid(row=6, column=1, padx=1)

        IntLabel = tk.Label(rawStatsLabelFrame, text="Int: ")#, bg="#000000", fg="#0000ff")
        self.IntEntry = tk.Entry(rawStatsLabelFrame, width=5, justify='center')
        self.IntEntry.insert(0, "")
        IntLabel.grid(row=7, column=0, sticky="we", padx=1)
        self.IntEntry.grid(row=7, column=1, padx=1)

        ResLabel = tk.Label(rawStatsLabelFrame, text="Res: ")#, bg="#000000", fg="#ff6a00")
        self.ResEntry = tk.Entry(rawStatsLabelFrame, width=5, justify='center')
        self.ResEntry.insert(0, "")
        ResLabel.grid(row=8, column=0, sticky="we", padx=1)
        self.ResEntry.grid(row=8, column=1, padx=1)

        #Unit Skills Frame
        UnitSkillsLabelFrame = tk.LabelFrame(self, text="Unit Skills")
        UnitSkillsLabelFrame.grid(row=1, column=1, sticky="n")
        Skill1 = tk.Label(UnitSkillsLabelFrame, text="Skill 1: ")
        self.Skill1Entry = tk.Entry(UnitSkillsLabelFrame, width=5, justify='center')
        self.Skill1Entry.insert(0, "")
        Skill1.grid(row=0, column=0)
        self.Skill1Entry.grid(row=0, column=1, padx=1)
        
        Skill2 = tk.Label(UnitSkillsLabelFrame, text="Skill 2: ")
        self.Skill2Entry = tk.Entry(UnitSkillsLabelFrame, width=5, justify='center')
        self.Skill2Entry.insert(0, "")
        Skill2.grid(row=1, column=0)
        self.Skill2Entry.grid(row=1, column=1, padx=1)

        Skill3 = tk.Label(UnitSkillsLabelFrame, text="Skill 3: ")
        self.Skill3Entry = tk.Entry(UnitSkillsLabelFrame, width=5, justify='center')
        self.Skill3Entry.insert(0, "")
        Skill3.grid(row=2, column=0)
        self.Skill3Entry.grid(row=2, column=1, padx=1)

        Skill4 = tk.Label(UnitSkillsLabelFrame, text="Skill 4: ")
        self.Skill4Entry = tk.Entry(UnitSkillsLabelFrame, width=5, justify='center')
        self.Skill4Entry.insert(0, "")
        Skill4.grid(row=3, column=0)
        self.Skill4Entry.grid(row=3, column=1, padx=1)

        # Unit Passive Frame
        UnitPassiveLabelFrame = tk.LabelFrame(self, text="Unit Passives")
        UnitPassiveLabelFrame.grid(row=2, column=1, sticky="n")
        Passive1 = tk.Label(UnitPassiveLabelFrame, text="Passive 1: ")
        self.Passive1Entry = tk.Entry(UnitPassiveLabelFrame, width=5, justify='center')
        self.Passive1Entry.insert(0, "")
        Passive1.grid(row=0, column=0)
        self.Passive1Entry.grid(row=0, column=1, padx=1)

        Passive2 = tk.Label(UnitPassiveLabelFrame, text="Passive 2: ")
        self.Passive2Entry = tk.Entry(UnitPassiveLabelFrame, width=5, justify='center')
        self.Passive2Entry.insert(0, "")
        Passive2.grid(row=1, column=0)
        self.Passive2Entry.grid(row=1, column=1, padx=1)

        Passive3 = tk.Label(UnitPassiveLabelFrame, text="Passive 3: ")
        self.Passive3Entry = tk.Entry(UnitPassiveLabelFrame, width=5, justify='center')
        self.Passive3Entry.insert(0, "")
        Passive3.grid(row=2, column=0)
        self.Passive3Entry.grid(row=2, column=1, padx=1)

        DeleteButton = tk.Button(self, text="Delete Unit", command=self.DeleteUnit, bg="#ff0000")
        DeleteButton.grid(row=3, column=0, padx=5, pady=5, sticky="we")

        SaveButton = tk.Button(self, text="Save Unit", command=self.SaveUnit, bg="#00ff00")
        SaveButton.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

    def LoadUnit(self, e):
        unit = self.MapGrid.focused_tile.tile.unit
        if unit is None:
            return

        self.UnitNameEntry.delete(0, "end")
        self.UnitLevelEntry.delete(0, "end")
        self.ClassIDEntry.delete(0, "end")
        self.UnitIDEntry.delete(0, "end")
        self.PersonalityEntry.delete(0, "end")
        self.DeathEventEntry.delete(0, "end")
        self.maxHPEntry.delete(0, "end")
        self.maxSPEntry.delete(0, "end")
        self.AtkEntry.delete(0, "end")
        self.DefEntry.delete(0, "end")
        self.SpdEntry.delete(0, "end")
        self.HitEntry.delete(0, "end")
        self.IntEntry.delete(0, "end")
        self.ResEntry.delete(0, "end")
        self.Skill1Entry.delete(0, "end")
        self.Skill2Entry.delete(0, "end")
        self.Skill3Entry.delete(0, "end")
        self.Skill4Entry.delete(0, "end")
        self.Passive1Entry.delete(0, "end")
        self.Passive2Entry.delete(0, "end")
        self.Passive3Entry.delete(0, "end")
        
        self.UnitNameEntry.insert(0, unit.unitName)
        self.UnitLevelEntry.insert(0, unit.unitLevel)
        self.ClassIDEntry.insert(0, unit.classID)
        self.UnitIDEntry.insert(0, unit.unitID)
        self.PersonalityEntry.insert(0, unit.personality)
        self.DeathEventEntry.insert(0, unit.deathEvent)
        self.maxHPEntry.insert(0, unit.maxHP)
        self.maxSPEntry.insert(0, unit.maxSP)
        self.AtkEntry.insert(0, unit.Atk)
        self.DefEntry.insert(0, unit.Def)
        self.SpdEntry.insert(0, unit.Spd)
        self.HitEntry.insert(0, unit.Hit)
        self.IntEntry.insert(0, unit.Int)
        self.ResEntry.insert(0, unit.Res)
        self.Skill1Entry.insert(0, unit.skills[0])
        self.Skill2Entry.insert(0, unit.skills[1])
        self.Skill3Entry.insert(0, unit.skills[2])
        self.Skill4Entry.insert(0, unit.skills[3])
        self.Passive1Entry.insert(0, unit.passives[0])
        self.Passive2Entry.insert(0, unit.passives[1])
        self.Passive3Entry.insert(0, unit.passives[2])
        
    def DeleteUnit(self):
        if len(self.MapGrid.selected_buttons) > 0:
            for Tile in self.MapGrid.selected_buttons:
                Tile.remove_unit()
        else:
            self.MapGrid.focused_tile.remove_unit()
        self.MapGrid.EmptySelectedButtons()

    def SaveUnit(self):
        new_unit = Unit(
            unitName=self.UnitNameEntry.get(),
            unitLevel=self.UnitLevelEntry.get(),
            classID=self.ClassIDEntry.get(),
            unitID=self.UnitIDEntry.get(),
            personality=self.PersonalityEntry.get(),
            deathEvent=self.DeathEventEntry.get(),
            maxHP=self.maxHPEntry.get(),
            maxSP=self.maxSPEntry.get(),
            Atk=self.AtkEntry.get(),
            Def=self.DefEntry.get(),
            Spd=self.SpdEntry.get(),
            Hit=self.HitEntry.get(),
            Int=self.IntEntry.get(),
            Res=self.ResEntry.get(),
            skills=[
                self.Skill1Entry.get(),
                self.Skill2Entry.get(),
                self.Skill3Entry.get(),
                self.Skill4Entry.get()
            ],
            passives=[
                self.Passive1Entry.get(),
                self.Passive2Entry.get(),
                self.Passive3Entry.get()
            ]
        )
        # ^ brainless mode here
        if len(self.MapGrid.selected_buttons) > 0:
            for Tile in self.MapGrid.selected_buttons:
                Tile.set_unit(new_unit)
        else:
            self.MapGrid.focused_tile.set_unit(new_unit)
        self.MapGrid.EmptySelectedButtons()
class ConfigurationFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.MapGrid = None
        self.Tile = None
        self.Tiles = []
        self.DP = tk.BooleanVar()
        self.AT = tk.BooleanVar()

        self.grid(row=0,column=0)
        
        self.HeightLabelFrame = tk.LabelFrame(self, text="Height")
        self.HeightLabelFrame.grid(row=0, column=0, sticky='w')
        self.HeightText = tk.Label(self.HeightLabelFrame, text="Height: ")
        self.HeightText.grid(row=0, column=0)
        self.HeightEntry = tk.Entry(self.HeightLabelFrame, width=20, validate='all', validatecommand=(self.register(lambda e: True if str.isdigit or "" else False), '%P'))
        self.HeightEntry.insert(0, "")
        self.HeightEntry.grid(row=0, column=1)
        self.HeightSaveButton = tk.Button(self.HeightLabelFrame, text="Save Only Height Configs",
                                    command=self.SaveHeightConfigs)
        self.HeightSaveButton.grid(row=3, column=1, sticky="se", pady=5, padx=5)
        
        self.DeployPositionLabelFrame = tk.LabelFrame(self, text="Deploy Position")
        self.DeployPositionLabelFrame.grid(row=1, column=0, sticky='w')
        self.DeployPositionCheckButton = tk.Checkbutton(self.DeployPositionLabelFrame, text="Flag", variable=self.DP,
                                                        onvalue=True, offvalue=False)
        self.DeployPositionCheckButton.grid(row=0,column=0, sticky='w')
        self.DeploySaveButton = tk.Button(self.DeployPositionLabelFrame, text="Save Only Deploy Configs",
                                    command=self.SaveDeployConfigs)
        self.DeploySaveButton.grid(row=3, column=1, sticky="se", pady=5, padx=5)

        self.ActionTileLabelFrame = tk.LabelFrame(self, text="Action Position")
        self.ActionTileLabelFrame.grid(row=2, column=0, sticky='w')
        self.ActionTileCheckBox = tk.Checkbutton(self.ActionTileLabelFrame, text="Flag", variable=self.AT,
                                                 onvalue=True, offvalue=False)
        self.ActionTileCheckBox.grid(row=0, column=0, sticky='w')
        self.TileNameText = tk.Label(self.ActionTileLabelFrame, text="Tile Name: ")
        self.TileNameText.grid(row=1, column=0)
        self.TileNameEntry = tk.Entry(self.ActionTileLabelFrame, width=20)
        self.TileNameEntry.insert(0, "")
        self.TileNameEntry.grid(row=1, column=1)
        self.EventIDText = tk.Label(self.ActionTileLabelFrame, text="Event ID: ")
        self.EventIDText.grid(row=2, column=0)
        self.EventIDEntry = tk.Entry(self.ActionTileLabelFrame, width=20)
        self.EventIDEntry.insert(0, "")
        self.EventIDEntry.grid(row=2, column=1)
        self.ActionSaveButton = tk.Button(self.ActionTileLabelFrame, text="Save Only Action Configs", command=self.SaveActionConfigs)
        self.ActionSaveButton.grid(row=3, column=1, sticky="se", pady=5, padx=5)

        self.SaveButton = tk.Button(self, text="Save All Configs", command=self.SaveAllConfigs)
        self.SaveButton.grid(row=3,column=0, sticky="s", pady=20, padx=5)

        self.EventIDEntry.bind("<Tab>", lambda e: self.TabControl(e))

    def AddMapGrid(self, MapGrid):
        self.MapGrid = MapGrid
    def TabControl(self, e):
        self.HeightEntry.focus()

    def LoadTileConfigs(self, e):
        self.HeightEntry.delete(0, 'end')
        self.HeightEntry.insert(0, self.MapGrid.focused_tile.tile.tile_height)
        self.DP.set(self.MapGrid.focused_tile.tile.is_deploy_position)
        self.AT.set(self.MapGrid.focused_tile.tile.is_action_tile)
        self.TileNameEntry.delete(0, 'end')
        self.TileNameEntry.insert(0, self.MapGrid.focused_tile.tile.tile_name)
        self.EventIDEntry.delete(0, 'end')
        self.EventIDEntry.insert(0, self.MapGrid.focused_tile.tile.event_id)

    def SaveActionConfigs(self):
        if len(self.MapGrid.selected_buttons) > 0:
            for Tile in self.MapGrid.selected_buttons:
                Tile.set_action_tile(self.AT.get())
                Tile.set_tile_name(self.TileNameEntry.get())
                Tile.set_event_id(self.EventIDEntry.get())
        else:
            self.MapGrid.focused_tile.set_action_tile(self.AT.get())
            self.MapGrid.focused_tile.set_tile_name(self.TileNameEntry.get())
            self.MapGrid.focused_tile.set_event_id(self.EventIDEntry.get())
        self.MapGrid.EmptySelectedButtons()
    def SaveDeployConfigs(self):
        if len(self.MapGrid.selected_buttons) > 0:
            for Tile in self.MapGrid.selected_buttons:
                Tile.set_deploy_position(self.DP.get())
        else:
            self.MapGrid.focused_tile.set_deploy_position(self.DP.get())
        self.MapGrid.EmptySelectedButtons()
    def SaveHeightConfigs(self):
        if len(self.MapGrid.selected_buttons) > 0:
            for Tile in self.MapGrid.selected_buttons:
                Tile.set_height(self.HeightEntry.get())
        else:
            self.MapGrid.focused_tile.set_height(self.HeightEntry.get())
        self.MapGrid.EmptySelectedButtons()

    def SaveAllConfigs(self):
        if len(self.MapGrid.selected_buttons) > 0:
            for Tile in self.MapGrid.selected_buttons:
                Tile.set_height(self.HeightEntry.get())
                Tile.set_deploy_position(self.DP.get())
                Tile.set_action_tile(self.AT.get())
                Tile.set_tile_name(self.TileNameEntry.get())
                Tile.set_event_id(self.EventIDEntry.get())
        else:
            self.MapGrid.focused_tile.set_height(self.HeightEntry.get())
            self.MapGrid.focused_tile.set_deploy_position(self.DP.get())
            self.MapGrid.focused_tile.set_action_tile(self.AT.get())
            self.MapGrid.focused_tile.set_tile_name(self.TileNameEntry.get())
            self.MapGrid.focused_tile.set_event_id(self.EventIDEntry.get())
        self.MapGrid.EmptySelectedButtons()

class Tile():
    def __init__(self, pos, has_unit=False, unit=Unit(), tile_height=1, is_deploy_position=False, is_action_tile=False, tile_name="", event_id=""):
        self.has_unit = has_unit
        self.unit = unit
        self.tile_height = tile_height
        self.tile_position = pos
        self.is_deploy_position = is_deploy_position
        self.is_action_tile = is_action_tile
        self.tile_name = tile_name
        self.event_id = event_id

class TileButton(tk.Button):
    def __init__(self, container, ConfigurationFrame, tile, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.container = container
        self.default_bg = self.cget('bg')
        self.configs = ConfigurationFrame
        self.tile = tile

    def reload_tile(self):
        self.configure(text=str(self.tile.tile_height))
        if self.tile.has_unit:
            self.configure(bg="Blue")
        elif self.tile.is_deploy_position:
            self.configure(bg="#00FFFF")
        elif self.tile.is_action_tile:
            self.configure(bg="#FFFF00")
        else:
            self.configure(bg=self.default_bg)

    def set_tile(self, tile):
        self.tile = tile
        self.reload_tile()

    def remove_unit(self):
        self.tile.unit = Unit()
        self.tile.has_unit = False
        self.reload_tile()
    def set_unit(self, new_unit):
        self.tile.unit = new_unit
        self.tile.has_unit = True
        self.reload_tile()

    def set_height(self, new_height):
        self.tile.tile_height = new_height
        self.reload_tile()

    def set_deploy_position(self, bool):
        self.tile.is_deploy_position = bool
        self.reload_tile()

    def set_action_tile(self, bool):
        self.tile.is_action_tile = bool
        self.reload_tile()

    def set_tile_name(self, new_tile_name):
        self.tile.tile_name = new_tile_name

    def set_event_id(self, new_event_id):
        self.tile.event_id = new_event_id

    def PickleLoad(self, file):
        self.set_tile(pickle.load(file))
    def PickleSave(self, file):
        pickle.dump(self.tile, file)

class ScrollableFrame(ttk.LabelFrame):
    def __init__(self, canvas_width, canvas_height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(text="Map Grid", padding=5)

        self.canvas = tk.Canvas(self, width=canvas_width, height=canvas_height, highlightthickness=2, highlightbackground="Black")
        self.v_scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.h_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.scrollable_frame = ttk.Frame(self.canvas, name="scrollframe")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="center")

        self.canvas.configure(yscrollcommand=self.v_scrollbar.set)
        self.canvas.configure(xscrollcommand=self.h_scrollbar.set)
        self.canvas.configure(bg='blue')

        self.canvas.grid(row=0, column=0, pady=40)
        self.v_scrollbar.grid(row=0, column=1, sticky='ns')
        self.h_scrollbar.grid(row=1, column=0, sticky='we')

    def zoom_in(self, event):
        print("zoom in")
        self.canvas.scale("all", event.x, event.y, 1.2, 1.2)  # Zoom in by 20%

    def zoom_out(self, event):
        print("zoom out")
        self.canvas.scale("all", event.x, event.y, 0.8, 0.8)  # Zoom out by 20%


class MapGrid(ttk.Frame):
    def __init__(self, container, width, height, canvas_width, canvas_height, ConfigurationFrame, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.container = container
        self.ConfigurationFrame = ConfigurationFrame
        self.UnitFrame = UnitFrame
        self.width = width
        self.height = height
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.focus = [0,0]
        self.focused_tile = None
        self.focus_padding = 6
        self.is_selecting = False
        self.selection_square = [None, None]
        self.selected_buttons = set()
        self.ButtonGrid = [[]]

        #Initialize Widgets
        self.frame = ScrollableFrame(canvas_width, canvas_height)
        self.frame.grid(row=0,column=0, sticky='s')

        self.mapsizeframe = tk.Frame(self.frame)
        self.mapsizeframe.grid(row=0, column=0, sticky='nw')

        self.HeightText = tk.Label(self.mapsizeframe, text="Height:")
        self.HeightEntry = tk.Entry(self.mapsizeframe, width=20)
        self.HeightEntry.insert(0, "20")
        self.HeightText.grid(row=0, column=0)
        self.HeightEntry.grid(row=0, column=1)

        self.WidthText = tk.Label(self.mapsizeframe, text="Width:")
        self.WidthEntry = tk.Entry(self.mapsizeframe, width=20)
        self.WidthEntry.insert(0, "20")
        self.WidthText.grid(row=0, column=3)
        self.WidthEntry.grid(row=0, column=4)

        self.ChangeGridButton = tk.Button(self.mapsizeframe, text="Change Size", command=self.RebuildMap)
        self.ChangeGridButton.grid(row=0, column=5)

        self.BottomFrame = tk.Frame(self.frame)
        self.BottomFrame.grid(row=0,column=0, sticky='sw')
        self.ClearSelectionButton = tk.Button(self.BottomFrame, text="Clear Selection", command=self.EmptySelectedButtons)
        self.ClearSelectionButton.grid(row=0, column=0)
        self.FocusText = tk.Label(self.BottomFrame, text="Focus:"+str(self.focus))
        self.FocusText.grid(row=0,column=1,padx=5)
        self.SelectionText = tk.Label(self.BottomFrame, text="Selection:"+str(self.selection_square))
        self.SelectionText.grid(row=0,column=2,padx=5)
        self.SelectedCountText = tk.Label(self.BottomFrame, text="Selected Count:" + str(len(self.selected_buttons)))
        self.SelectedCountText.grid(row=0,column=3,padx=5)

        self.default_bg = self.ClearSelectionButton.cget('bg')

        self.container.bind("<Escape>", lambda e: self.EmptySelectedButtons(e))


        # Initialize Buttons
    def InitializeButtons(self, height, width):
        self.ButtonGrid = [[None for x in range(width)] for y in range(height)]
        for y in range(height):
            for x in range(width):
                self.ButtonGrid[y][x] = TileButton(self.frame.scrollable_frame, self.ConfigurationFrame, Tile([x, y]), height=2, width=4, name="{}:{}".format(x+1, y+1), text="1")
                self.ButtonGrid[y][x].grid(row=y, column=x)
                self.ButtonGrid[y][x].bind("<Up>", lambda e: self.ArrowKeyFocusHandler(e))
                self.ButtonGrid[y][x].bind("<Down>", lambda e: self.ArrowKeyFocusHandler(e))
                self.ButtonGrid[y][x].bind("<Left>", lambda e: self.ArrowKeyFocusHandler(e))
                self.ButtonGrid[y][x].bind("<Right>", lambda e: self.ArrowKeyFocusHandler(e))
                self.ButtonGrid[y][x].bind("<Shift-space>", lambda e: self.RegionSelectionHandler(e))
                self.ButtonGrid[y][x].bind("<space>", lambda e: self.SelectionHandler(e))
                self.ButtonGrid[y][x].bind("<Button-1>", lambda e: self.M1FocusHandler(e))
                self.ButtonGrid[y][x].bind("<FocusIn>", lambda e: self.SetConfigurationFrame(e))

                self.ButtonGrid[y][x].bind("<Up>", lambda e: self.UnitFrame.LoadUnit(e), add="+")
                self.ButtonGrid[y][x].bind("<Down>", lambda e: self.UnitFrame.LoadUnit(e), add="+")
                self.ButtonGrid[y][x].bind("<Left>", lambda e: self.UnitFrame.LoadUnit(e), add="+")
                self.ButtonGrid[y][x].bind("<Right>", lambda e: self.UnitFrame.LoadUnit(e), add="+")
                self.ButtonGrid[y][x].bind("<Button-3>", lambda e: self.OnRightClick(e), add="+")
                self.ButtonGrid[y][x].bind("<B3-Motion>", lambda e: self.OnDrag(e), add="+")
                self.ButtonGrid[y][x].bind("<Button-1>", lambda e: self.UnitFrame.LoadUnit(e), add="+")


        #container.bind("<esc>", lambda Se: self.ClearSelection(e))
        #container.bind_all("<Button-1>", lambda e: self.M1FocusHandler(e))

    def OnRightClick(self, event):
        self.frame.canvas.scan_mark(event.x, event.y)

    def OnDrag(self, event):
        self.frame.canvas.scan_dragto(event.x, event.y, gain=1)

    def PickleLoad(self, file):
        if self.ButtonGrid != [[]]:
            for y in range(self.height):
                for x in range(self.width):
                    self.ButtonGrid[y][x].destroy()
        self.ButtonGrid = [[]]
        self.width = pickle.load(file)
        self.height = pickle.load(file)
        self.WidthEntry.delete(0, "end")
        self.HeightEntry.delete(0, "end")
        self.WidthEntry.insert(0, str(self.width))
        self.HeightEntry.insert(0, str(self.height))
        self.RebuildMap()
        for y in range(self.height):
            for x in range(self.width):
                self.ButtonGrid[y][x].PickleLoad(file)
    def PickleSave(self, file):
        pickle.dump(self.width, file)
        pickle.dump(self.height, file)
        for y in range(self.height):
            for x in range(self.width):
                self.ButtonGrid[y][x].PickleSave(file)

    def SetUnitFrame(self, new_unitFrame):
        self.UnitFrame = new_unitFrame

    def SetConfigurationFrame(self, event):
        self.ConfigurationFrame.LoadTileConfigs(event.widget.tile)

    def RebuildMap(self):
        new_width = self.WidthEntry.get()
        new_height = self.HeightEntry.get()
        if new_height.isdigit() and new_width.isdigit():
            new_width = int(new_width)
            new_height = int(new_height)
        else:
            return
        if not (new_width > 0 or new_height > 0):
            return

        if self.ButtonGrid != [[]]:
            for y in range(self.height):
                for x in range(self.width):
                    self.ButtonGrid[y][x].destroy()

        self.InitializeButtons(new_height, new_width)
        self.EmptySelectedButtons()
        self.height = new_height
        self.width = new_width
        self.focus = [0, 0]

    def ArrowKeyFocusHandler(self, e):
            match e.keysym:
                case "Up":
                    self.focus[1] = (self.focus[1] - 1) % self.height
                    self.frame.canvas.yview_moveto((self.focus[1]-self.focus_padding)/self.height)
                case "Down":
                    self.focus[1] = (self.focus[1] + 1) % self.height
                    self.frame.canvas.yview_moveto((self.focus[1]-self.focus_padding)/self.height)
                case "Left":
                    self.focus[0] = (self.focus[0] - 1) % self.width
                    self.frame.canvas.xview_moveto((self.focus[0]-self.focus_padding)/self.width)
                case "Right":
                    self.focus[0] = (self.focus[0] + 1) % self.width
                    self.frame.canvas.xview_moveto((self.focus[0] - self.focus_padding) / self.width)
            self.ButtonGrid[self.focus[1]][self.focus[0]].focus_set()
            self.focused_tile = self.ButtonGrid[self.focus[1]][self.focus[0]]
            self.FocusText.configure(text="Focus:"+str(self.focus))

    def M1FocusHandler(self, event):
            event.widget.focus_set()
            self.focused_tile = event.widget
            self.focus = event.widget.tile.tile_position
            self.FocusText.configure(text="Focus:" + str(self.focus))
            # worst code ever written

    def AddRegionToList(self):
        A = self.selection_square[0]
        B = self.selection_square[1]
        if A[0] >= B[0] and A[1] >= B[1]:
            B[0], A[0] = A[0], B[0]
            B[1], A[1] = A[1], B[1]
        elif A[1] <= B[1] and A[0] >= B[0]:
            B[0], A[0] = A[0], B[0]
        elif A[1] >= B[1] and A[0] <= B[0]:
            B[1], A[1] = A[1], B[1]
        else:
            pass

        #IF selected tiles are the same => add single tile to list
        if self.selection_square[0] == self.selection_square[1]:
            self.ButtonGrid[self.focus[0]][self.focus[1]].configure(bg="green")
            self.selected_buttons.add(self.ButtonGrid[self.focus[0]][self.focus[1]])
        #IF selected tiles have matching X coordinates => Iterate through the y component
        elif self.selection_square[0][0] == self.selection_square[1][0]:
            for y in range(self.selection_square[0][1], self.selection_square[1][1]+1, -1 if self.selection_square[0][1] > self.selection_square[1][1] else 1):
                self.ButtonGrid[y][self.selection_square[0][0]].configure(bg="green")
                self.selected_buttons.add(self.ButtonGrid[y][self.selection_square[0][0]])
        #IF selected tiles have matching Y coordinates => Iterate through the x component
        elif self.selection_square[0][1] == self.selection_square[1][1]:
            for x in range(self.selection_square[0][0], self.selection_square[1][0]+1, -1 if self.selection_square[0][0] > self.selection_square[1][0] else 1):
                self.ButtonGrid[self.selection_square[0][1]][x].configure(bg="green")
                self.selected_buttons.add(self.ButtonGrid[self.selection_square[0][1]][x])
        #ELSE Iterate through both x and y components
        else:
            for x in range(self.selection_square[0][0], self.selection_square[1][0]+1, -1 if self.selection_square[0][0] > self.selection_square[1][0] else 1):
                for y in range(self.selection_square[0][1], self.selection_square[1][1]+1, -1 if self.selection_square[0][1] > self.selection_square[1][1] else 1):
                    self.ButtonGrid[y][x].configure(bg="green")
                    self.selected_buttons.add(self.ButtonGrid[y][x])

    def SelectionHandler(self, e):
        if self.ButtonGrid[self.focus[1]][self.focus[0]] in self.selected_buttons:
            self.selected_buttons.remove(self.ButtonGrid[self.focus[1]][self.focus[0]])
            self.ButtonGrid[self.focus[1]][self.focus[0]].configure(bg=self.default_bg)
        else:
            self.selected_buttons.add(self.ButtonGrid[self.focus[1]][self.focus[0]])
            self.ButtonGrid[self.focus[1]][self.focus[0]].configure(bg="green")
        self.SelectedCountText.configure(text="Selected Count:"+str(len(self.selected_buttons)))

    def RegionSelectionHandler(self, e):
        if self.is_selecting:
            self.selection_square[1] = self.focus.copy()
            self.AddRegionToList()
            self.ClearSelection()
            self.SelectedCountText.configure(text="Selected Count:" + str(len(self.selected_buttons)))
        else:
            self.selection_square[0] = self.focus.copy()
            self.is_selecting=True
        self.SelectionText.configure(text="Selection:" + str(self.selection_square))

    def ClearSelection(self):
        self.selection_square = [None, None]
        self.is_selecting=False
        self.SelectionText.configure(text="Selection:" + str(self.selection_square))

    def EmptySelectedButtons(self, e=None):
        for button in self.selected_buttons:
            button.reload_tile()
        self.selected_buttons = set()
        self.ClearSelection()
        self.SelectedCountText.configure(text="Selected Count:"+str(len(self.selected_buttons)))