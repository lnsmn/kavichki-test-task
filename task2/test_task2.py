import pytest
from task2 import post, get

TEST_ID = 1
LIST_OF_FIELDS = ['userId', 'id', 'title', 'body']
COUNT_OF_FIELDS = 4

TEST_DATA = {'id': '101', 'title': 'h1', 'body': 'healthy'}
EMPTY_DATA = {}
CUSTOM_ID = {'id': 500}
TITLE_IN_POST = {'title': 'h1'}
BODY_IN_POST = {'body': 'healthy'}
INT_USERID_IN_POST = {'userID': 1}
STR_USERID_IN_POST = {'userID': '1'}
CUSTOM_PROPERTY_IN_POST = {'something': 18}
CREATED_POST_ID = 101
CREATED_RESPONSE_CODE = 201

class Test_Get:
    def test_id_equal(self):
        res = get(TEST_ID).json()
        assert res.get('id') == TEST_ID

    def test_id_empty(self):
        res = get(TEST_ID).json()
        assert res.get('id') != ''

    def test_id_integer(self):
        res = get(TEST_ID).json().get('id')
        assert isinstance(res, int)

    def test_fields_equal(self):
        res = get(TEST_ID).json().keys()
        assert list(res) == LIST_OF_FIELDS

    def test_fields_len(self):
        res = get(TEST_ID).json().keys()
        assert list(res).__len__() == COUNT_OF_FIELDS

    def test_title_empty(self):
        res = get(TEST_ID).json()
        assert res.get('title') != ''

    def test_title_string(self):
        res = get(TEST_ID).json().get('title')
        assert isinstance(res, str)

    def test_body_empty(self):
        res = get(TEST_ID).json()
        assert res.get('body') != ''

    def test_body_string(self):
        res = get(TEST_ID).json().get('body')
        assert isinstance(res, str)

    def test_userId_empty(self):
        res = get(TEST_ID).json()
        assert res.get('userId') != ''

    def test_userId_integer(self):
        res = get(TEST_ID).json().get('userId')
        assert isinstance(res, (int, str))

class Test_Post:
    def test_status_created(self):
        res = post(TEST_DATA).status_code
        assert res == CREATED_RESPONSE_CODE

    def test_empty_created(self):
        res = post(EMPTY_DATA).status_code
        assert res == CREATED_RESPONSE_CODE

    def test_id_next(self):
        res = post(TEST_DATA).json().get('id')
        assert res == CREATED_POST_ID

    def test_id_created(self):
        res = post(EMPTY_DATA).json().get('id')
        assert res == CREATED_POST_ID

    def test_id_custom(self):
        res = post(CUSTOM_ID).json().get('id')
        assert res == CREATED_POST_ID

    def test_fields_equal(self):
        res = post(EMPTY_DATA).json().keys()
        assert list(res).__len__() == 1

    def test_id_exist(self):
        res = post(EMPTY_DATA).json().keys()
        assert ('id' in list(res))

    def test_title_not_exist(self):
        res = post(EMPTY_DATA).json().keys()
        assert ('title' in list(res)) == False

    def test_userId_not_exist(self):
        res = post(EMPTY_DATA).json().keys()
        assert ('userId' in list(res)) == False

    def test_body_not_exist(self):
        res = post(EMPTY_DATA).json().keys()
        assert ('body' in list(res)) == False

    def test_id_and_body_exist(self):
        res = post(BODY_IN_POST).json().keys()
        assert list(res).__len__() == 2
        assert ('body' in list(res))

    def test_id_and_body_exist(self):
        res = post(TITLE_IN_POST).json().keys()
        assert list(res).__len__() == 2
        assert ('title' in list(res))

    def test_id_and_custom_exist(self):
        res = post(CUSTOM_PROPERTY_IN_POST).json()
        assert isinstance(res.get('something'), str)
        assert list(res.keys()).__len__() == 2
        assert ('something' in list(res))

    def test_id_and_intUserId_exist(self):
        res = post(INT_USERID_IN_POST).json()
        assert isinstance(res.get('userID'), int) == False
        assert list(res.keys()).__len__() == 2
        assert ('userID' in list(res.keys()))

    def test_id_and_strUserId_exist(self):
        res = post(STR_USERID_IN_POST).json()
        assert isinstance(res.get('userID'), str)
        assert list(res.keys()).__len__() == 2
        assert ('userID' in list(res.keys()))