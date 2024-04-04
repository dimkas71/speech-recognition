import pytest

from fast_langdetect import detect_langs



# region fixtures
@pytest.fixture()
def hello_world() -> dict[str, str]:
    hello_world_phrases = {
        "en": "Hello, World!",
        "hi": "नमस्ते, दुनिया!",
        "es": "¡Hola, mundo!",
        "fr": "Bonjour, monde!",
        "zh": "你好，世界！",
        "ar": "مرحباً بالعالم!",
        "ru": "Привет, мир!",
        "pt": "Olá, mundo!",
        "bn": "ওহে, বিশ্ব!",
        "id": "Halo, dunia!",
        "ur": "ہیلو، دنیا!",
        "de": "Hallo, Welt!",
        "ja": "こんにちは、世界！",
        "tr": "Merhaba, dünya!",
        "it": "Ciao, mondo!",
        "pl": "Witaj, świecie!",
        "nl": "Hallo, wereld!",
        "th": "สวัสดี, โลก!",
        "ko": "안녕하세요, 세상!",
        "vi": "Xin chào, thế giới!",
        "sv": "Hej, världen!",
        "he": "שלום, עולם!",
        "ta": "வணக்கம், உலகம்!",
        "uk": "Привіт, світ!",
        "ro": "Salut, lume!",
        "el": "Γειά σου, κόσμε!",
        "no": "Hei, verden!",
        "fi": "Hei, maailma!",
        "da": "Hej, verden!",
        "hu": "Helló, világ!",
        "cs": "Ahoj, světe!",
        "sk": "Ahoj, svet!",
        "hr": "Pozdrav, svijete!",
        "sr": "Здраво, свете!",
        "bg": "Здравей, свят!",
        "lt": "Labas, pasauli!",
        "lv": "Sveiki, pasaule!",
        "et": "Tere, maailm!",
        "sl": "Pozdravljen, svet!",
        "mk": "Здраво, светот!",
        "sq": "Përshëndetje, bota!",
        "hy": "Ողջույն, աշխարհ!",
        "ka": "გამარჯობა, მსოფლიო!",
        "uz": "Salom, dunyo!",
        "kk": "Сәлем, әлем!",
        "az": "Salam, dünya!",
        "ky": "Салам, дүйнө!",
        "tk": "Salam, dünýä!",
        "tg": "Салом, ҷаҳон!",
    }

    return hello_world_phrases

# endregion


def test_detect_langs(hello_world) -> None:
    for key, value in hello_world.items():
        assert key.upper() == detect_langs(value, low_memory=False)