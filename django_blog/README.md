Blog Post Features
1. List Posts

URL: /posts/

View: PostListView

Description: Displays all blog posts. Accessible by all users (authenticated or not).

Template: post_list.html

2. Post Detail

URL: /posts/<int:pk>/

View: PostDetailView

Description: Shows the full content of a single post. Accessible by all users.

Template: post_detail.html

3. Create Post

URL: /posts/new/

View: PostCreateView

Permissions: Only logged-in users can create posts.

Template: post_form.html

Notes: Author is automatically set to the logged-in user.

4. Update Post

URL: /posts/<int:pk>/edit/

View: PostUpdateView

Permissions: Only the author of the post can edit it.

Template: post_form.html

5. Delete Post

URL: /posts/<int:pk>/delete/

View: PostDeleteView

Permissions: Only the author of the post can delete it.

Template: post_confirm_delete.html

Notes: After deletion, user is redirected to the post list.

Permissions & Access Control

List & Detail: Accessible to all users.

Create: Requires login (LoginRequiredMixin).

Update & Delete: Requires login and post ownership (UserPassesTestMixin).

Data Handling

PostForm ensures only title and content fields are editable.

Author is set automatically; users cannot change it manually.

CSRF protection is enabled in all forms ({% csrf_token %}).