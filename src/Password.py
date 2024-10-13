import secrets


class Password:
    """
    パスワードを生成するためのクラス。

    parameters:
        lower_str (str): 小文字のアルファベット文字列。
        upper_str (str): 大文字のアルファベット文字列。
        number_str (str): 数字の文字列。
        flag_str (str): 記号の文字列。
    """

    lower_str = "abcdefghijklmnopqrstuvwxyz"
    upper_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_str = "0123456789"
    flag_str = r"-_/*+.,!?#$%&~|^@;:()[]\{\}"
    password_chars = ""
    password_length = 0
    result_pw = ""

    def __init__(
        self,
        # toggle_l=True,
        toggle_u=False,
        toggle_n=False,
        toggle_symbol=False,
        min_length=6,
        max_length=12,
        password_length=10,
    ):
        """
        Passwordクラスのコンストラクタ。

        parameters:
            toggle_u (bool): Trueの場合、大文字を含めます。
            toggle_n (bool): Trueの場合、数字を含めます。
            toggle_symbol (bool): Trueの場合、記号を含めます。
            min_length (int): パスワードの最小長。
            max_length (int): パスワードの最大長。
            password_length (int): 生成するパスワードの長さ。
        """
        self.toggle_u = toggle_u
        # self.toggle_l = toggle_l
        self.toggle_n = toggle_n
        self.toggle_symbol = toggle_symbol
        self.min_length = min_length
        self.max_length = max_length
        self.password_length = password_length

        self.password_chars = self.lower_str
        if toggle_u is True:
            self.password_chars += self.upper_str
        if toggle_n is True:
            self.password_chars += self.number_str
        if toggle_symbol is True:
            self.password_chars += self.flag_str

    def generate(self) -> str:
        """パスワードを生成するメソッド。

        Raises:
            ValueError: パスワード長さに対する例外。

        Returns:
            str: 生成されたパスワード。
        """
        if not (self.min_length <= self.password_length <= self.max_length):
            raise ValueError(
                f"パスワードの長さは{self.min_length}から{self.max_length}の間で指定してください。"
            )

        p = [secrets.choice(self.password_chars) for _ in range(self.password_length)]
        password: str = "".join(p)

        return password

    def __str__(self):
        """
        オブジェクトの文字列表現を返します。

        Returns:
            str: 生成されたパスワード。
        """
        return self.result_pw
