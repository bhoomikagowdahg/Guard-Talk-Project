import flet as ft

class Message:
    def __init__(self, user: str, text: str, message_type: str,starred=False):
        self.user = user
        self.text = text
        self.message_type = message_type
        self.starred = starred  # New attribute to track if a message is starred
    

class ChatMessage(ft.Row):
    def __init__(self, message: Message, toggle_star, is_current_user: bool):
        super().__init__()
        self.message = message
        self.toggle_star = toggle_star

        # Adjust alignment based on the sender
        self.alignment = (
            ft.MainAxisAlignment.END if is_current_user else ft.MainAxisAlignment.START
        )

        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user)),
                color=ft.colors.WHITE,
                bgcolor=self.get_avatar_color(message.user),
            ),
            ft.Column(
                [
                    ft.Text(message.user, weight="bold"),
                    ft.Text(message.text, selectable=True),
                ],
                tight=True,
                spacing=5,
            ),
            ft.IconButton(
                icon=ft.icons.STAR if message.starred else ft.icons.STAR_BORDER,
                tooltip="Star message",
                on_click=self.on_star_click,
            ),
            
        ]

        # Reorder controls for current user messages to appear on the right
        if is_current_user:
            self.controls = self.controls[::-1]


    def on_star_click(self, e):
        self.message.starred = not self.message.starred
        self.toggle_star(self.message)
        self.controls[2].icon=(ft.icons.STAR if self.message.starred else ft.icons.STAR_BORDER)
        self.update()

    def get_initials(self, user: str):
        return user[:1].capitalize()

    def get_avatar_color(self, user: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user) % len(colors_lookup)]
