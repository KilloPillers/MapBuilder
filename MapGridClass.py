import tkinter as tk
from tkinter import ttk

class ConfigurationFrame(ttk.LabelFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Tile = Tile
        self.Tiles = [Tile]
        self.DP = tk.BooleanVar()
        self.AT = tk.BooleanVar()

        self.configure(text="Tile Configuration", padding=5)
        self.grid(row=0,column=1, rowspan=10)
        
        self.HeightLabelFrame = tk.LabelFrame(self, text="Height")
        self.HeightLabelFrame.grid(row=0, column=0, sticky='w')
        self.HeightText = tk.Label(self.HeightLabelFrame, text="Height: ")
        self.HeightText.grid(row=0, column=0)
        self.HeightEntry = tk.Entry(self.HeightLabelFrame, width=20, validate='all', validatecommand=(self.register(lambda e: True if str.isdigit or "" else False), '%P'))
        self.HeightEntry.insert(0, " ")
        self.HeightEntry.grid(row=0, column=1)
        
        self.DeployPositionLabelFrame = tk.LabelFrame(self, text="Deploy Position")
        self.DeployPositionLabelFrame.grid(row=1, column=0, sticky='w')
        self.DeployPositionCheckButton = tk.Checkbutton(self.DeployPositionLabelFrame, text="Flag", variable=self.DP,
                                                        onvalue=True, offvalue=False)
        self.DeployPositionCheckButton.grid(row=0,column=0, sticky='w')

        self.ActionTileLabelFrame = tk.LabelFrame(self, text="Action Position")
        self.ActionTileLabelFrame.grid(row=2, column=0, sticky='w')
        self.ActionTileCheckBox = tk.Checkbutton(self.ActionTileLabelFrame, text="Flag", variable=self.AT,
                                                 onvalue=True, offvalue=False)

        self.ActionTileCheckBox.grid(row=0, column=0, sticky='w')
        self.TileNameText = tk.Label(self.ActionTileLabelFrame, text="Tile Name: ")
        self.TileNameText.grid(row=1, column=0)
        self.TileNameEntry = tk.Entry(self.ActionTileLabelFrame, width=20)
        self.TileNameEntry.insert(0, " ")
        self.TileNameEntry.grid(row=1, column=1)
        self.EventIDText = tk.Label(self.ActionTileLabelFrame, text="Event ID: ")
        self.EventIDText.grid(row=2, column=0)
        self.EventIDEntry = tk.Entry(self.ActionTileLabelFrame, width=20)
        self.EventIDEntry.insert(0, " ")
        self.EventIDEntry.grid(row=2, column=1)

        self.SaveButton = tk.Button(self, text="Save to Tile(s)", command=self.SaveConfigs)
        self.SaveButton.grid(row=3,column=0, sticky="se")

        self.EventIDEntry.bind("<Tab>", lambda e: self.TabControl(e))

    def TabControl(self, e):
        self.HeightEntry.focus()

    def LoadTileConfigs(self, Tile):
        self.Tile = Tile
        self.HeightEntry.delete(0, 'end')
        self.HeightEntry.insert(0, self.Tile.tile_height)
        self.DP.set(self.Tile.is_deploy_position)
        self.AT.set(self.Tile.is_action_tile)
        self.TileNameEntry.delete(0, 'end')
        self.TileNameEntry.insert(0, self.Tile.tile_name)
        self.EventIDEntry.delete(0, 'end')
        self.EventIDEntry.insert(0, self.Tile.event_id)
        
    def LoadSelectionsConfigs(self, Tiles):
        self.Tiles = Tiles

    def SaveConfigs(self):
        if len(self.Tiles) > 0:
            for Tile in self.Tiles:
                Tile.set_height(self.HeightEntry.get())
                Tile.set_deploy_position(self.DP.get())
                Tile.set_action_tile(self.AT.get())
                Tile.set_tile_name(self.TileNameEntry.get())
                Tile.set_event_id(self.EventIDEntry.get())
        else:
            self.Tile.set_height(self.HeightEntry.get())
            self.Tile.set_deploy_position(self.DP.get())
            self.Tile.set_action_tile(self.AT.get())
            self.Tile.set_tile_name(self.TileNameEntry.get())
            self.Tile.set_event_id(self.EventIDEntry.get())

class Tile(tk.Button):
    def __init__(self, container, ConfigurationFrame, pos, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.container = container
        self.configs = ConfigurationFrame
        self.tile_height = 64
        self.tile_position = pos
        self.is_deploy_position = False
        self.is_action_tile = False
        self.tile_name = "None"
        self.event_id = "None"
    def set_height(self, new_height):
        self.configure(text=str(new_height))
        self.tile_height = new_height

    def set_deploy_position(self, bool):
        self.is_deploy_position = bool

    def set_action_tile(self, bool):
        self.is_action_tile = bool

    def set_tile_name(self, new_tile_name):
        self.tile_name = new_tile_name

    def set_event_id(self, new_event_id):
        self.event_id = new_event_id

class ScrollableFrame(ttk.LabelFrame):
    def __init__(self, canvas_width, canvas_height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(text="Map Grid", padding=5)

        self.canvas = tk.Canvas(self, width=canvas_width, height=canvas_height, highlightthickness=2, highlightbackground="Black")
        self.v_scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.h_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.scrollable_frame = ttk.Frame(self.canvas)

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

class MapGrid(ttk.Frame):
    def __init__(self, container, width, height, canvas_width, canvas_height, ConfigurationFrame, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.container = container
        self.ConfigurationFrame = ConfigurationFrame
        self.width = width
        self.height = height
        self.focus = [0,0]
        self.focused_tile = None
        self.focus_padding = 4
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

        # Initialize Buttons
    def InitializeButtons(self, height, width):
        self.ButtonGrid = [[None for x in range(width)] for y in range(height)]
        for y in range(height):
            for x in range(width):
                self.ButtonGrid[y][x] = Tile(self.frame.scrollable_frame, self.ConfigurationFrame, [x,y], height=2, width=2, name="{}:{}".format(x, y), text="64")
                self.ButtonGrid[y][x].grid(row=y, column=x)
                self.ButtonGrid[y][x].bind("<Up>", lambda e: self.ArrowKeyFocusHandler(e))
                self.ButtonGrid[y][x].bind("<Down>", lambda e: self.ArrowKeyFocusHandler(e))
                self.ButtonGrid[y][x].bind("<Left>", lambda e: self.ArrowKeyFocusHandler(e))
                self.ButtonGrid[y][x].bind("<Right>", lambda e: self.ArrowKeyFocusHandler(e))
                self.ButtonGrid[y][x].bind("<Shift-space>", lambda e: self.RegionSelectionHandler(e))
                self.ButtonGrid[y][x].bind("<Control-space>", lambda e: self.SelectionHandler(e))
                self.ButtonGrid[y][x].bind("<Button-1>", lambda e: self.M1FocusHandler(e))

        #container.bind("<esc>", lambda Se: self.ClearSelection(e))
        #container.bind_all("<Button-1>", lambda e: self.M1FocusHandler(e))

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
            self.focus = event.widget.tile_position
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
            self.ConfigurationFrame.LoadSelectionsConfigs(self.selected_buttons)
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

    def EmptySelectedButtons(self):
        for button in self.selected_buttons:
            button.configure(bg=self.default_bg)
        self.selected_buttons = set()
        self.ClearSelection()
        self.SelectedCountText.configure(text="Selected Count:"+str(len(self.selected_buttons)))