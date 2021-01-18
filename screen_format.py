build_string = ("""
ScreenManager:
    LoginScreen:
    RegistrationScreen:

<LoginScreen>:
    name: 'login'
    MDFloatLayout:
        MDLabel:
            text: "Welcome to Portal"
            pos_hint: {"center_y": .85}
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
        MDLabel:
            text: "Login"
            pos_hint: {"center_y": .70}
            font_style: "H6"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
        MDTextField:
            id: email
            hint_text: "Enter Your Email"
            pos_hint: {"center_y": .60, "center_x": .5}
            current_hint_text_color: 0, 0, 0, 1
            size_hint_x: .8
            required: True
        MDTextField:
            id: password
            hint_text: "Enter Your Password"
            pos_hint: {"center_y": .48, "center_x": .5}
            current_hint_text_color: 0, 0, 0, 1
            size_hint_x: .8
            password: True
            required: True
        MDRaisedButton:
            text: "Register"
            pos_hint: {"center_x": .5, "center_y": .2}
            size_hint_x: .3
            size_hint_y: .08
            on_release: root.manager.current = 'registration'
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
        MDRaisedButton:
            text: "Login"
            pos_hint: {"center_x": .5, "center_y": .33}
            size_hint_x: .4
            size_hint_y: .1
            on_release: app.verifyLogin(email.text, password.text)
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
<RegistrationScreen>:
    name: 'registration'
    MDFloatLayout:
        MDLabel:
            text: "Registration"
            pos_hint: {"center_y": .85}
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
        MDLabel:
            text: "Please create an account!"
            pos_hint: {"center_y": .70}
            font_style: "H6"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
        MDTextField:
            id: email
            hint_text: "Enter Your Email"
            pos_hint: {"center_y": .60, "center_x": .5}
            current_hint_text_color: 0, 0, 0, 1
            size_hint_x: .8
            required: False
            helper_text_mode: "on_error"
            helper_text: "Enter a valid email (ex: abc@def.gh)"
        MDTextField:
            id: password1
            hint_text: "Enter Your Password"
            pos_hint: {"center_y": .48, "center_x": .5}
            current_hint_text_color: 0, 0, 0, 1
            size_hint_x: .8
            max_text_length: 20
            password: True
            required: False
            helper_text_mode: "on_error"
            helper_text: "Enter a password under 20 characters"
        MDTextField:
            id: password2
            hint_text: "Re-enter Your Password"
            pos_hint: {"center_y": .36, "center_x": .5}
            current_hint_text_color: 0, 0, 0, 1
            size_hint_x: .8
            max_text_length: 20
            password: True
            required: False
            helper_text_mode: "on_error"
            helper_text: "Enter a password under 20 characters"
        MDRaisedButton:
            text: "Register"
            pos_hint: {"center_x": .5, "center_y": .2}
            size_hint_x: .4
            size_hint_y: .1
            on_release: app.doRegistration(email.text, password1.text, password2.text)
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
""")