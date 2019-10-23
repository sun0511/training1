import graphene
from holy.schema import Query as PostQuery

class Query(PostQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)