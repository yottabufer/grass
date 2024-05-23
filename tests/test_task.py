def test_tasks(test_app):
    response = test_app.get('/tasks')
    body = response.json()
    assert isinstance(body['tasks'][0].get('title'), str) is True
    assert response.status_code == 200


available_body = {
    'title': 'Write Code',
    'completed': False,
}


def test_create_positive_task(test_app):
    response = test_app.post('/tasks', json=available_body)
    assert response.status_code == 201
    assert response.json()['title'] == available_body['title']


title_is_not_exist = {
    'title': None,
    'completed': True,
}


def test_create_not_title_task(test_app):
    response = test_app.post('/tasks', json=title_is_not_exist)
    assert response.status_code == 400
    assert response.json()['detail'] == "The title cannot be empty"


string_completed_type = {
    'title': 'String type',
    'completed': 'true',
}


def test_create_string_completed_task(test_app):
    response = test_app.post('/tasks', json=string_completed_type)
    assert response.status_code == 400
    assert response.json()['detail'] == "Completed type error"
