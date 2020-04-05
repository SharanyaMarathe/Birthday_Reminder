import pytest
from Birthday_reminder_test import Display_Notifications 
#Birthday_reminder_test has the notification message returned as result

test_strings=[("02-04-2014","In same month"),("01-01-1997","3Months Ago"),("11-08-2000","4Months from now")]

@pytest.mark.parametrize('date,exp',test_strings)
def test_Birthday(date,exp):
    act=Display_Notifications(date)
    assert act==exp
