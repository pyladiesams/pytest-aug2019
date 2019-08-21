def test_example(base_url, client_mocked):
    url = base_url + "tasks/1"

    res = client_mocked.get(url)
    import pdb; pdb.set_trace()
    assert res
