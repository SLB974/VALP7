from app.core.parser import Parser

essai = "Bonjour grandpy, comment ça va ce matin ? Est-ce-que ça roule ? \
    C'est le bonheur pour toi ? Peux-tu me trouver l'adresse d'OpenClassrooms \
        sur Paris ? Est-ce-que tu connais l'adresse de Richard CADOR \
        à Nantes ?"

def test_not_none():
    ps = Parser(essai)
    result = len(ps.clean_string())
    assert result > 0

def test_not_single():
    ps = Parser(essai)
    result = len(ps.clean_string())
    assert result > 1
    
def test_space_free():
    ps = Parser(essai)
    for item in ps.clean_string():
        assert item == item.strip()
        