import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Nick, Like
from .converters import select_word_form, get_time_ago

class ConvertersTests(TestCase):

    """
    selected_word_form
    """

    def test_select_word_form_with_one(self):
        """
        select_word_form returns singular word form 
        when it has got '1' as a numeric parameter
        """
        number = 1
        singular = 's'
        plural = 'p'
        self.assertIs(select_word_form(number, singular, plural), singular)

    
    def test_select_word_form_with_eleven(self):
        """
        select_word_form returns plural word form 
        when it has got '11' as a numeric parameter
        """
        number = 11
        singular = 's'
        plural = 'p'
        self.assertIs(select_word_form(number, singular, plural), plural)
    
    
    def test_select_word_form_with_twenty(self):
        """
        select_word_form returns plural word form 
        when it has got '20' as a numeric parameter
        """
        number = 20
        singular = 's'
        plural = 'p'
        self.assertIs(select_word_form(number, singular, plural), plural)
    
    """
    get_time_ago
    """
    
    def test_get_time_ago_with_now(self):
        """
        get_time_ago returns '0 seconds ago'
        when it has got current timestamp
        """
        self.assertIs(get_time_ago(timezone.now()) == '0 seconds ago', True)

    
    def test_get_time_ago_with_one_second(self):
        """
        get_time_ago returns '1 second ago'
        when it has got current timestamp - 1 second
        """
        self.assertIs(get_time_ago(timezone.now() - datetime.timedelta(seconds = 1)) == '1 second ago', True)

    
    def test_get_time_ago_with_sixty_seconds(self):
        """
        get_time_ago returns '60 seconds ago'
        when it has got current timestamp - 60 seconds
        """
        self.assertIs(get_time_ago(timezone.now() - datetime.timedelta(seconds = 60)) == '60 seconds ago', True)


    def test_get_time_ago_with_sixty_one_seconds(self):
        """
        get_time_ago returns '1 minute ago'
        when it has got current timestamp - 61 seconds
        """
        self.assertIs(get_time_ago(timezone.now() - datetime.timedelta(seconds = 61)) == '1 minute ago', True)

    def test_get_time_ago_with_sixty_minutes(self):
        """
        get_time_ago returns '60 minutes ago'
        when it has got current timestamp - 60 minutes
        """
        self.assertIs(get_time_ago(timezone.now() - datetime.timedelta(minutes = 60)) == '60 minutes ago', True)


    def test_get_time_ago_with_sixty_one_minutes(self):
        """
        get_time_ago returns '1 hour ago'
        when it has got current timestamp - 61 minutes
        """
        self.assertIs(get_time_ago(timezone.now() - datetime.timedelta(minutes = 61)) == '1 hour ago', True)


    def test_get_time_ago_with_twenty_four_hours(self):
        """
        get_time_ago returns '24 hours ago'
        when it has got current timestamp - 24 hours
        """
        self.assertIs(get_time_ago(timezone.now() - datetime.timedelta(hours = 24)) == '24 hours ago', True)

    
    def test_get_time_ago_with_twenty_five_hours(self):
        """
        get_time_ago returns '1 day ago'
        when it has got current timestamp - 25 hours
        """
        self.assertIs(get_time_ago(timezone.now() - datetime.timedelta(hours = 25)) == '1 day ago', True)

    
    def test_get_time_ago_with_standard_year(self):
        """
        get_time_ago returns '365 days ago'
        when it has got current timestamp - 365 days
        """
        self.assertIs(get_time_ago(timezone.now() - datetime.timedelta(days = 365)) == '365 days ago', True)

