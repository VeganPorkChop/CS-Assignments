"""
Author: Graham Gilbert-Schroeer
Starting Date: 1/14/2026

Initial creation by Dietrich Geisler on 10/12/2025
Edits by Anastasia Kurdia on 1/14/2026

Test cases for the "getting to know you" analysis functions
"""

import utils
import analysis

# Constant data file information
# We use smaller data files than the "whole thing" to help us with testing
# Reminder: these are for you to use when testing also!

DATA_1 = utils.read_data('testdata1.csv')
DATA_2 = utils.read_data('testdata2.csv')
DATA_3 = utils.read_data('testdata3.csv')
DATA_4 = utils.read_data('testdata4.csv')

# TO DO: add new data files here!

# ---------------------------------------------------------
# Provided example functions
# You do not need to extend these tests

def test_first_name():
    """
    Test cases for first_name
    """
    expected = ['anonymous', 'test']
    result = analysis.first_name(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['test', 'anonymous', 'first', 'anonymous', 'ABCD', 'anonymous', 'anonymous']
    result = analysis.first_name(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    print('First name tests passed')

def test_introduction():
    """
    Test cases for introduction
    """
    expected = [
        ['Hi, this is anonymous!\n\tHello!'], 
        ['Hi, this is test!\n\tThis is a test!']
    ]
    result = analysis.introduction(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        ['Hi, this is test!\n\tthis is an introduction!'], 
        ['Hi, this is anonymous!\n\ta'], 
        ['Hi, this is ABCD!\n\t12345'], 
        ['Hi, this is anonymous!\n\thello world!']
    ]
    result = analysis.introduction(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    print('Introduction tests passed')

def test_cs_count():
    """
    Test cases for cs count
    """
    expected = 2 # note that economics has "cs" at the end, so we count it!
    result = analysis.cs_count(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 2
    result = analysis.cs_count(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    print('CS count tests passed')

# ---------------------------------------------------------
# Part 1 tests

def test_number_of_students():
    """
    Test cases for student count
    """
    expected = 2
    result = analysis.number_of_students(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 7
    result = analysis.number_of_students(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 4
    result = analysis.number_of_students(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 4
    result = analysis.number_of_students(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    print('Number of students tests passed')

def test_number_of_anonymous():
    """
    Test cases for anonymous count
    """
    expected = 1
    result = analysis.number_of_anonymous(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 4
    result = analysis.number_of_anonymous(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 0
    result = analysis.number_of_anonymous(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 0
    result = analysis.number_of_anonymous(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    print('Number of anonymous tests passed')

def test_number_of_ramen_recommends():
    """
    Test cases for ramen recommends
    """
    expected = 0
    result = analysis.number_of_ramen_recommends(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 2
    result = analysis.number_of_ramen_recommends(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 1
    result = analysis.number_of_ramen_recommends(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 1
    result = analysis.number_of_ramen_recommends(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    print('Number of ramen recommends tests passed')

# ------------------------------------------------
# Part 2 Tests

def test_first_last():
    """
    Test cases for first last
    """
    expected = ['anonymous anonymous', 'test student']
    result = analysis.first_last(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        'test student', 
        'anonymous anonymous', 
        'first last',
        'anonymous anonymous', 
        'ABCD EFGH', 
        'anonymous anonymous', 
        'anonymous anonymous'
    ]
    result = analysis.first_last(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        'Skibidi Toilet', 
        'Giga Chad', 
        'NPC ', 
        'Anonymous Anonymous'
    ]
    result = analysis.first_last(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        'Rizz King',
        'Ohio Final',
        'NPC ',
        'Anon Anon'
    ]
    result = analysis.first_last(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    print('First last tests passed')

def test_tea_enjoyers():
    """
    Test cases for tea enjoyers
    """
    expected = ['anonymous anonymous']
    result = analysis.tea_enjoyers(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['anonymous anonymous']
    result = analysis.tea_enjoyers(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = []
    result = analysis.tea_enjoyers(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['Ohio Final']
    result = analysis.tea_enjoyers(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    print('Tea enjoyer tests passed')

def test_coffee_enjoyers():
    """
    Test cases for coffee enjoyers
    """
    expected = ['test student']
    result = analysis.coffee_enjoyers(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['anonymous anonymous', 'first last']
    result = analysis.coffee_enjoyers(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['Anonymous Anonymous'] 
    result = analysis.coffee_enjoyers(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = []
    result = analysis.coffee_enjoyers(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    print('Coffee enjoyer tests passed')

def test_travelled_south():
    """
    Test cases for travelled_south
    """
    expected = ['test student (-12.123°)']
    result = analysis.travelled_south(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        'test student (9.940512411°)', 
        'anonymous anonymous (-37.81249621°)', 
        'anonymous anonymous (18.912096°)', 
        'anonymous anonymous (21.03557°)'
    ]
    result = analysis.travelled_south(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['Skibidi Toilet (-42.069°)', 'Giga Chad (-12.345°)', 'NPC  (-90.0°)']
    result = analysis.travelled_south(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['Rizz King (-66.666°)', 'NPC  (-90.0°)', 'Anon Anon (12.345°)']
    result = analysis.travelled_south(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    print('Travelled south tests passed')

# ------------------------------------------------
# Part 3 Tests

def test_list_majors():
    """
    Test cases for majors
    """
    expected = ['anonymous anonymous (Computer Science): Teleportation', 'test student (Economics): Underwater Basket Weaving']
    result = analysis.list_majors(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        'test student (biomedical engineering): kniitting', 
        'anonymous anonymous (Data Science): Pilates', 
        'first last (Materials Science and Engineering): wine design', 
        'anonymous anonymous (Industrial Engineering): travelling for fun', 
        'ABCD EFGH (CS): egyptian mythology', 
        'anonymous anonymous (Comp Sci): fire wizard', 
        'anonymous anonymous (Biomedical Engineering): Racecar driver'
    ]
    result = analysis.list_majors(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message



    print('List Major tests passed')

def test_cool_things():
    """
    Test cases for cool things
    """
    expected = [
        ['anonymous anonymous', '\twebsite', '\tvideo games'], 
        ['test student']
    ]
    result = analysis.cool_things(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        ['test student', '\tinternet', '\ta website'], 
        ['anonymous anonymous', '\tgame', '\tgame'], 
        ['first last'], 
        ['anonymous anonymous', '\tcat videos'], 
        ['ABCD EFGH', '\tgoogle earth', '\tmedical software'], 
        ['anonymous anonymous', '\tdoom', '\tprosthetics'], 
        ['anonymous anonymous']
    ]
    result = analysis.cool_things(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        ['Skibidi Toilet', '\taimbot', '\ttwitter clone'],
        ['Giga Chad', '\tML model', '\tcrypto scam'],
        ['NPC ', '\tdialog tree', '\tRPG game'],
        ['Anonymous Anonymous', '\tcat website', '\tneural implant']
    ]
    result = analysis.cool_things(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        ['Rizz King', '\tbots', '\tdating app'],
        ['Ohio Final', '\t404 page', '\tbetter life'],
        ['NPC ', '\tdialog system', '\tRPG'],
        ['Anon Anon', '\tprocedural art', '\tart website']
    ]
    result = analysis.cool_things(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    print('Cool things tests passed')

def test_emojis():
    """
    Test cases for emojis
    """
    expected = ['😟', '🍅']
    result = analysis.emojis(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['😟', '🐋', '😳', 'crying', '😛', '🌚', '🤯']
    result = analysis.emojis(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['💀', '🗿', '😐', '🤯']
    result = analysis.emojis(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = ['😈', '🫥', '😐', '💀']
    result = analysis.emojis(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    print('Emojis tests passed')

def test_study_partners():
    """
    Test cases for study partners
    """
    expected = [
        ['test student Tuesdays/Thursdays', '\torganization', '\tComplicated code']
    ]
    result = analysis.study_partners(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        ['test student after 5pm', '\tcommunication', '\tdetails of code'], 
        ['ABCD EFGH anytime', '\tmotivation', '\tintuition'], 
        ['anonymous anonymous whenever', '\tpatience', "\tI'll need some support getting going"], 
        ['anonymous anonymous 11:00-12:00', '\torganization', '\tgeneral background']
    ]
    result = analysis.study_partners(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        ['Skibidi Toilet never', '\tconfidence', '\tloops'],
        ['Giga Chad late nights', '\tvibes', '\tdebugging'],
        ['NPC  anytime', '\tconsistency', '\tthinking'],
        ['Anonymous Anonymous evenings', '\torganization', '\tstarting']
    ]
    result = analysis.study_partners(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = [
        ['Rizz King never', '\tconfidence', '\tlogic'],
        ['Ohio Final midnight', '\tperseverance', '\teverything'],
        ['NPC  anytime', '\tconsistency', '\tthinking'],
        ['Anon Anon evenings', '\tcreativity', '\tmath']
    ]
    result = analysis.study_partners(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    print('Study partners tests passed')

# ------------------------------------------------
# Part 4 Tests

def test_graduation_years():
    """
    Test cases for graduation years
    """
    # Note for these cases, the order of the dictionary keys doesn't matter!
    expected = {2026: 1, 2027: 1}
    result = analysis.graduation_years(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = {2028: 5, 2027: 1, 2029: 1}
    result = analysis.graduation_years(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = {2028: 2, 2027: 1, 2029: 1}
    result = analysis.graduation_years(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = {2028: 1, 2027: 1, 2029: 1, 2030: 1}
    result = analysis.graduation_years(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    print('Graduation years tests passed')

def test_birthday_buddies():
    """
    Test cases for birthday buddies
    """
    expected = {'1-Jan': ['anonymous anonymous', 'test student']}
    result = analysis.birthday_buddies(DATA_1)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = {'7-May': ['test student', 'ABCD EFGH'], '10-Mar': ['anonymous anonymous', 'anonymous anonymous', 'anonymous anonymous']}
    result = analysis.birthday_buddies(DATA_2)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = {}
    result = analysis.birthday_buddies(DATA_3)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = {}
    result = analysis.birthday_buddies(DATA_4)
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message
    
    print('Birthday buddies tests passed')

def test_all():
    test_first_name()
    test_introduction()
    test_cs_count()
    test_number_of_students()
    test_number_of_anonymous()
    test_number_of_ramen_recommends()
    test_first_last()
    test_tea_enjoyers()
    test_coffee_enjoyers()
    test_travelled_south()
    test_list_majors()
    test_cool_things()
    test_emojis()
    test_study_partners()
    test_graduation_years()
    test_birthday_buddies()
    print('Hooray, all tests passed!')

if __name__ == "__main__":
    test_all()