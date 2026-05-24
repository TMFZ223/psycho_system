from back.schemas.auth_schema import AuthSchema
from back.schemas.register_schema import RegisterSchema
from test_utils.env_reader import EnvReader

class UserFactory:

    @staticmethod
    def standard_register():
        return RegisterSchema(email="student@gmail.com", password="example_password", verify_password="example_password")

    @staticmethod
    def register_with_existing_email():
        return RegisterSchema(email=EnvReader.get_env_variable_value("admin_email"), password="U{('D#(5wKSVo^A9'>`R'0Dc%", verify_password="U{('D#(5wKSVo^A9'>`R'0Dc%")

    @staticmethod
    def register_with_empty_email():
        return RegisterSchema(email="", password="U{('D#(5wKSVo^A9'>`R'0Dc%", verify_password="U{('D#(5wKSVo^A9'>`R'0Dc%")

    @staticmethod
    def register_with_none_email():
        return RegisterSchema(email=None, password="U{('D#(5wKSVo^A9'>`R'0Dc%", verify_password="U{('D#(5wKSVo^A9'>`R'0Dc%")

    @staticmethod
    def register_with_email_without_add_symbol():
        return RegisterSchema(email="etcgmail.com", password=";%-QWLX#B(H", verify_password=";%-QWLX#B(H")

    @staticmethod
    def register_with_email_without_dod_symbol():
        return RegisterSchema(email="stiv@gmailcom", password=";%-QWLX#B(H", verify_password=";%-QWLX#B(H")

    @staticmethod
    def register_with_email_without_required_symbols():
        return RegisterSchema(email="examplegmailcom", password="pomidoro", verify_password="pomidoro")

    @staticmethod
    def register_with_6_character_password():
        return RegisterSchema(email="128@gmail.com", password="tomato", verify_password="tomato")

    @staticmethod
    def register_with_7_character_password():
        return RegisterSchema(email="albukerke@cloud.com", password="testing", verify_password="testing")

    @staticmethod
    def register_with_8_character_password():
        return RegisterSchema(email="eshly@gmail.com", password="acapulka", verify_password="acapulka")

    @staticmethod
    def register_with_29_character_password():
        return RegisterSchema(email="aliceStenf@domain.co", password="X{tt^R#hcfC(qj4zgFw!VEUx[Cf<y", verify_password="X{tt^R#hcfC(qj4zgFw!VEUx[Cf<y")

    @staticmethod
    def register_with_30_character_password():
        return RegisterSchema(email="premium-bagels@testDomain.us", password="r/1n;m{No;%@PLGm@mrOQ!D_Uy:OF~", verify_password="r/1n;m{No;%@PLGm@mrOQ!D_Uy:OF~")

    @staticmethod
    def register_with_31_character_password():
        return RegisterSchema(email="visual@inbox.org", password="Bq:>mB+YUME{2s]weJ6;j?l>WRc!(&V", verify_password="Bq:>mB+YUME{2s]weJ6;j?l>WRc!(&V")

    @staticmethod
    def register_with_cyrilic_symbols_in_password():
        return  RegisterSchema(email="visual_user@domain.com", password="задание", verify_password="задание")

    @staticmethod
    def register_with_cyrilic_and_latinic_symbols_in_password():
        return RegisterSchema(email="flour@rambler.su", password="passwordпароль", verify_password="passwordпароль")

    @staticmethod
    def register_with_special_and_space_symbols_in_password():
        return RegisterSchema(email="secret@exampleDomain.com", password="!`~_;.@#  ^", verify_password="!`~_;.@#  ^")

    @staticmethod
    def register_with_empty_password():
        return RegisterSchema(email="email@electro.su", password="", verify_password="U{('D#(5wKSVo>")

    @staticmethod
    def register_with_none_password():
        return RegisterSchema(email="email@electro.su", password=None, verify_password="U{('D#(5wKSVo>")

    @staticmethod
    def register_with_differents_password_verify_password():
        return RegisterSchema(email="email@electrodomain.su", password="U{('D#(5wKSVo>", verify_password="U{('D#(5wKSVo")

    @staticmethod
    def register_with_empty_verify_password():
        return RegisterSchema(email="email@rambler.co", password="U{('D#(5wKSVo>", verify_password="")

    @staticmethod
    def register_with_none_verify_password():
        return RegisterSchema(email="boy@mail.ru", password="U{('D#(5wKSVo>", verify_password=None)

    @staticmethod
    def login_with_admin():
        return AuthSchema(email=EnvReader.get_env_variable_value("admin_email"), password=EnvReader.get_env_variable_value("admin_password"))