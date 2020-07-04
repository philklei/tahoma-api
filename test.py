from tahoma_api.tahoma_api import TahomaApi, Action, Device, Command, ActionGroup, Event, Execution 

def tahoma_login():
    t = TahomaApi('philip.kleimeyer@gmail.com', '3mpgmrrk78!')
    t.get_setup()

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__main__":
    tahoma_login()
    print("Everything passed")