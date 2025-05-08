from ...extensions import db
from ...models.user import User
from ...models.post import Post





class CommentService:
    def create_post(data):

        post = Post(title=data['title'], content=data['content'])
        db.session.add(post)
        db.session.commit()
        return post




