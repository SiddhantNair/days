from days import fromDate, bleh, nonveg_or_not

def test_date():
    assert fromDate('3 4 2020') == 'Friday'

def test_sum():
    assert bleh([1,2,3]) == 6

def test_nonveg():
    assert nonveg_or_not('14 4 2020') == True