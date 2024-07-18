from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from models.database import init_db, add_user, get_users

Builder.load_file('ui/main.xml')

class MyApp(App):
    def build(self):
        self.title = 'My App'
        self.root = BoxLayout(orientation='vertical')
        
        button = Button(text='Click Me')
        label = Label(text='Hello, World!')
        
        button.bind(on_press=lambda x: self.on_button_click(label))
        
        self.root.add_widget(button)
        self.root.add_widget(label)
        
        init_db()
        
        return self.root

    def on_button_click(self, label):
        add_user('New User')
        users = get_users()
        label.text = f'Users in DB: {len(users)}'

if __name__ == '__main__':
    MyApp().run()
