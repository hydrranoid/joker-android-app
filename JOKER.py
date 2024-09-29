from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from all_joker_data import draws_data

class JokerApp(App):
    def build(self):
        # Δημιουργία κύριου layout
        self.layout = BoxLayout(orientation='vertical')

        # Εισαγωγή για τους 5 αριθμούς
        self.number_inputs = []
        for i in range(5):
            label = Label(text=f"Αριθμός {i + 1} (1-45):")
            self.layout.add_widget(label)
            number_input = TextInput(multiline=False, input_filter='int')
            self.layout.add_widget(number_input)
            self.number_inputs.append(number_input)

        # Εισαγωγή για τον αριθμό Τζόκερ
        self.joker_label = Label(text="Αριθμός Τζόκερ (1-20):")
        self.layout.add_widget(self.joker_label)
        self.joker_input = TextInput(multiline=False, input_filter='int')
        self.layout.add_widget(self.joker_input)

        # Κουμπί για έλεγχο αν οι αριθμοί έχουν κερδίσει
        self.check_button = Button(text="Έλεγχος αν έχουν κερδίσει")
        self.check_button.bind(on_press=self.check_numbers)
        self.layout.add_widget(self.check_button)

        # Περιοχή εμφάνισης αποτελεσμάτων
        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)

        return self.layout

    def check_numbers(self, instance):
        try:
            # Λήψη των αριθμών από την είσοδο χρήστη και έλεγχος ορθότητας
            user_numbers = {int(input_field.text) for input_field in self.number_inputs}
            user_joker = int(self.joker_input.text)

            # Έλεγχος ότι οι αριθμοί είναι εντός των ορίων
            if len(user_numbers) != 5:
                self.result_label.text = "Πρέπει να δώσετε 5 μοναδικούς αριθμούς."
                return
            if any(num < 1 or num > 45 for num in user_numbers):
                self.result_label.text = "Οι αριθμοί πρέπει να είναι από το 1 έως το 45."
                return
            if user_joker < 1 or user_joker > 20:
                self.result_label.text = "Ο αριθμός Τζόκερ πρέπει να είναι από το 1 έως το 20."
                return

            # Έλεγχος αν οι αριθμοί έχουν ξανακερδίσει
            winning_dates = check_if_numbers_won(user_numbers, user_joker)

            if winning_dates:
                self.result_label.text = f"Κερδίσατε στις εξής ημερομηνίες: {', '.join(winning_dates)}"
            else:
                self.result_label.text = "Δεν έχουν κερδίσει ποτέ."
        except ValueError:
            self.result_label.text = "Παρακαλώ δώστε έγκυρους ακέραιους αριθμούς."

def check_if_numbers_won(numbers, joker):
    won_dates = []
    for draw in draws_data:
        try:
            # Έλεγχος για μετατροπή των τιμών σε ακέραιους αριθμούς
            draw_numbers = {int(draw['num1']), int(draw['num2']), int(draw['num3']), int(draw['num4']), int(draw['num5'])}
            draw_joker = int(draw['joker'])
        except ValueError:
            continue

        # Έλεγχος αν οι αριθμοί και ο αριθμός Τζόκερ ταυτίζονται με την κλήρωση
        if draw_numbers == numbers and draw_joker == joker:
            won_dates.append(draw['date'])

    return won_dates

if __name__ == "__main__":
    JokerApp().run()
