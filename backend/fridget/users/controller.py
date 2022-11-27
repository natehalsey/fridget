from fridget.base.schema import User

class UserController:
    # debugging only, remove before prod
    async def get_users(self) -> list[User]:
        return await User.objects.select_related("created_recipes").all()