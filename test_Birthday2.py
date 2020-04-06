import pytest
from Birthday_reminder_test2 import Display_Notifications 


test_strings=[("02-04-2020","Last Month"),("15-03-2020","Today"),("11-01-2020","2Months from now")]

@pytest.mark.parametrize('date,exp',test_strings)
def test_Birthday(date,exp):
    act=Display_Notifications(date)
    assert act==exp
