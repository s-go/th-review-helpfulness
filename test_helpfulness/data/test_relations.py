from helpfulness.data.relations import match_relation_name


class TestRelations:

    def test_match_relation_name(self):
        line = '2298..2303|Temporal.Asynchronous'
        relation_name = match_relation_name(line)
        assert relation_name == 'Temporal.Asynchronous'
