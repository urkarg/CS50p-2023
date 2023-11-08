import project
import pytest


def get_input_123(i):
    return "123"

def get_input_k(i):
    return "k"

def test_get_user_choice_123():
    assert project.get_user_choice(kind="roll", input_func=get_input_123) == {"1", "2", "3"}

def test_get_user_choice_k():
    assert project.get_user_choice(kind="roll", input_func=get_input_k) == "k"

def test_load_dice_file():
    assert project.load_dice_file("dices.txt")
    with pytest.raises(SystemExit):
        assert project.load_dice_file("file_is_a_lie.txt")

def test_read_score_csv():
    assert project.read_score_csv("db_score_card.csv")
    with pytest.raises(SystemExit):
        assert project.read_score_csv("file_is_a_lie.csv")

def test_dict_dict_throws():
    assert project.dict_dice_throws([1,2,3,4,5], order=["I", "II", "III", "IV", "V"]) == {"I":1, "II":2, "III":3, "IV":4, "V":5}
    assert project.dict_dice_throws([1,2,2,4,6], order=["I", "II", "III", "IV", "V"]) == {"I":1, "II":2, "III":2, "IV":4, "V":6}
    with pytest.raises(SystemExit):
        assert project.dict_dice_throws([1], order=["a", "b"]) == {"a":1}
    with pytest.raises(SystemExit):
        assert project.dict_dice_throws([1, 2, 3], order=["a", "b"])

def test_correlate_dice_values():
    assert project.correlate_dice_values({"I":1, "II":3},{"1":"a", "3":"B"}) == {"I":"a", "II":"B"}
    with pytest.raises(SystemExit):
        assert project.correlate_dice_values({"I":1, "II":4},{"1":"a", "3":"B"}) == {"I":"a", "II":"B"}

def test_convert_set_reroll_to_order_list():
    assert set(project.convert_set_reroll_to_order_list({"1","2","3"})) == set(["I", "II", "III"])
    with pytest.raises(SystemExit):
        assert project.convert_set_reroll_to_order_list({"cat"})
