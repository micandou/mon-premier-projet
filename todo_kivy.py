from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class TodoItem(BoxLayout):
    def __init__(self, task_text, **kwargs):
        super().__init__(orientation='horizontal', size_hint_y=None, height=40, **kwargs)
        self.task_text = task_text
        self.label = Label(text=task_text, size_hint_x=0.8)
        self.add_widget(self.label)
        self.button = Button(text='Done', size_hint_x=0.2)
        self.button.bind(on_press=self.mark_done)
        self.add_widget(self.button)

    def mark_done(self, instance):
        # On "barre" le texte pour marquer la tâche comme faite.
        self.label.text = "[s]{}[/s]".format(self.task_text)
        self.label.markup = True

class TodoListScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # Partie ajout de tâche
        add_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.task_input = TextInput(hint_text="Enter a new task", multiline=False)
        add_layout.add_widget(self.task_input)
        add_button = Button(text="Add", size_hint_x=0.3)
        add_button.bind(on_press=self.add_task)
        add_layout.add_widget(add_button)
        self.add_widget(add_layout)
        
        # Liste déroulante pour afficher les tâches
        self.task_list_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.task_list_layout.bind(minimum_height=self.task_list_layout.setter('height'))
        scroll_view = ScrollView()
        scroll_view.add_widget(self.task_list_layout)
        self.add_widget(scroll_view)
    
    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:
            todo_item = TodoItem(task_text)
            self.task_list_layout.add_widget(todo_item)
            self.task_input.text = ""

class TodoListApp(App):
    def build(self):
        return TodoListScreen()

if __name__ == '__main__':
    TodoListApp().run()
