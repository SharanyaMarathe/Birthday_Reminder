import pytest
import Display_Notifications from Birthday_reminder
import Birthday from Birthday_reminder

test_strings=[("02-04-2014","In same month"),("01-01-1997","3Months Ago"),("11-08-2000","4Months from now")]

@pytest.mark.parametrize('date,exp',test_strings)
def test_Birthday(date,exp):
    bday= Birthday(date)
    act=Notification()
    assert act==exp
