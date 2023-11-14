import PySimpleGUI as sg

class Window:
    def __init__ (self, ASSETS_PATH = r"./assets"):
        self.ASSETS_PATH = ASSETS_PATH
        self.windowSizeX = 610
        self.windowSizeY = 480
        self.font = ("Calibri", 12)
        self.fontB = ("Calibri", 12, 'bold')
        self.colors = ("", "#FFFFFF")
        self.button1 = self.ASSETS_PATH +"/button1.png"
        self.button2 = self.ASSETS_PATH +"/button2.png"

    def create_window(self,content_layout, windowtitlemsg):

        #sg.theme("LightGrey1")  # Change the theme to your preferred one
        sg.set_options(font=self.font)


        layout = [        
                [sg.Image(filename= self.ASSETS_PATH +"/image_3.png",pad=(30))],
                [content_layout],
                [sg.Image(filename= self.ASSETS_PATH +"/image_2.png",pad=(0,0)),sg.Push(),sg.VPush(),sg.Image(filename= self.ASSETS_PATH +"/image_1_s.png",pad=(0,0))]
               ]


        windowname = sg.Window(windowtitlemsg, layout, size=(self.windowSizeX,self.windowSizeY), resizable=True, finalize=True)
        return windowname

    def update_top_message(self,window, new_message):
        window['-TOPMESSAGE-'].update(new_message)
        window.refresh()
        return window


    def makeWindow0(self, connected):

            if connected:
                topMessage = 'The Conductor is connected on ' + self.dataStream.ssid + ' at ' + self.dataStream.host
                connectVis = True   #Use to set visibility of an item when The Conductor is connected
                disconnectVis = False  #Use to unset visibility of an item when The Conductor is not connected
                self.SSIDList = self.dataStream.getNetworks()  #Get the network list from the air so user can reconnect

            else:
                topMessage = 'Start up The Conductor and connect your PC to the SSID displayed on the screen.\n\nThen enter IP address on the screen and click "Connect."'
                connectVis = False
                disconnectVis = True

            windowtitlemsg = 'THE CONDUCTOR: Step 0'
            content_layout = ([sg.Push(),sg.Text(f'Connect to The Conductor.',key='-OUTPUT-',font = ("Calibri", 16, "bold",), pad=((0,0),(0,25))),sg.Push()], 
                    [sg.pin(sg.Column([[sg.Text(topMessage, pad=(50,4), key='-TOPMESSAGE-')]]))],
                    # [sg.pin(sg.Column([[sg.Text('Then enter IP address on the screen and click "Connect."', pad=(50,4), key='-TOPMESSAGE01-')]]))],
                    [sg.pin(sg.Column([[sg.Text(f"To use this network click 'Continue.' To connect to another network enter the network info below and click 'Reconnect'. Click 'Don't Connect' to continue without connecting", key='-TOPMESSAGE01-', size=(100,2), visible=connectVis)]]), shrink=True)],
                    [sg.pin(sg.Column([[sg.Input('192.168.XX.XXX', key="-IPIN-", visible=disconnectVis, pad=((5),(0,5)), do_not_clear=True)]], pad=(50,0)))],
                    [sg.Column([[sg.Btn('Connect',button_color=self.colors, border_width=0, image_source=self.button1, font = self.fontB, key='-APCNTEBTN-', visible=disconnectVis,pad=((70,70 ),(5,0)))]]),
                     sg.Column([[sg.Btn("Don't Connect",button_color=self.colors, border_width=0, image_source=self.button1,font = self.fontB, key='-NOCNTBTN-', visible=disconnectVis )]],pad=((0,0),(5,0)))],
                    [sg.pin(sg.Column([[sg.Input('192.168.XX.XXX', key="-IPNEW-", visible=False)]]), shrink=True)],
                    [sg.pin(sg.Column([[sg.Btn('Connect', key='-STNCNTEBTN-', visible=False)]]), shrink=False)],
                    #[sg.pin(sg.Column([], pad=(50,0)), shrink=True)],
                    #[sg.pin(sg.Column([[sg.Listbox(self.SSIDList, size=(15, 4), key="-SSIDIN-", expand_y=True, enable_events=True, visible=False)]]), shrink=False)],
                    [sg.pin(sg.Column([[sg.Input('Password', key="-PSWDIN-", visible=False,pad=(50,0))]]), shrink=False)],
                    #[sg.pin(sg.Column([[sg.Btn('Connect', key='-APCNTEBTN-', visible=True)]], pad=(50,0)), shrink=False)],
                    [sg.pin(sg.Column([[sg.Btn('Continue', key='-CONTBTN-', visible=False)]], pad=(50,0)), shrink=False)],
                    [sg.pin(sg.Column([[sg.Btn('Reconnect', key='-RECNTBTN-', visible=False)]], pad=(50,0)), shrink=True)],
                    [sg.pin(sg.Column([[sg.Text('', visible=True, key='-MESSAGE-')]], pad=(0,0)), shrink=False)])
        
            window0=self.create_window(content_layout,windowtitlemsg)
            self.update_top_message(window0, topMessage)
            return window0
        
    def makeWindow1(self, modelMessage):
    #Window one welcome, load / create model
        windowtitlemsg = 'THE CONDUCTOR: Step 1'
        content_layout = ([sg.Push(),sg.Text('The Conductor: Window 1',key='-OUTPUT-',font = ("Calibri", 16, "bold",), pad=((0,0),(0,25))),sg.Push()],
                [sg.pin(sg.Column([[sg.Text('Upload an existing neural network model or create a new one.', key='-OUTPUT-')]], pad=(50,0)))], 
                [sg.pin(sg.Column([[sg.Text(modelMessage, key='-MODELMESSAGE-'), sg.Btn('Ok',button_color=self.colors, border_width=0, image_source=self.button2, font = self.fontB, key='-MODELMESAGEBTN-')]], pad=(50,0)))],
                [sg.pin(sg.Column([[sg.Text('Upload a model', key='-UPLOADMODEL-'), sg.Input(), sg.FileBrowse(), sg.Btn('Upload',button_color=self.colors, border_width=0, image_source=self.button1, font = self.fontB, key='-UPLOADMODELBTN-')]], pad=(50,0)))],
                [sg.pin(sg.Column([[sg.Text('Create a New Model', key='-OUTPUT-'), sg.Btn('Ok',button_color=self.colors, border_width=0, image_source=self.button2, font = self.fontB, key='-CREATE-')]], pad=(50,0)))],
                [sg.pin(sg.Column([[sg.Text('', visible=True, key='-MESSAGE-')]], pad=(50,0)), shrink=False)],
                #[sg.pin(sg.Column([[sg.Btn('-MODELOK-', visible=False)]], pad=(0,0)), shrink=False)]
                        #sg.Text('Not a valid model file. Please try again.', size=(2,1), key='-invalidModel-', visible=True, pad=(0,0)), sg.Text(size=(2,1))]
        )

        window1=self.create_window(content_layout,windowtitlemsg)
        return window1

    def makeWindow2_1(self):
        #Window3 Training or prediction select
        windowtitlemsg = 'THE CONDUCTOR: Step 2.1'
        content_layout = [[sg.Text('The Conductor: Window 2.1'), sg.Text(size=(2,1), key='-OUTPUT-')],
                    [sg.pin(sg.Column([[sg.Text('Train Model'), sg.Text(size=(2,1), key='-TRAIN-'), sg.Btn('Train', key='-TRAINBTN-')]]))],
                    [sg.pin(sg.Column([[sg.Text('Predict gestures'), sg.Text(size=(2,1), key='-PREDICT-'), sg.Btn('Predict', key='-PREDICTBTN-')]]))],
                    [sg.pin(sg.Column([[sg.Text('', visible=True, key='-WORDS-'), sg.Text(size=(2,1))]], pad=(0,0)), shrink=False)],
        ]
        window2_1=self.create_window(content_layout,windowtitlemsg)
        return window2_1
        return sg.Window('THE CONDUCTOR: Step 2.1', layout, layout, size=(self.windowSizeX,self.windowSizeY), finalize=True)


    def makeWindow3(self):
        #Window3 Training 
        windowtitlemsg = 'THE CONDUCTOR: Step 3'
        content_layout = [[sg.Text('The Conductor: Window 3'), sg.Text(size=(2,1), key='-OUTPUT-')],
                    [sg.pin(sg.Column([[sg.Text("Hit the 'GO!' Btn to begin training", visible=True, key='-GESTURE-'), sg.Text(size=(2,1))]], pad=(0,0)), shrink=False)],
                    [sg.pin(sg.Column([[sg.Text('', visible=True, key='-CountDown-'), sg.Text(size=(2,1))]], pad=(0,0)), shrink=False)],
                    [sg.Btn('GO!')]
        ]
        window3=self.create_window(content_layout,windowtitlemsg)
        return window3
        return sg.Window('THE CONDUCTOR: Step 3', layout, layout, size=(self.windowSizeX,self.windowSizeY), finalize=True)


    def makeWindow3_1(self):
        #Window3_1 Prediction 
        windowtitlemsg = 'THE CONDUCTOR: Step 3_1'
        content_layout = [[sg.Text('The Conductor: Window 3_1'), sg.Text(size=(2,1), key='-OUTPUT-')],
                    [sg.pin(sg.Column([[sg.Text("Hit the 'GO!' Btn to begin prediction", visible=True, key='-GESTURE-'), sg.Text(size=(2,1))]], pad=(0,0)), shrink=False)],
                    [sg.pin(sg.Column([[sg.Text('', visible=True, key='-CountDown-'), sg.Text(size=(2,1))]], pad=(0,0)), shrink=False)],
                    [sg.pin(sg.Column([[sg.Text(''), sg.Text(size=(2,1), key='-GO-'), sg.Btn('GO!', key='-GOBTN-', visible=True)]]), shrink=False)],
                    [sg.pin(sg.Column([[sg.Text(''), sg.Text(size=(2,1), key='-STOP-'), sg.Btn('Stop', key='-STOPBTN-', visible=False)]]), shrink=False)]
        ]
        window3_1=self.create_window(content_layout,windowtitlemsg)
        return window3_1
        return sg.Window('THE CONDUCTOR: Step 3_1', layout, layout, size=(self.windowSizeX,self.windowSizeY), finalize=True)
