import matchers as m

class QueryBuilder:
    def __init__(self, query = m.All()):
        self.query = query
    
    def build(self):
        return self.query

    def plays_in(self, team):
        return QueryBuilder(m.And(self.query, m.PlaysIn(team)))
    
    def has_at_least(self, value, attr):
        return QueryBuilder(m.And(self.query, m.HasAtLeast(value, attr)))
    
    def has_fewer_than(self, value, attr):
        return QueryBuilder(m.And(self.query, m.HasFewerThan(value, attr)))

    def oneOf(self, *matchers):
        return QueryBuilder(m.Or(*matchers))

