from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
 
# kv code within the Python file
Builder.load_string("""
<ScreenOne>:
    
    canvas:
        Color:
            rgb: 0,0,0.3
        Rectangle:
            pos: self.pos
            size: self.size

     
    Label:
        text: "Starters"
        text_size: self.size
        halign: "center"
        valign: "top"
        font_size: 25
        color: [1,0,1,1]
        
    GridLayout:
        rows:3
        cols:4
        spacing: 30
        padding: 30
         
        
        Button:
            text: "Aloo Paratha"
            background_color: (0,0,0,0.1)
            Image:
                source: 'Ap.jpg'
                y: self.parent.y + self.parent.height - 180
                x: self.parent.x-21
                size: 200, 180
                allow_stretch: False
                keep_ratio:  
                on_touch_down:
                    root.manager.transition.direction= 'right'
                    root.manager.transition.duration= 1
                    root.manager.current= 'screen_four'
            
        Button:
            text: "Baingan Bharta"
            
            color: [0.8,0.4,0.5,1]

            
        Button:
            text: "Pav Bhaji"
            
            color: [0.6,0.6,0.7,0.9]
            
        Button:
            text: "Chana Bhatura"
            
            color: [0.3,0.8,0.5,0.75]
            
        Button:
            text: "Daal Bati Churma"
            
            color: [0.7,0.2,0.5,0.69]
            
        Button:
            text: "Sarson ka Saag"
            
            color: [0.8,0.4,0.5,0.34]
        
        Button:
            text: "Tandoori Chicken"
            
            color: [0,0.4,0.5,0.8]
            
        Button:
            text: "Rogan Josh"
            
            color: [0.7,0,0.5,1]
            
        Button:
            text: "Hyderabadi Biryani"
            
            color: [0.67,0.76,0.42,0.94]
            
        Button:
            text: "--->"
            
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_two'
 
<ScreenTwo>:
    
    canvas:
        Color:
            rgb: 0,0,0.5
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "Desserts" 
        text_size: self.size
        halign: "center"
        valign: "top"
        font_size: 25
        color: [1,0,1,1]
    
    GridLayout:
        rows: 3
        cols: 4
        spacing: 30
        padding: 30
        Button:
            text: "Gulab Jamun"
            width:300
        Button:
            text: "Tiramisu"
            width: 300
        
        Button:
            text: "Red Celvet Cheesecake"
            width: 300
        Button:
            text: "Molten Chocolate Brownie"
            width: 300
        Button:
            text: "Treacle tart"
            width: 300
        
        Button:
            text: "Moong Dal Halwa"
            width:"300"
        Button:
            text: "Coconut Barfi"
            width:"300"
        Button:
            text: "Puran Poli"
            width:"300"
        Button:
            text: "Balushahi"
            width: 300
        
        Button:
            text: "<----"
            
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_one'


<ScreenThree>:

    canvas:
        Color:
            rgb: 0,0,0.5
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "Aloo Paratha" 
        text_size: self.size
        halign: "center"
        valign: "top"
        font_size: 25
        color: [1,0,1,1]
    

    GridLayout:
        rows: 10
        cols: 1
        spacing: 30
        padding: 30

    
        Label:
            text: "How to Make Aloo Paratha"

        Label:
            text:  "1. Make a soft dough with the specified ingredients"

        Label:
            text: "2. Divide the dough into balls, as per the required size"

        Label:
            text: "3. Chop the onions, green chillies and the coriander leaves. Then boil the potatoes; remove the skin and mash"

        Label:
            text: "4. Add the rest of the ingredients and mix well. Take each portion of the dough, flatten it on palm"

        Label:
            text: "5. Stuff the filling in the dough and roll into balls. With a rolling pin, flatten the balls into 1/2 inch thick round parathas."
            
        Label:
            text: "6. Grease a pan with a little oil and heat on a medium flame"

        Label:
            text: "7. Cook the parathas until both sides are golden and cooked through."

        Button:
            text: "---->"
            
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'screen_one'
        

<ScreenFour>:

    canvas:
        Color:
            rgb: 0,0,0.5
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "Aloo Paratha" 
        text_size: self.size
        halign: "center"
        valign: "top"
        font_size: 25
        color: [1,0,1,1]
    

    GridLayout:
        rows: 15
        cols: 1
        spacing: 30
        padding: 30

    
        Label:
            text: "Ingredients"

        Label:
            text: "250 gm whole wheat flour"

        Label:
            text: "Pinch of salt" 

        Label:
            text: "1 cup water"

        Label:
            text: "50 ml oil"

        Label:
            text: "500 gm potatoes"
            
        Label:
            text: "20 gm coriander leaves"

        Label:
            text: "20 gm ginger garlic paste"

        Label:
            text: "75 gm onions"

        Label:
            text: "5 gm green chillies"
            
        Label:
            text: "5 gm turmeric"

        Label:
            text: "5 gm Chilli powder"
            
        Label:
            text: "10 ml lime juice"
            
        Label:
            text: "Oil for frying"
            
        Button:
            text: "Click to view procedure for preparation"
            
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'screen_three'

       
        
        
       
""")
 
# Create a class for all screens in which you can include
# helpful methods specific to that screen
class ScreenOne(Screen):
    pass
 
 
class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass

class ScreenFour(Screen):
    pass
 
# The ScreenManager controls moving between screens
screen_manager = ScreenManager()
 
# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))
screen_manager.add_widget(ScreenThree(name="screen_three"))
screen_manager.add_widget(ScreenFour(name="screen_four"))

class KivyTut2App(App):
 
    def build(self):
        return screen_manager

    
        
 
sample_app = KivyTut2App()
sample_app.run()
