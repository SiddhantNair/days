from days import fromDate, bleh

def test_date():
    assert fromDate('3 4 2020') == 'Friday'

def test_sum():
    assert bleh([1,2,3]) == 6