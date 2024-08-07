import graphene
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()

class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutations(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)
