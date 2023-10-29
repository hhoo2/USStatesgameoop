import turtle

class InputPrompt:
    def __init__(self, screen):
        """
        Initializes the InputPrompt object.

        Args:
            screen (turtle.Screen): The turtle screen on which the input prompt will be displayed.
        """
        self.screen = screen
        self.input_prompt_turtle = self.create_input_prompt_turtle()

    def clear_prompt(self):
        """
        Clears the input prompt turtle from the screen.
        """
        self.input_prompt_turtle.hideturtle()

    def get_user_input(self, title, prompt):
        """
        Displays a text input dialog to the user and returns their input.

        Args:
            title (str): The title of the input dialog.
            prompt (str): The prompt message displayed to the user.

        Returns:
            str: The user's input, converted to title case.
        """
        return self.screen.textinput(title=title, prompt=prompt).title()
